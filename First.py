# Import required modules
import requests, json

# Enter your API key here
api_key = "906e9450851e85944b4a293e5c8162b7"

# Base URL variable to store URL
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Enter city name: ")

# Complete URL variable to store
# complete URL address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# Get method of requests module
# return response object
response = requests.get(complete_url)

# JSON method of response object 
# convert JSON format data into
# Python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check if the value of "cod" key is not equal to
# "404", which means the city is found
if x["cod"] != "404":

    # Store the value of "main" key in variable y
    y = x["main"]

    # Store the value corresponding to the "temp" key of y
    current_temperature = y["temp"]

    # Store the value corresponding to the "pressure" key of y
    current_pressure = y["pressure"]

    # Store the value corresponding to the "humidity" key of y
    current_humidity = y["humidity"]

    # Store the value of "weather" key in variable z
    z = x["weather"]

    # Store the value corresponding to the "description" key at 
    # the 0th index of z
    weather_description = z[0]["description"]

    # Print the following values
    print("Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\nAtmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\nHumidity (in percentage) = " +
                    str(current_humidity) +
          "\nDescription = " +
                    str(weather_description))
    
    # Check for extreme weather conditions
    if current_temperature > 313.15:  # Example: Alert if temperature > 40°C
        print("Alert: Extreme heat detected!")
    
    if current_humidity > 80:  # Example: Alert if humidity > 80%
        print("Alert: High humidity levels detected! Risk of heavy rain.")
    
    if "rain" in weather_description or "storm" in weather_description:
        print("Alert: Severe weather detected! Risk of flooding or storms.")
    
    # You can add more conditions for other types of weather alerts
    
else:
    print("City Not Found")
