# WeatherSales
A simple program to display sales and the corresponding weather data of the sales place. This happend out of the idea that weather/cahnge in weather has an influence on the buying decision of customers

## sales_pipe.py
sales_pipe.py returns a pandas dataframe containing these columns:

| sale id | item id | category | zip code | 

with the weather_pipe.py function you add the columns "Temperature" and "Description" to the previous dataframe

### Temperature
Shows the Temperature at the place the item got sold

### Description
Gives information about the weather situation e.g. "clear sky"

Build your crendentials.json file the following:

{

  
  "openweather_api_key": "YOUR API KEY"

}

Get your key here:

https://openweathermap.org/api
