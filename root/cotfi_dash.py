# 1. Librerias

import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd 
from dash.dependencies import Input,Output

# 2. Formato y templates

external_stylesheet=['https://codepen.io/chriddyp/pen/bWLwgp.css']
tickFont = {'size':9, 'color':"rgb(50,50,50)"}

# 3. Declaración  de la función para el objeto data

def loadData(filename):
    data = pd.read_csv('root\FieldStrengthvsChannel.csv')
    return data

# 4. Lectura de los datos

data = loadData("FieldStrengthvsChannel.csv")
#data = data.drop(['Variable_1','Variable_2','Variable_n'], axis = 1) # Descarta variables no deseadas en el eje 1 que es columnas
#data.melt(id_vars=['Nombre/columna'], var_name='date', value_name="Medido") # Transposicion para una base ancha a una base larga
#data = data.astype({'date':'datetime64[ns]',"Medidos":'Int64'}, errors='ignore')
#data['datestr'] = data['date'].dt.strftime('%b %d, %Y') #formato de fecha mes dia y año # https://strftime.org/

# 5. Preparando una lista

#frequencys = data['Frequency (MHz)'].unique()
#frequencys.sort()

# 6. Dashboard Layout

app = dash.Dash(__name__)
  
    #Header 1 tipo banner Html renderizado
app.layout = html.Div([#Acá van los cuatro elementos del dashboard El Banner, el radio de botones y los dos graficos
    
    html.Div([
        html.H1('Gerencia de Telecomunicaciones: CoTFI'),
        html.Img(src='assets/antena.png')
    ], className = 'banner'),
 html.Div([
        html.H1('Mediciones de Espectro Radioeléctrico para FM'),
       
    ], className = 'banner'),
]) #Fin del layout

# Creación de botones de seleccion de parametros

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


app.run_server(port=5050)