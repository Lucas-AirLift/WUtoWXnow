import requests
import datetime
import time

API_KEY = "INSERT API KEY HERE"
STATION_ID = "INSERT STATION ID HERE"
FILE_PATH = "WXnow.txt"

def get_weather_data(api_key, station_id):
    url = f"https://api.weather.com/v2/pws/observations/current?stationId={station_id}&format=json&units=e&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def convert_pressure(pressure):
    # Convert inches of mercury to millibars (in tenths of a millibar)
    millibars = int(pressure * 33.86389 * 10)
    return millibars

def generate_wxnow_file(weather_data, file_path):
    observation = weather_data.get('observations', [])
    if observation:
        current_observation = observation[0]
        temperature = int(current_observation.get('imperial', {}).get('temp', 0))
        wind_speed = int(current_observation.get('imperial', {}).get('windSpeed', 0))
        wind_gust = int(current_observation.get('imperial', {}).get('windGust', 0))
        wind_dir = int(current_observation.get('winddir', 0))
        humidity = int(current_observation.get('humidity', 0))
        pressure = convert_pressure(float(current_observation.get('imperial', {}).get('pressure', 0)))
        precip_rate = int(current_observation.get('imperial', {}).get('precipRate', 0))
        precip_total = int(current_observation.get('imperial', {}).get('precipTotal', 0))

        wx_report = f"{wind_dir:03d}/{wind_speed:03d}g{wind_gust:03d}t{temperature:03d}r{precip_rate:03d}p{precip_total:03d}h{humidity:02d}b{pressure:05d}"

        current_time = datetime.datetime.now().strftime("%b %d %Y %H:%M")
        wx_report_with_time = f"{current_time}\n{wx_report}"

        with open(file_path, 'w') as file:
            file.write(wx_report_with_time)
    else:
        print("No weather data found.")

def main(api_key, station_id, file_path):
    while True:
        try:
            weather_data = get_weather_data(api_key, station_id)
            generate_wxnow_file(weather_data, file_path)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Retrying...")
            time.sleep(60)
        else:
            time.sleep(60)

if __name__ == '__main__':
    main(API_KEY, STATION_ID, FILE_PATH)
