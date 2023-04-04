import requests
from auth import KIWIAPI
from pprint import pprint

KIWI_END_POINT = "https://api.tequila.kiwi.com/locations/query"
HEADER = dict()
HEADER["apikey"] = f"{KIWIAPI}"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.IATAS = []

    def get(self, country):
        new_data = {"term": country}
        try:
            request = requests.get(url=KIWI_END_POINT, headers=HEADER, params=new_data)
            self.IATAS = request.json()
        except Exception as e:
            print("couldnt find the required country")
            return None
        return self.IATAS["locations"][0]["code"]
