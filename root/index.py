import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output

df = pd.read_csv('root\FieldStrengthvsChannel.csv')
df_filtrado = df.fillna(0) #Filtra los datos vacios con ceros
#print(df)
#print(df.vacuna_nombre.nunique())
#print(df.vacuna_nombre.unique())

app = dash.Dash(__name__)

app.layout = html.Div([#Acá van los cuatro elementos del dashboard El Banner, el radio de botones y los dos graficos
    
    html.Div([
        html.H1('Gerencia de Telecomunicaciones: CoTFI'),
        html.Img(src='assets/antena.png')
    ], className = 'banner'),
    html.Div([
        html.H1('Mediciones de Espectro Radioeléctrico para FM'),
       
    ], className = 'banner'),

    html.Div([
        html.Div([
            html.P('Selecciona El Parámetro', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'mediciones-radioitems', 
                            labelStyle = {'display': 'inline-block'},
                            options = [
                                {'label' : 'Campo Eléctrico Max (dBuV/m)', 'value' : 'Maximum Field Strength (dBuV/m)'},
                                {'label' : 'Campo Eléctrico Prom (dBuV/m)', 'value' : 'Average Field Strength (dBuV/m)'}
                            ], value = 'Maximum Field Strength (dBuV/m)',#Para que aparezca por defecto la primera opción
                            style = {'text-aling':'center', 'color':'black'}, className = 'dcc_compon'),
        ], className = 'create_container2 five columns', style = {'margin-bottom': '20px'}),
    ], className = 'row flex-display'),

    html.Div([#Crea el grafico de barras
        html.Div([
            dcc.Graph(id = 'my_graph', figure = {})
        ], className = 'create_container2 eight columns'),

        html.Div([#Crea el gráfico de pastel
            dcc.Graph(id = 'pie_graph', figure = {})
        ], className = 'create_container2 five columns')
    ], className = 'row flex-display'),

], id='mainContainer', style={'display':'flex', 'flex-direction':'column'})

@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('mediciones-radioitems', component_property='value')])

def update_graph(value):

    if value == 'Maximum Field Strength (dBuV/m)':
        fig = px.bar(
            data_frame = df,
            x = 'Frequency (MHz)',
            y = 'Maximum Field Strength (dBuV/m)', barmode='group')
    else:
        fig = px.bar(
            data_frame= df,
            x = 'Frequency (MHz)',
            y = 'Average Field Strength (dBuV/m)')
    return fig

@app.callback(
    Output('pie_graph', component_property='figure'),
    [Input('mediciones-radioitems', component_property='value')])

def update_graph_pie(value):

    if value == 'Maximum Field Strength (dBuV/m)':
        fig2 = px.pie(
            data_frame = df,
            names = 'Frequency (MHz)',
            values = 'Maximum Field Strength (dBuV/m)')
    else:
        fig2 = px.pie(
            data_frame = df,
            names = 'Frequency (MHz)',
            values = 'Average Field Strength (dBuV/m)'
        )
    return fig2

if __name__ == ('__main__'):
    app.run_server(port=8050)