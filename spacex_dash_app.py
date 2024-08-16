# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

unique_launch_sites = spacex_df['Launch Site'].unique()

# Create a list of dictionaries for dropdown options
unique_launch_sites_options = [{'label': 'All Sites', 'value': 'ALL'}]  # Start with the 'All Sites' option
unique_launch_sites_options.extend([{'label': site, 'value': site} for site in unique_launch_sites])

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36',
                   'font-size': 40}),
    # Dropdown for Launch Site selection
    dcc.Dropdown(id='site-dropdown',
                 options=unique_launch_sites_options,
                 value='ALL',
                 placeholder="Select a Launch Site here",
                 searchable=True,
                 style={'width': '80%', 'margin': '0 auto'}
                 ),
    html.Br(),

    # Pie chart for total successful launches
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    # Payload range slider label and display
    html.P("Payload range (Kg):"),
    html.Div(id='slider-output-container', style={'textAlign': 'center', 'margin-bottom': '20px'}),
    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                    value=[min_payload, max_payload],
                    tooltip={"placement": "bottom", "always_visible": True},
                    allowCross=False,
                    updatemode='drag',
                    ),

    # Scatter chart for correlation between payload and launch success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


# Callback to update the displayed payload range values
@app.callback(
    Output('slider-output-container', 'children'),
    [Input('payload-slider', 'value')]
)
def update_output(value):
    return f"Selected Payload Range: {value[0]} Kg - {value[1]} Kg"


# Callback for the pie chart
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='class',
                     names='Launch Site',
                     title='Total Success Launches For all Sites')
    else:
        filtered_df = spacex_df.loc[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(filtered_df,
                     names='class',
                     title=f'Total Success Launches for Site {entered_site}')
    return fig


# Callback for the scatter plot
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id="payload-slider", component_property="value")])
def get_scatter_plot(selected_site, payload_range):
    if selected_site == 'ALL':
        filtered_df = spacex_df
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]

    filtered_df = filtered_df[
        (filtered_df['Payload Mass (kg)'] >= payload_range[0]) &
        (filtered_df['Payload Mass (kg)'] <= payload_range[1])
    ]

    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title=f'Success by Payload Mass for site {selected_site}',
        labels={'class': 'Launch Success'}
    )

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server()
