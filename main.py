import re
import requests
import time

import export
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_site_information(hotel, sites):
    for site in sites:
        if site["website_base_url"] in hotel["hotel_url"]:
            current_site = site
            break
    return current_site


def get_page_content(hotel):
    html_content = requests.get(hotel["hotel_url"])
    soup = BeautifulSoup(html_content.text, "html5lib")
    return soup


def clean_number(number):
    number = remove_substring(number, [" ", "تومان", ",", "ریال", "\n", "\r", "-"])
    digits = {"۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6",
              "۷": "7", "۸": "8", "۹": "9", "۰": "0"}
    number = re.compile('|'.join(digits.keys())).sub(lambda x: digits[x.group()], number)
    return number


def clean_hotel_name(name):
    remove_substring(name, ["\t", "\n"])
    return name


def remove_substring(string, substring):
    for word in substring:
        string = string.replace(word, '')
    return string

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def build_rooms_data_from_html(current_site, soup, hotel):
    rooms = list()
    rooms_price = [clean_number(price.text) for price in soup.select(current_site[
                                                                         "room_price_selector"])]
    rooms_name = [clean_hotel_name(name.text) for name in soup.select(current_site["room_name_selector"])]
    # TODO this condition should be removed.
    if len(rooms_name) == len(rooms_price):
        for room_idx in range(len(rooms_name)):

            if is_int(rooms_price[room_idx]):
                current_price = int(rooms_price[room_idx])
            else:
                pass

            # TODO this condition should be removed.
            if rooms_name[room_idx] == '' or rooms_price[room_idx] == '':
                continue
            # print("roon name count: " + str(len(rooms_name)) + ", roon price count: " + str(len(rooms_price)))
            room = dict()
            room["hotel_name"] = hotel["hotel_name"]
            room["room_name"] = rooms_name[room_idx]
            room["website_name"] = current_site["website_name"]
            room["price"] = str(current_price * 10) if current_site["is_toman"] == 'TRUE' else rooms_price[room_idx]
            room["date"] = time.strftime("%Y/%m/%d")
            rooms += [room]

    return rooms


def build_rooms_data_from_json(current_site, json, hotel):
    return ["A"]


def get_google_spreadsheet_data(title, sheet):
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open(title).worksheet(sheet)
    data = sheet.get_all_records()
    return data


def get_json_content(hotel):
    return True


def main():
    rooms = list()

    hotels = get_google_spreadsheet_data('Hotels Price Collector', 'hotel')
    sites = get_google_spreadsheet_data('Hotels Price Collector', 'site')

    for hotel in hotels:
        current_site = get_site_information(hotel, sites)
        if hotel["ajax_request_place_id"] == "-":
            soup = get_page_content(hotel)
            rooms += build_rooms_data_from_html(current_site, soup, hotel)
        else:
            json = get_json_content(hotel)
            rooms += build_rooms_data_from_json(current_site, json, hotel)

    # export.write_csv(rooms)
    export.write_html(rooms)
