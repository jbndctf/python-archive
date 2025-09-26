import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
api_key = os.getenv("API_KEY")


def main():
    address = input("Address: ")
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url)
    if response.ok:
        geocode = response.json()
        size = 0
        for i, result in enumerate(geocode["results"]):
            print(f"{i}    {result['formatted_address']}")
            size += 1
        try:
            address_index = int(input("Address Index: "))
        except ValueError:
            print("Address does not exist.")
            return
        if address_index < 0 or address_index >= size:
            print("Address does not exist.")
            return
        lat = geocode["results"][address_index]["geometry"]["location"]["lat"]
        lng = geocode["results"][address_index]["geometry"]["location"]["lng"]
        print(f"Latitude: {lat} Degrees")
        print(f"Longitude: {lng} Degrees")
        url = f"https://weather.googleapis.com/v1/currentConditions:lookup?key={api_key}&location.latitude={lat}&location.longitude={lng}"
        response = requests.get(url)
        if response.ok:
            weather = response.json()
            current_time = weather["currentTime"]
            time_zone = weather["timeZone"]["id"]
            is_daytime = weather["isDaytime"]
            weather_condition_description = weather["weatherCondition"]["description"][
                "text"
            ]
            temperature_degrees = weather["temperature"]["degrees"]
            temperature_unit = weather["temperature"]["unit"]
            feels_like_temperature_degrees = weather["feelsLikeTemperature"]["degrees"]
            feels_like_temperature_unit = weather["feelsLikeTemperature"]["unit"]
            dew_point_degrees = weather["dewPoint"]["degrees"]
            dew_point_unit = weather["dewPoint"]["unit"]
            heat_index_degrees = weather["heatIndex"]["degrees"]
            heat_index_unit = weather["heatIndex"]["unit"]
            wind_chill_degrees = weather["windChill"]["degrees"]
            wind_chill_unit = weather["windChill"]["unit"]
            relative_humidity = weather["relativeHumidity"]
            uv_index = weather["uvIndex"]
            precipitation_probability = weather["precipitation"]["probability"][
                "percent"
            ]
            precipitation_type = weather["precipitation"]["probability"]["type"]
            qpf_quantity = weather["precipitation"]["qpf"]["quantity"]
            qpf_unit = weather["precipitation"]["qpf"]["unit"]
            thunderstorm_probability = weather["thunderstormProbability"]
            air_pressure = weather["airPressure"]["meanSeaLevelMillibars"]
            wind_direction_degrees = weather["wind"]["direction"]["degrees"]
            wind_direction_cardinal = weather["wind"]["direction"]["cardinal"]
            wind_speed_value = weather["wind"]["speed"]["value"]
            wind_speed_unit = weather["wind"]["speed"]["unit"]
            wind_gust_value = weather["wind"]["gust"]["value"]
            wind_gust_unit = weather["wind"]["gust"]["unit"]
            visibility_distance = weather["visibility"]["distance"]
            visibility_unit = weather["visibility"]["unit"]
            cloud_cover = weather["cloudCover"]
            temperature_change_history_degrees = weather["currentConditionsHistory"][
                "temperatureChange"
            ]["degrees"]
            temperature_change_history_unit = weather["currentConditionsHistory"][
                "temperatureChange"
            ]["unit"]
            max_temperature_history_degrees = weather["currentConditionsHistory"][
                "maxTemperature"
            ]["degrees"]
            max_temperature_history_unit = weather["currentConditionsHistory"][
                "maxTemperature"
            ]["unit"]
            min_temperature_history_degrees = weather["currentConditionsHistory"][
                "minTemperature"
            ]["degrees"]
            min_temperature_history_unit = weather["currentConditionsHistory"][
                "minTemperature"
            ]["unit"]
            qpf_history_quantity = weather["currentConditionsHistory"]["qpf"][
                "quantity"
            ]
            qpf_history_unit = weather["currentConditionsHistory"]["qpf"]["unit"]
            print(pd.to_datetime(current_time).round("s").strftime("%Y-%m-%d %-I %p"))
            print(time_zone)
            if is_daytime:
                print("Day")
            else:
                print("Night")
            print(f"Weather Condition: {weather_condition_description}")
            print(
                f"Temperature: {temperature_degrees} Degrees {temperature_unit.replace('_', ' ').title()}"
            )
            print(
                f"Feels Like Temperature: {feels_like_temperature_degrees} Degrees {feels_like_temperature_unit.replace('_', ' ').title()}"
            )
            print(
                f"Dew Point: {dew_point_degrees} Degrees {dew_point_unit.replace('_', ' ').title()}"
            )
            print(
                f"Heat Index: {heat_index_degrees} Degrees {heat_index_unit.replace('_', ' ').title()}"
            )
            print(
                f"Wind Chill: {wind_chill_degrees} Degrees {wind_chill_unit.replace('_', ' ').title()}"
            )
            print(f"Relative Humidity: {relative_humidity}%")
            print(f"UV Index: {uv_index}")
            print(
                f"Probability of {precipitation_type.replace('_', ' ').title()}: {precipitation_probability}%"
            )
            print(f"QPF: {qpf_quantity} {qpf_unit.replace('_', ' ').title()}")
            print(f"Probability of Thunderstorm: {thunderstorm_probability}%")
            print(f"Air Pressure: {air_pressure} hPa")
            print(
                f"Wind Direction: {wind_direction_degrees} Degrees or {wind_direction_cardinal.replace('_', ' ').title()}"
            )
            print(
                f"Wind Speed: {wind_speed_value} {wind_speed_unit.replace('_', ' ').title()}"
            )
            print(
                f"Wind Gust: {wind_gust_value} {wind_gust_unit.replace('_', ' ').title()}"
            )
            print(
                f"Visibility: {visibility_distance} {visibility_unit.replace('_', ' ').title()}"
            )
            print(f"Cloud Cover: {cloud_cover}%")
            print(
                f"Temperature Change History: {temperature_change_history_degrees} Degrees {temperature_change_history_unit.replace('_', ' ').title()}"
            )
            print(
                f"Max Temperature History: {max_temperature_history_degrees} Degrees {max_temperature_history_unit.replace('_', ' ').title()}"
            )
            print(
                f"Min Temperature History: {min_temperature_history_degrees} Degrees {min_temperature_history_unit.replace('_', ' ').title()}"
            )
            print(
                f"QPF History: {qpf_history_quantity} {qpf_history_unit.replace('_', ' ').title()}"
            )
        else:
            print(f"Request failed with status code: {response.status_code}")
    else:
        print(f"Request failed with status code: {response.status_code}")


if __name__ == "__main__":
    main()
