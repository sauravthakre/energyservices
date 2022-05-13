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

tourists = tourism.iloc[:12916, :]

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
#
# Turismo_dormidas=Turismo.iloc[12933:25849,:] #Finding Overnights in the file
#
# Turismo_dormidas=Turismo_dormidas.drop(columns={'zona_geo_h','hospedes_tipo_aloj','hospedes_mes','textbox23','textbox25'})
# Turismo_dormidas=Turismo_dormidas.drop(columns={'textbox27','textbox28','textbox29'})
# #Eliminating columns that are not important
# Turismo_dormidas=Turismo_dormidas.rename(columns={'hospedes_anos':'Year','textbox9':'Dormidas'})
# #Rename columns
#
# Turismo_dormidas['Dormidas']=Turismo_dormidas['Dormidas'].apply(lambda x: str(x).replace(" ",""))
# Turismo_dormidas['Dormidas']=Turismo_dormidas['Dormidas'].apply(lambda x: str(x).replace("-","0"))
# Turismo_dormidas['Dormidas']=Turismo_dormidas['Dormidas'].astype('int64')
# Turismo_dormidas['Year']=Turismo_dormidas['Year'].astype('int64')
# #Originally the number have spaces between and in some cases that don't have data (-). In this way fixing that and transforming
# #into a number.
#
# Turismo_dormidas=Turismo_dormidas.groupby('Year') #Group the data by the Year
# Turismo_dormidas=Turismo_dormidas.sum() #Sum of all overnights data by year
#
# Turismo_dormidas
