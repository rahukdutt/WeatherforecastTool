import requests
import json
import datetime
import sys
API_KEY='b0fabe127a83d5680834a44bb740713d' # API key for openweathermap.org

def getWeather(City):
    # Get weather data from openweathermap.org
    # Return weather data as a dictionary
    # Return None if error
    # API call: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
    # Example: api.openweathermap.org/data/2.5/weather?q=London&appid=b0fabe127a83d5680834a44bb740713d
    # API call returns a JSON object
    # Example: {"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":300,"main":"Drizzle","description":"light intensity drizzle","icon":"09d"}],"base":"stations","main":{"temp":280.32,"pressure":1012,"humidity":81,"temp_min":279.15,"temp_max":281.15},"visibility":10000,"wind":{"speed":4.1,"deg":80},"clouds":{"all":90},"dt":1485789600,"sys":{"type":1,"id":5091,"message":0.0103,"country":"GB","sunrise":1485762037,"sunset":1485794875},"id":2643743,"name":"London","cod":200}
    # API call returns a status code
    # Parse the JSON object & prints all the weather parameters
    # Example: 200
    # API call returns current weather forecast for the city
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(City, API_KEY)
    print(url)
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data
    else:    
        return None     
    
def printWeather(data):
    print('Weather forecast for {}'.format(data['name']))
    print('Current weather: {}'.format(data['weather'][0]['description']))
    print('Temperature: {} degrees F'.format(data['main']['temp']))
    print('Humidity: {}%'.format(data['main']['humidity']))
    print('Wind speed: {} mph'.format(data['wind']['speed']))
    print('Cloud cover: {}%'.format(data['clouds']['all']))
    print('Sunrise: {}'.format(datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')))
    print('Sunset: {}'.format(datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')))
    
if __name__ == "__main__":
    # Get weather forecast for a city
    # Print weather forecast
    print('Weather forecast tool')
    if len(sys.argv) < 2:
        print('Usage: WeatherForecastTool.py <city name>')
        sys.exit()
    city = ' '.join(sys.argv[1:])
    print('Getting weather forecast for {}'.format(city))
    data = getWeather(city)
    if data:
        printWeather(data)
    else:
        print('Error getting weather forecast for {}'.format(city))   

        
    
