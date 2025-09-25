import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def main():
    address = input("Address: ")
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url)
    if response.ok:
        print("Request was successful")
        geocode = response.json()
        lat = geocode["results"][0]["geometry"]["location"]["lat"]
        lng = geocode["results"][0]["geometry"]["location"]["lng"]
        print(f"Latitude: {lat}")
        print(f"Longitude: {lng}")
        url = f"https://weather.googleapis.com/v1/currentConditions:lookup?key={api_key}&location.latitude={lat}&location.longitude={lng}"
        response = requests.get(url)
        if response.ok:
            print("Request was successful")
            weather = response.json()
            print(weather)
        else:
            print(f"Request failed with status code: {response.status_code}")
    else:
        print(f"Request failed with status code: {response.status_code}")


if __name__ == "__main__":
    main()
