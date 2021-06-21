import requests

from datetime import datetime

api = '641c0de8fc1d154e5baae10f9f775509'
location = input('Enter location: ')

complete_api_url = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+api

appdata = requests.get(complete_api_url)

appdata_json = appdata.json()

#create variables to store and display data
temp_city = ((appdata_json['main']['temp']) - 273.15)
weather_desc = appdata_json['weather'][0]['description']
hmdt = appdata_json['main']['humidity']
wind_spd = appdata_json['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
with open('weatherinfo.txt','w') as f:
    f.write('-------------------------------------------------------------\n')
    f.write("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
    f.write('-------------------------------------------------------------\n')
    f.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
    f.write("Current weather desc  :"+weather_desc+'\n')
    f.write("Current Humidity      :"+str(hmdt)+ ' %\n')
    f.write("Current wind speed    : "+str(wind_spd) +' kmph\n')
f.close()