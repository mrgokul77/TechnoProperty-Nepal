import os
import datetime
from read import read_invoice_info, read_land_info


def generate_invoice(note, file_name):
    with open(file_name, 'w') as file:
        file.write(note)


def rent_land_transaction():
    kitta_number = input("\nEnter Kitta Number of the land to rent (or 'e' to exit): ")
    if kitta_number.lower() == 'e':
        return
    if not kitta_number.isdigit():
        print("Invalid input! Please enter a valid Kitta Number.")
        return
    customer_name = input("\nPlease enter your name: ")
    rental_duration = input("\nPlease enter duration of rent (in months): ")
    if not rental_duration.isdigit():
        print("Invalid input! Please enter a valid duration.")
        return
    land_info = read_land_info("land_info.txt")
    if kitta_number in land_info and land_info[kitta_number][-1] == 'Available':
        city, direction, area, price, _ = land_info[kitta_number]
        total_amount = int(price) * int(rental_duration)
        land_info[kitta_number] = (city, direction, area, price, 'Not Available')
        update_land_info("land_info.txt", land_info)
        
        existing_invoice_file = f"rent_invoice_{customer_name}.txt"
        if os.path.exists(existing_invoice_file):
            with open(existing_invoice_file, 'a') as invoice_file:
                note = f"\n\nRenting of Land\nKitta Number: {kitta_number}\nCity: {city}\nDirection: {direction}\nArea: {area} anna\nDate and Time of Rent: {datetime.datetime.now()}\nAggreed duration for rent: {rental_duration} \nTotal Amount: {total_amount} NPR"
                invoice_file.write(note)
        else:
            note = f"Renting of Land\nKitta Number: {kitta_number}\nCity: {city}\nDirection: {direction}\nArea: {area} anna\nCustomer: {customer_name}\nDate and Time of Rent: {datetime.datetime.now()}\nAggreed duration for rent: {rental_duration} \nTotal Amount: {total_amount} NPR"
            file_name = f"rent_invoice_{customer_name}.txt"
            generate_invoice(note, file_name)
            print("Invoice generated for rent transaction.")
    else:
        print("Land not available for rent.")


def return_land_transaction():
    kitta_number = input("Enter Kitta Number of the land to return (or 'e' to exit): ")
    if kitta_number.lower() == 'e':
        return
    if not kitta_number.isdigit():
        print("Invalid input! Please enter a valid Kitta Number.")
        return
    customer_name = input("\nPlease enter your name: ")
    returned_duration = input("\nEnter the duration of rent (in months) for the land being returned: ")
    if not returned_duration.isdigit():
        print("Invalid input! Please enter a valid duration.")
        return
    land_info = read_land_info("land_info.txt")
    if kitta_number in land_info and land_info[kitta_number][-1] == 'Not Available':
        city, direction, area, price = land_info[kitta_number][:-1]
        returned_duration = int(returned_duration)
        rent_invoice_file = f"rent_invoice_{customer_name}.txt"
        rent_invoice_info = read_invoice_info(rent_invoice_file)
        if rent_invoice_info:
            returned_duration_str = rent_invoice_info.get("Aggreed duration for rent", "0")
            rented_duration_in_invoice = int( returned_duration_str)
            if returned_duration > rented_duration_in_invoice:
                exceeded_months = returned_duration - rented_duration_in_invoice
                fine = exceeded_months * 10000
            else:
                fine = 0
        else:
            fine = 0

        total_amount = int(price) * returned_duration + fine

        land_info[kitta_number] = (city, direction, area, price, 'Available')
        update_land_info("land_info.txt", land_info)
        note = f"Returning of Land\nCustomer: {customer_name}\nKitta Number: {kitta_number}\nCity: {city}\nDirection: {direction}\nDate and Time of Return: {datetime.datetime.now()}\nDuration of Rent: {returned_duration} months\nArea: {area} anna\nFine:{fine}\nTotal Amount: {total_amount} NPR (including fine of {fine} NPR)"
        file_name = f"return_invoice_{customer_name}.txt"
        generate_invoice(note, file_name)
        print("Invoice generated for return transaction.")
    else:
        print("Land not rented.")


def update_land_info(file_name, land_info):
    with open(file_name, 'w') as file:
        for kitta_number, land in land_info.items():
            line = f"{kitta_number},{','.join(map(str, land))}\n"
            file.write(line)


if __name__ == "__main__":
    rent_land_transaction()
    return_land_transaction()