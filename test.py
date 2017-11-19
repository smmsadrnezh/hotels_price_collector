import requests
from main import clean_number, clean_hotel_name
from bs4 import BeautifulSoup


def test():
    hotel_url = "https://www.eghamat24.com/TehranHotels/ParsianAzadiHotel.html"
    room_price_selector = "div.tr section.td.td_five.table_grey.room_price div.hotel_room_price div.hotel_room_price_new.r_left p ,div.hotel_room_price_none > span + span"
    room_name_selector = "html body main div div div div div.hotel_reservation_main.hotel_table_main div.table.table_block.table_row_border div.tbody div.tr section.td.td_three.room-info label"
    custom_selector = "div.hotel_reservation_main.hotel_table_main " \
                      "div.table.table_block.table_row_border div.tbody div.tr div.hotel_room_price " \
                      "div.hotel_room_price_new.r_left p, div.hotel_reservation_main.hotel_table_main " \
                      "div.table.table_block.table_row_border div.tbody " \
                      "div.tr div.hotel_room_price"

    html_content = requests.post(hotel_url)
    soup = BeautifulSoup(html_content.text, "html5lib")
    rooms_price = [clean_number(price.text) for price in soup.select(room_price_selector)]
    rooms_name = [clean_hotel_name(name.text) for name in soup.select(room_name_selector)]

    for i in soup.select(custom_selector):
        print(i , "\nAAAAAAAAAA\n")
    print(rooms_price)
    print(rooms_name)


test()
