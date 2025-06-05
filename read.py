
def read_land_info(file_name):
    land_info = {}
    try:
        with open("land_info.txt", 'r') as file:
          for line in file:
            parts = line.strip().split(',')
            kitta_number = parts[0]
            city = parts[1]
            direction = parts[2]
            area = int(parts[3])
            price = int(parts[4])
            availability = parts[5].strip()  
            land_info[kitta_number] = (city, direction, area, price, availability)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")       
    return land_info

def read_invoice_info(file_name):
    invoice_info = {}
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if ': ' in line:
                    key, value = line.split(': ', 1)
                    invoice_info[key] = value
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    return invoice_info
