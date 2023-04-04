from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from datetime import date
from pprint import pprint


# objects
def main():
    today = date.today()
    weekday = today.weekday()
    if weekday == 6:
        data_manager = DataManager()
        flight_data = FlightData()
        notification_manager = NotificationManager()

        # get all the users from the sheet and IATAS
        IATAS = data_manager.get_IATAS()
        list_of_users = data_manager.get_users()
        print(list_of_users, len(IATAS))

        # make it csv file then convert to excel
        flight_data.get(IATAS)
        flight_data.make_it_csv()
        flight_data.convert_to_excel()

        # send the deals
        # notification_manager.send_deals(list_of_users)
    else:
        print("Not today")


if __name__ == "__main__":
    main()
