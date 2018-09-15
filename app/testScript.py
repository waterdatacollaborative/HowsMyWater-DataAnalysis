import requests
import pandas as pd
import numpy as np

watsysDf = pd.read_csv("../watsys.csv", encoding='cp1252')
watsysDf = watsysDf.drop_duplicates(subset='SYSTEM_NO')
#watsysDf = watsysDf.head(n=100)
watsysDf['latitude'] = pd.Series(np.random.randn(len(watsysDf)), index=watsysDf.index)
watsysDf['longitude'] = pd.Series(np.random.randn(len(watsysDf)), index=watsysDf.index)
watsysDf['updatedAddress'] = pd.Series(np.random.randn(len(watsysDf)), index=watsysDf.index)

# m = folium.Map(location=[36.7783, -119.4179], zoom_start=6)
for index, row in watsysDf.iterrows():
	if (pd.notna(row['ADDRESS'])):
		address = str(row['ADDRESS'])+" "+str(row['CITY'])+" "+str(row['STATE'])+" "+str(row['ZIP'])
	elif (pd.notna(row['SYSTEM_NAM'])):
		address = row['SYSTEM_NAM']
	else:
		pass
	print(address)
	row['updatedAddress'] = address
	api_key = "AIzaSyCxXF9S5YimyZfj0NdbtUNeajaPPCVPGpQ"
	api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
	api_response_dict = api_response.json()

	if api_response_dict['status'] == 'OK':
		latitude = api_response_dict['results'][0]['geometry']['location']['lat']
		longitude = api_response_dict['results'][0]['geometry']['location']['lng']
		row['latitude'] = latitude
		row['longitude'] = longitude

cols_to_keep = ['SYSTEM_NO', 'SYSTEM_NAM', 'ADDRESS', 'latitude', 'longitude']
watsysDf[cols_to_keep].to_json('waterSources.json')
