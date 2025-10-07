#!/usr/bin/env python3

"""
Weather

Prompts user for an address, then fectches and prints weather information.
"""

import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
API_KEY: str | None = os.getenv("API_KEY")

GEOCODE_URL: str = (
    "https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
)

WEATHER_URL: str = "https://weather.googleapis.com/v1/currentConditions:lookup?key={api_key}&location.latitude={lat}&location.longitude={lng}"

INVALID_INDEX_MESSAGE: str = "Invalid index."
INDEX_OUT_OF_RANGE_MESSAGE: str = "Index out of range."
LATITUDE_MESSAGE: str = "Latitude: {lat} Degrees"
LONGITUDE_MESSAGE: str = "Longitude: {lng} Degrees"
FAILED_REQUEST_MESSAGE: str = "Request failed with status code: {status_code}"
ADDRESS_DOES_NOT_EXIST_MESSAGE: str = "Address does not exist."
TIME_MESSAGE = "Time: {time}"
TIMEZONE_MESSAGE = "Time Zone: {time_zone}"
DAYTIME_MESSAGE = "Daytime: {daytime}"
WEATHER_CONDITION_MESSAGE = "Weather Condition: {weather_condition}"
TEMPERATURE_MESSAGE = "Temperature: {degrees} °{unit}"
FEELS_LIKE_TEMPERATURE_MESSAGE = "Feels Like Temperature: {degrees} °{unit}"
DEW_POINT_MESSAGE = "Dew Point: {degrees} °{unit}"
HEAT_INDEX_MESSAGE = "Heat Index: {degrees} °{unit}"
WIND_CHILL_MESSAGE = "Wind Chill: {degrees} °{unit}"
RELATIVE_HUMIDITY_MESSAGE = "Relative Humidity: {relative_humidity}%"
UV_INDEX_MESSAGE = "UV Index: {uv_index}"
PRECIPITATION_MESSAGE = "Probability of {type}: {probability}%"
QPF_MESSAGE = "QPF: {quantity} {unit}"
THUNDERSTORM_MESSAGE = "Probability of Thunderstorm: {probability}%"
AIR_PRESSURE_MESSAGE = "Air Pressure: {air_pressure} hPa"
WIND_DIRECTION_MESSAGE = "Wind Direction: {degrees}° or {cardinal}"
WIND_SPEED_MESSAGE = "Wind Speed: {value} {unit}"
WIND_GUST_MESSAGE = "Wind Gust: {value} {unit}"
VISIBILITY_MESSAGE = "Visibility: {distance} {unit}"
CLOUD_COVER_MESSAGE = "Cloud Cover: {cloud_cover}%"
TEMPERATURE_CHANGE_HISTORY_MESSAGE = "Temperature Change History: {degrees} °{unit}"
MAX_TEMPERATURE_HISTORY_MESSAGE = "Max Temperature History: {degrees} °{unit}"
MIN_TEMPERATURE_HISTORY_MESSAGE = "Min Temperature History: {degrees} °{unit}"
QPF_HISTORY_MESSAGE = "QPF History: {quantity} {unit}"

PROMPT_ADDRESS_INDEX: str = "Enter an address index: "
PROMPT_ADDRESS: str = "Enter an Address: "


def is_valid_address_index(address_index: int, size: int) -> bool:
    """
    Checks that the address index is within the valid range of [0, size - 1]

    Args:
        address_index (int): the index of the address list.
        size (int): The size of the address list.

    Returns:
        bool: True, if the address index is within the valid range.
        False otherwise
    """
    return 0 <= address_index <= size - 1


def get_geocode(address: str) -> None | tuple[float, float]:
    """
    Fetches the longitude and latitude of an address.

    Args:
        address (str): The address or location to be found.

    Returns:
        tuple[float, float]: The longitude and latitude of the address.
    """
    url: str = GEOCODE_URL.format(address=address, api_key=API_KEY)
    response: object = requests.get(url)

    if not response.ok:
        print(FAILED_REQUEST_MESSAGE.format(status_code=response.status_code))
        return None

    geocode: dict = response.json()
    results: list = geocode["results"]

    if not results:
        print(ADDRESS_DOES_NOT_EXIST_MESSAGE)
        return None

    for i, result in enumerate(results):
        print(f"{i}    {result['formatted_address']}")

    try:
        address_index: int = int(input(PROMPT_ADDRESS_INDEX))
    except ValueError:
        print(INVALID_INDEX_MESSAGE)
        return None

    if not is_valid_address_index(address_index, len(results)):
        print(INDEX_OUT_OF_RANGE_MESSAGE)
        return None

    lat: float = results[address_index]["geometry"]["location"]["lat"]
    lng: float = results[address_index]["geometry"]["location"]["lng"]
    return lat, lng


def output_geocode(lat: float, lng: float) -> None:
    """
    Prints the longitude and latitude.
    """
    print(LATITUDE_MESSAGE.format(lat=lat))
    print(LONGITUDE_MESSAGE.format(lng=lng))


def get_weather(lat: float, lng: float) -> dict | None:
    """
    Gets weather information at a longitude and latitude.

    Args:
        lat (float): Latitude
        lng (float): Longitude

    Returns:
        dict: Weather information
        None: No weather information found
    """
    url: str = WEATHER_URL.format(api_key=API_KEY, lat=lat, lng=lng)
    response: object = requests.get(url)

    if not response.ok:
        print(FAILED_REQUEST_MESSAGE.format(status_code=response.status_code))
        return None

    weather: dict = response.json()
    return weather


def prettify(message: str) -> str:
    """
    Formats a message.

    Args:
        message (str): A message to format.

    Returns:
        str: A formatted message
    """
    return message.replace("_", " ").title()


def output_weather(weather: dict) -> None:
    """
    Prints weather information.

    Args:
        weather (dict): Weather information.
    """
    current_time: str = weather["currentTime"]
    current_time: str = (
        pd.to_datetime(current_time).round("s").strftime("%Y-%m-%d %-I %p")
    )

    time_zone: str = weather["timeZone"]["id"]

    is_daytime: bool = weather["isDaytime"]

    weather_condition: str = weather["weatherCondition"]["description"]["text"]

    temp_degrees: float = weather["temperature"]["degrees"]
    temp_unit: str = prettify(weather["temperature"]["unit"])

    feels_like_temp: dict = weather["feelsLikeTemperature"]
    feels_like_temp_degrees: float = feels_like_temp["degrees"]
    feels_like_temp_unit: str = prettify(feels_like_temp["unit"])

    dew_point_degrees: float = weather["dewPoint"]["degrees"]
    dew_point_unit: str = prettify(weather["dewPoint"]["unit"])

    heat_index_degrees: float = weather["heatIndex"]["degrees"]
    heat_index_unit: str = prettify(weather["heatIndex"]["unit"])

    wind_chill_degrees: float = weather["windChill"]["degrees"]
    wind_chill_unit: str = prettify(weather["windChill"]["unit"])

    relative_humidity: float = weather["relativeHumidity"]

    uv_index: float = weather["uvIndex"]

    precipitation: dict = weather["precipitation"]["probability"]
    precipitation_probability: float = precipitation["percent"]
    precipitation_type: str = prettify(precipitation["type"])

    qpf_quantity: float = weather["precipitation"]["qpf"]["quantity"]
    qpf_unit: str = prettify(weather["precipitation"]["qpf"]["unit"])

    thunderstorm_probability: float = weather["thunderstormProbability"]

    air_pressure: float = weather["airPressure"]["meanSeaLevelMillibars"]

    wind_direction_degrees: float = weather["wind"]["direction"]["degrees"]
    wind_direction_cardinal: str = weather["wind"]["direction"]["cardinal"]
    wind_direction_cardinal: str = prettify(wind_direction_cardinal)

    wind_speed_value: float = weather["wind"]["speed"]["value"]
    wind_speed_unit: str = prettify(weather["wind"]["speed"]["unit"])

    wind_gust_value: float = weather["wind"]["gust"]["value"]
    wind_gust_unit: str = prettify(weather["wind"]["gust"]["unit"])

    visibility_distance: float = weather["visibility"]["distance"]
    visibility_unit: str = prettify(weather["visibility"]["unit"])

    cloud_cover: float = weather["cloudCover"]

    history: dict = weather["currentConditionsHistory"]

    temp_change_history: dict = history["temperatureChange"]
    temp_change_history_degrees: float = temp_change_history["degrees"]
    temp_change_history_unit: str = temp_change_history["unit"]
    temp_change_history_unit: str = prettify(temp_change_history_unit)

    max_temp_history_degrees: float = history["maxTemperature"]["degrees"]
    max_temp_history_unit: str = prettify(history["maxTemperature"]["unit"])

    min_temp_history_degrees: float = history["minTemperature"]["degrees"]
    min_temp_history_unit: str = prettify(history["minTemperature"]["unit"])

    qpf_history_quantity: float = history["qpf"]["quantity"]
    qpf_history_unit: str = prettify(history["qpf"]["unit"])

    daytime = "Day"
    if not is_daytime:
        daytime = "Night"

    print(TIME_MESSAGE.format(time=current_time))
    print(TIMEZONE_MESSAGE.format(time_zone=time_zone))
    print(DAYTIME_MESSAGE.format(daytime=daytime))
    print(WEATHER_CONDITION_MESSAGE.format(weather_condition=weather_condition))
    print(TEMPERATURE_MESSAGE.format(degrees=temp_degrees, unit=temp_unit))
    print(
        FEELS_LIKE_TEMPERATURE_MESSAGE.format(
            degrees=feels_like_temp_degrees, unit=feels_like_temp_unit
        )
    )
    print(DEW_POINT_MESSAGE.format(degrees=dew_point_degrees, unit=dew_point_unit))
    print(HEAT_INDEX_MESSAGE.format(degrees=heat_index_degrees, unit=heat_index_unit))
    print(WIND_CHILL_MESSAGE.format(degrees=wind_chill_degrees, unit=wind_chill_unit))
    print(RELATIVE_HUMIDITY_MESSAGE.format(relative_humidity=relative_humidity))
    print(UV_INDEX_MESSAGE.format(uv_index=uv_index))
    print(
        PRECIPITATION_MESSAGE.format(
            type=precipitation_type, probability=precipitation_probability
        )
    )
    print(QPF_MESSAGE.format(quantity=qpf_quantity, unit=qpf_unit))
    print(THUNDERSTORM_MESSAGE.format(probability=thunderstorm_probability))
    print(AIR_PRESSURE_MESSAGE.format(air_pressure=air_pressure))
    print(
        WIND_DIRECTION_MESSAGE.format(
            degrees=wind_direction_degrees, cardinal=wind_direction_cardinal
        )
    )
    print(WIND_SPEED_MESSAGE.format(value=wind_speed_value, unit=wind_speed_unit))
    print(WIND_GUST_MESSAGE.format(value=wind_gust_value, unit=wind_gust_unit))
    print(VISIBILITY_MESSAGE.format(distance=visibility_distance, unit=visibility_unit))
    print(CLOUD_COVER_MESSAGE.format(cloud_cover=cloud_cover))
    print(
        TEMPERATURE_CHANGE_HISTORY_MESSAGE.format(
            degrees=temp_change_history_degrees, unit=temp_change_history_unit
        )
    )
    print(
        MAX_TEMPERATURE_HISTORY_MESSAGE.format(
            degrees=max_temp_history_degrees, unit=max_temp_history_unit
        )
    )
    print(
        MIN_TEMPERATURE_HISTORY_MESSAGE.format(
            degrees=min_temp_history_degrees, unit=min_temp_history_unit
        )
    )
    print(
        QPF_HISTORY_MESSAGE.format(quantity=qpf_history_quantity, unit=qpf_history_unit)
    )


def main() -> None:
    """
    Weather program

    Prompts user for an address, then fectches and prints weather information.
    """
    address: str = input(PROMPT_ADDRESS)

    geocode: tuple[float, float] | None = get_geocode(address)
    if not geocode:
        return
    lat, lng = geocode
    output_geocode(lat, lng)

    weather: dict | None = get_weather(lat, lng)
    if not weather:
        return
    output_weather(weather)


if __name__ == "__main__":
    main()
