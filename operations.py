import datetime
from read import read_land_info


def display_available_lands():
    land_info = read_land_info("land_info.txt")
    for kitta_number, (city, direction, area, price, availability) in land_info.items():
        if availability == 'Available':
            print(f"Kitta Number: {kitta_number}, City: {city}, Direction: {direction}, Area: {area} anna, Price: {price}, Availability: {availability}")

def display_unavailable_lands():
    land_info = read_land_info("land_info.txt")
    for kitta_number, (city, direction, area, price, availability) in land_info.items():
        if availability == 'Not Available':
            print(f"Kitta Number: {kitta_number}, City: {city}, Direction: {direction}, Area: {area} anna, Price: {price}, Availability: {availability}")




