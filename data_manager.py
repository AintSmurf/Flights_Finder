import requests
from auth import GOOGLETOKEN
from flight_search import FlightSearch
from flight_data import FlightData


SHEETY_PRICES_ENDPOINT = (
    "https://api.sheety.co/8087dbb80005e8a3b46dd2c9b8dc9af0/flightDeals/prices"
)

SHEETY_USERS_ENDPOINT = (
    "https://api.sheety.co/8087dbb80005e8a3b46dd2c9b8dc9af0/flightDeals/users"
)

HEADER = dict()
HEADER["Authorization"] = f"Bearer {GOOGLETOKEN}"
HEADER["Content-Type"] = "application/json"


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.flight_search = FlightSearch()
        self.flight_data = FlightData()

    def get(self):
        # 1. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADER)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # 2. update the IATA through the flight search api (KIWI)
    def put(self):
        for city in self.destination_data:
            try:
                code = self.flight_search.get(city["city"])
                new_data = {"price": {"iataCode": code}}
                response = requests.put(
                    url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                    json=new_data,
                    headers=HEADER,
                )
            except Exception as e:
                print("failed to retrive the IATA", e)

    def get_users(self):
        ls = []
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=HEADER)
        data = response.json()
        users = data["users"]
        for x in users:
            ls.append(x["email"])
        return ls

    def get_user_id(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=HEADER)
        data = response.json()
        users = data["users"]
        return users

    def add_user(self, email, token):
        new_data = {"user": {"email": email, "token": token}}
        response = requests.post(
            url=SHEETY_USERS_ENDPOINT,
            json=new_data,
            headers=HEADER,
        )

    def validate_user(self, email):
        ls = self.get_users()
        return email in ls

    def get_IATAS(self):
        ls = []
        data = self.get()
        for x in range(len(data)):
            ls.append(data[x]["iataCode"])
        return ls

    def update_prices(self):
        for city in self.destination_data:
            print(city["iataCode"])
            temp_dic = self.flight_data.update_prices("TLV", city["iataCode"])
            try:
                price = temp_dic["price"]
                if price is None:
                    price = 0
                new_data = {"price": {"lowestPrice": price}}
                response = requests.put(
                    url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                    json=new_data,
                    headers=HEADER,
                )
                print(response.status_code)
            except Exception as e:
                print(e, "failed to update")

    def delete_user(self, email):
        id = 0
        dic = self.get_user_id()
        for tk in dic:
            try:
                if email == tk["email"]:
                    id = tk["id"]
                    response = requests.delete(
                        url=f"{SHEETY_USERS_ENDPOINT}/{id}", headers=HEADER
                    )
                    print(response.status_code)
                    print(response)
                    return True
            except Exception as e:
                print("User does not exist", e)
        return False
