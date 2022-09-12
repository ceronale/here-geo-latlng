#!pip install here-location-services
import pandas as pd
from tqdm import tqdm
import json
import os

#HERE API
from here_location_services import LS
from here_location_services import PlatformCredentials
#ROUTE OF THE CREDENTIALS
platform_credentials = PlatformCredentials.from_credentials_file(r'./credentials.properties')
ls = LS(platform_credentials=platform_credentials) 
#ROUTE XLSX
df = pd.read_csv (r'./list_of_real_usa_addresses.csv')

#ADDRESS LIST
address = (df['address'])
address

#SET LONGITUDE AND LATITUDE
cont=0;
for x in tqdm(address):
    try:
      print(x)
      geo = ls.geocode(query=x)
      cor = geo.to_geojson()['features'][0]["properties"]["access"][0]
      df.at[cont,'latitude']=cor['lat']
      df.at[cont,'longitude']=cor['lng']
      cont=cont+1
    except:
      df.at[cont,'latitude']=0
      df.at[cont,'longitude']=0
      cont=cont+1

df.to_csv (r'latitudeAndLongitude.csv', index = False, header=True)