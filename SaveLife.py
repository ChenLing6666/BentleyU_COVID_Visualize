import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import base64
import numpy as np
from datetime import date
import plotly.graph_objects as go




stylesheet = ['https://codepen.io/chriddyp/pen/dZVMbK.css']
image_filename = 'covidimage2.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
app = dash.Dash(__name__, external_stylesheets=stylesheet)
server = app.server
df_pop = pd.read_csv('population.csv')
df_total = pd.read_csv('df.csv')
df_total['date']= pd.to_datetime(df_total['date'], format =  '%m/%d/%Y')
df_total.set_index('date', inplace = True)
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

def generate_df_summaryTable():
    positiveName = ['positive' + '_' + state for state in states]
    negativeName = ['negative' + '_' + state for state in states]
    deathName = ['death' + '_' + state for state in states]
    totalPositive = np.sum(df_total.loc[:, positiveName].iloc[-1, :])
    totalNegative = np.sum(df_total.loc[:, negativeName].iloc[-1, :])
    totalDeath = np.sum(df_total.loc[:, deathName].iloc[-1, :])
    dictDF = {'Location' : ['The United States'], 'Total Positive' : [totalPositive], 'Total Negative' : [totalNegative], 'Total Death':[totalDeath]}
    df_summary = pd.DataFrame(dictDF)
    return df_summary

df_summaryData = generate_df_summaryTable()


app.layout = html.Div([
    html.H1('The Tracker of the COVID-19 in U.S. ', style={'color': 'black', 'textAlign': 'center', 'font-style': 'oblique'}),
    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())),
    html.Div([
        html.H2('Case Summary'),
        html.H5('Last updated at 12/19/2020'),
        generate_table(df_summaryData)
    ]),
    html.Br(),
    html.Br(),

    html.Div([html.H5('Date Range for COVID (From 1/22/2020 thru. 12/09/2020)', style = {'font-style': 'italic',
                                                                                         'font-weight': 'bold'}),
            dcc.DatePickerRange(id='dateSelect',
                                min_date_allowed=date(2020, 1, 22),
                                max_date_allowed=date(2020, 12, 9),
                                start_date=date(2020, 1, 22),
                                end_date_placeholder_text='Select a date!'),
            html.H5('Features(y-axis) to Show', style = {'font-style': 'italic',
                                                         'font-weight': 'bold'}),
            dcc.Dropdown(options=[  {'label': 'Positive Cases', 'value': 'positive'},
                                    {'label': 'Negative Cases', 'value': 'negative'},
                                    {'label': 'Death', 'value': 'death'},
                                    {'label': 'Positive Increase', 'value': 'positiveIncrease'},
                                    {'label': 'Negative Increase', 'value': 'negativeIncrease'},
                                    {'label': 'Death Increase', 'value': 'deathIncrease'},
                                    {'label': 'Hospitalized Increase', 'value': 'hospitalizedIncrease'}],
                            value="positive",
                            id = 'featureSelect',
                            style={'width': '49%'}),
            html.H5('States to Show on the Righthand Side Plot', style = {'font-style': 'italic',
                                                         'font-weight': 'bold'}),
            dcc.Checklist(options=[{'label': 'Alabama ', 'value': 'AL'},
                                   {'label': 'Alaska ', 'value': 'AK'},
                                   {'label': 'Arizona ', 'value': 'AZ'},
                                   {'label': 'Arkansas ', 'value': 'AR'},
                                   {'label': 'California ', 'value': 'CA'},
                                   {'label': 'Colorado ', 'value': 'CO'},
                                   {'label': 'Connecticut ', 'value': 'CT'},
                                   {'label': 'Delaware ', 'value': 'DE'},
                                   {'label': 'Florida ', 'value': 'FL'},
                                   {'label': 'Georgia ', 'value': 'GA'},
                                   {'label': 'Hawaii ', 'value': 'HI'},
                                   {'label': 'Idaho ', 'value': 'ID'},
                                   {'label': 'Illinois ', 'value': 'IL'},
                                   {'label': 'Indiana ', 'value': 'IN'},
                                   {'label': 'Iowa ', 'value': 'IA'},
                                   {'label': 'Kansas ', 'value': 'KS'},
                                   {'label': 'Kentucky ', 'value': 'KY'},
                                   {'label': 'Louisiana ', 'value': 'LA'},
                                   {'label': 'Maine ', 'value': 'ME'},
                                   {'label': 'Maryland ', 'value': 'MD'},
                                   {'label': 'Massachusetts ', 'value': 'MA'},
                                   {'label': 'Michigan ', 'value': 'MI'},
                                   {'label': 'Minnesota ', 'value': 'MN'},
                                   {'label': 'Mississippi ', 'value': 'MS'},
                                   {'label': 'Missouri ', 'value': 'MO'},
                                   {'label': 'Montana ', 'value': 'MT'},
                                   {'label': 'Nebraska ', 'value': 'NE'},
                                   {'label': 'Nevada ', 'value': 'NV'},
                                   {'label': 'New Hampshire ', 'value': 'NH'},
                                   {'label': 'New Jersey ', 'value': 'NJ'},
                                   {'label': 'New Mexico ', 'value': 'NM'},
                                   {'label': 'New York ', 'value': 'NY'},
                                   {'label': 'North Carolina ', 'value': 'NC'},
                                   {'label': 'North Dakota ', 'value': 'ND'},
                                   {'label': 'Ohio ', 'value': 'OH'},
                                   {'label': 'Oklahoma ', 'value': 'OK'},
                                   {'label': 'Oregon ', 'value': 'OR'},
                                   {'label': 'Pennsylvania ', 'value': 'PA'},
                                   {'label': 'Rhode Island ', 'value': 'RI'},
                                   {'label': 'South Carolina ', 'value': 'SC'},
                                   {'label': 'South Dakota ', 'value': 'SD'},
                                   {'label': 'Tennessee ', 'value': 'TN'},
                                   {'label': 'Texas ', 'value': 'TX'},
                                   {'label': 'Utah ', 'value': 'UT'},
                                   {'label': 'Vermont ', 'value': 'VT'},
                                   {'label': 'Virginia ', 'value': 'VA'},
                                   {'label': 'Washington ', 'value': 'WA'},
                                   {'label': 'West Virginia ', 'value': 'WV'},
                                   {'label': 'Wisconsin ', 'value': 'WI'},
                                   {'label': 'Wyoming ', 'value': 'WY'}],

                          value=['AL', 'AK', 'AZ', 'AR', 'CA'],
                          labelStyle={'display': 'inline-block'},
                          id = '5StatesCheckList',
                          style={'width': '49%'}),
            html.Br(),
            html.Div(id = 'OutputofChoices')                

            ],style={'width': '49%', 'display': 'inline-block'}),
            html.Div([html.H5('Time Series Plot', style={'color': 'black', 'textAlign': 'center', 'font-style': 'oblique'}),
                      dcc.Graph(id="time-series-chart")],
            style={'width': '49%', 'display': 'inline-block', 'float': 'right'}),
            html.Br(),
            html.Br(),
            html.Div([html.H5('Property Selection for GeoPlot'),
                      html.Div('Date'),
                      dcc.DatePickerSingle(id='GeoPlotDate',
                                           min_date_allowed=date(2020, 1, 22),
                                           max_date_allowed=date(2020, 12, 9),
                                           initial_visible_month=date(2020, 12, 9),
                                           date=date(2020, 12, 9)),
                      html.Div('Metric to Present on the Plot'),
                      dcc.Dropdown(options=[  {'label': 'Positive Cases', 'value': 'positive'},
                                              {'label': 'Death', 'value': 'death'},
                                              {'label': 'Positive Increase', 'value': 'positiveIncrease'},
                                              {'label': 'Death Increase', 'value': 'deathIncrease'}],
                                   value="positive",
                                   id = 'GeoFeature',
                                   style={'width': '49%'}),
                      html.Div(dcc.Graph(id = 'GeoPlot'))]),
            html.Div(dcc.Graph(id = 'PopulationPlot'))
    ])







@app.callback(
    Output(component_id='OutputofChoices', component_property='children'),
    [Input(component_id='dateSelect', component_property='start_date'),
     Input(component_id='dateSelect', component_property='end_date'),
     Input(component_id='featureSelect', component_property='value'),
     Input(component_id='5StatesCheckList', component_property='value')]
)
def update_output(input_value1, input_value2, input_value3, input_value4):
    if len(input_value4) != 0:
        return 'The date you chose is from {} to {}, \nThe feature is {}, \nThe states are {}'.format(input_value1, input_value2, input_value3, input_value4)
    else:
        return 'Please select at least ONE state!'


@app.callback(
    Output(component_id="time-series-chart", component_property="figure"),
    [Input(component_id='dateSelect', component_property='start_date'),
     Input(component_id='dateSelect', component_property='end_date'),
     Input(component_id='featureSelect', component_property='value'),
     Input(component_id='5StatesCheckList', component_property='value')]
)
def display_time_series(input_value1, input_value2, input_value3, input_value4):
    df_sub1 = df_total.loc[input_value1:input_value2, :]
    featureLst = []
    for state in input_value4:
        featureLst.append(input_value3 + '_' + state)
    if len(input_value4) == 0:
        featureLst = [input_value3 + '_' + 'AL']
        df_sub2 = df_sub1[featureLst]
        fig = px.line(df_sub2, x = df_sub2.index , y = featureLst)
        return fig
    else:
        df_sub2 = df_sub1[featureLst]
        fig = px.line(df_sub2, x = df_sub2.index , y = featureLst)
        fig.update_xaxes(rangeslider_visible=True)
        return fig


@app.callback(
    Output(component_id="GeoPlot", component_property="figure"),
    [Input(component_id='GeoPlotDate', component_property='date'),
     Input(component_id='GeoFeature', component_property='value')]
)
def display_geoPlot(input_value1, input_value2):
    metric = []
    for state in states:
        metric.append(df_total.loc[input_value1, input_value2 + '_' + state])
    dct = {'code':states, input_value2:metric}
    df_metric = pd.DataFrame(dct, columns = ['code', input_value2])

        
    df_space = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

    df_geo = pd.merge(df_space, df_metric, on='code')
    lstofScale = sorted(df_geo[input_value2].values)
    lower = np.percentile(lstofScale, 15)
    upper = np.percentile(lstofScale, 70)
    fig_1 = go.Figure(data=go.Choropleth(
                    locations=df_geo['code'], # Spatial coordinates
                    z = df_geo[input_value2].astype(float), # Data to be color-coded
                    locationmode = 'USA-states', # set of locations match entries in `locations`
                    colorscale = 'Reds',
                    colorbar_title = input_value2,
                    zmax = upper,
                    zmin = lower
                    
                    ))

    fig_1.update_layout(title_text = '2020 US COVID-19 by State',
                      geo_scope='usa',
                      height = 700,
                      width = 1900)
    return fig_1


@app.callback(
    Output(component_id="PopulationPlot", component_property="figure"),
    [Input(component_id='GeoPlotDate', component_property='date')]
)
def display_populationPlot(input_value1):
        
    df_space = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

    df_geo = pd.merge(df_space, df_pop, on='code')
    lstofScale = sorted(df_geo['Population'].values)
    lower = np.percentile(lstofScale, 15)
    upper = np.percentile(lstofScale, 70)
    fig_2 = go.Figure(data=go.Choropleth(
                    locations=df_geo['code'], # Spatial coordinates
                    z = df_geo['Population'].astype(float), # Data to be color-coded
                    locationmode = 'USA-states', # set of locations match entries in `locations`
                    colorscale = 'Blues',
                    colorbar_title = 'Population',
                    zmax = upper,
                    zmin = lower
                    
                    ))

    fig_2.update_layout(title_text = '2019 US Population by State',
                      geo_scope='usa',
                      height = 700,
                      width = 1900)
    return fig_2








if __name__ == '__main__':
    app.run_server(debug=True)