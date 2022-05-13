import numpy as np
import pandas as pd
import xlrd
from matplotlib import pyplot as plt

population = pd.read_excel('Demografia.xls', sheet_name='Q.02.02')
immigrants = pd.read_excel('Demografia.xls', sheet_name='Q.02.05')
demogr_rates = pd.read_excel('Demografia.xls', sheet_name='q.02.04')
prod = pd.read_csv('Energia-Produção.csv')
consum = pd.read_csv('Energia-Consumo.csv')
prod_type = pd.read_excel('Energia e Agua.xls', sheet_name='Q1301')
consum_type = pd.read_excel('Energia e Agua.xls', sheet_name='Q1302')
tourism = pd.read_csv('Hospedes Dormidas e Estada Media por Ilha.csv')
passengers = pd.read_csv('Transportes-Aéreos.csv')
water = pd.read_excel('Energia e Agua.xls', sheet_name='Q1303')

tourists = tourism.iloc[:13462, :]

tourists = tourists.drop(columns={'zona_geo_h', 'hospedes_tipo_aloj', 'hospedes_mes', 'textbox23', 'textbox25',
                                  'textbox27', 'textbox28', 'textbox29'})
tourists = tourists.rename(columns={'hospedes_anos': 'Year', 'textbox9': 'Tourists'})

tourists['Tourists'] = tourists['Tourists'].apply(lambda x: str(x).replace(" ", ""))
tourists['Tourists'] = tourists['Tourists'].apply(lambda x: str(x).replace("-", "0"))
tourists['Tourists'] = tourists['Tourists'].astype('int64')

tourists['Year'] = tourists['Year'].astype('int64')
tourists = tourists.groupby('Year')
tourists = tourists.sum()
print(tourists)

overnight = tourism.iloc[13463:26925, :] # Finding Overnights in the file

overnight=overnight.drop(columns={'zona_geo_h', 'hospedes_tipo_aloj', 'hospedes_mes', 'textbox23', 'textbox25',
                                                'textbox27', 'textbox28', 'textbox29'})

overnight=overnight.rename(columns={'hospedes_anos': 'Year', 'textbox9': 'Night Guests'})

overnight['Night Guests'] = overnight['Night Guests'].apply(lambda x: str(x).replace(" ",""))
overnight['Night Guests'] = overnight['Night Guests'].apply(lambda x: str(x).replace("-","0"))
overnight['Night Guests'] = overnight['Night Guests'].astype('int64')
overnight['Year'] = overnight['Year'].astype('int64')

overnight=overnight.groupby('Year')
overnight=overnight.sum()

print(overnight)
