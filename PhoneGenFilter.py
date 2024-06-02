# © @Nyx_FallagaTn
# This code is open source and protected under the MIT License.
# Educational Purposes only :)
# Unauthorized use, modification, or distribution of this code is strictly prohibited.

import os
import re
import fontstyle
import phonenumbers
from datetime import date
from phonenumbers import carrier
from phone_gen import PhoneNumber
from multiprocessing.dummy import Pool

fg = '\033[92m'
fr = '\033[91m'
fw = '\033[97m'
fy = '\033[93m'
fb = '\033[94m'
flc = '\033[96m'

today = date.today()
d1 = today.strftime("%d_%m_%Y")

allphones = []
count = 0

countries = ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW", "BV", "BR", "IO", "BN", "BG", "BF", "BI", "CV", "KH", "CM", "CA", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "SZ", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES", "LK", "SD", "SR", "SJ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN", "VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]

def logo():
    msg = """{}       ⣰⡆                      ⠐⣆       \     ⣴⠁⡇    {}@Nyx_FallagaTn{}    ⢀⠃⢣\     ⢻ ⠸⡀                     ⡜ ⢸⠇         \    ⠘⡄⢆⠑⡄     ⢀⣀⣀⣠⣄⣀⣀⡀     ⢀⠜⢠⢀⡆          \     ⠘⣜⣦⠈⢢⡀⣀⣴⣾⣿⡛⠛⠛⠛⠛⠛⡿⣿⣦⣄ ⡠⠋⣰⢧⠎           \      ⠘⣿⣧⢀⠉⢻⡟⠁⠙⠃    ⠈⠋ ⠹⡟⠉⢠⢰⣿⠏           \       ⠘⣿⡎⢆⣸⡄          ⠠⣿⣠⢣⣿⠏             \       ⡖⠻⣿⠼⢽            ⢹⠹⣾⠟⢳⡄           \       ⡟⡇⢨ ⢸⡀           ⡎ ⣇⢠⢿⠇           \       ⢹⠃⢻⡤⠚    {}⣀  ⢀{}    ⠙⠢⡼ ⢻   \       ⠸⡓⡄{}⢹⠦⠤⠤⠤⢾⣇  ⢠⡷⠦⠤⠤⠴⢺{}⢁⠔⡟  \       ⢠⠁⣷{}⠈⠓⠤⠤⠤⣞⡻  ⢸⣱⣤⠤⠤⠔⠁{}⣸⡆⣇   \       ⠘⢲⠋⢦⣀⣠⢴⠶ {}⠁  ⠈⠁{}⠴⣶⣄⣀⡴⠋⣷⠋   \        ⣿⡀  ⢀⡘⠶⣄⡀   ⣠⡴⠞⣶ ⢀ ⣼              \        ⠈⠻⣌⢢⢸⣷⣸⡈⠳⠦⠤⠞⠁⣷⣼⡏⣰⢃⡾⠋              \          ⠙⢿⣿⣿⡇⢻⡶⣦⣤⡴⡾⢸⣿⣿⣷⠏               \            ⢿⡟⡿⡄⣳⣤⣤⣴⢁⣾⠏⡿⠁                 \            ⠈⣷⠘⠒⠚⠉⠉⠑⠒⠊⣸⠇                 \             ⠈⠳⠶⠔⠒⠒⠲⠴⠞⠋{}              \ """.format(fg,fr,fg,fr,fg,fr,fg,fr,fg,fr,fg,fw)
    lines = [line.center(os.get_terminal_size().columns, " ") for line in msg.split('\\')]
    for line in lines:
        print(fontstyle.apply(line, 'bold/GREEN'))
    print()

def format_string(string):
    return re.sub(r'[<>:"/\\|?*]', '', string.replace(' ', '_'))

def check_number(number):
    try:
        parsed_number = phonenumbers.parse(number)
        carrier_name = carrier.name_for_number(parsed_number, 'en')
        if carrier_name:
            print(f"[{fr}#{fw}] {number} [{fg}{carrier_name}{fw}]")
            with open(f'Results/Output_{d1}/{country}/{format_string(carrier_name)}.txt', 'a', errors='ignore') as f:
                f.write(number + '\n')
    except phonenumbers.phonenumberutil.NumberParseException:
        print(f"{number} => Invalid number")

def checker():
    global count
    while True:
        phone_number = PhoneNumber(country).get_number()
        if phone_number not in allphones:
            check_number(phone_number)
            allphones.append(phone_number)
            count += 1

if __name__ == "__main__":
    logo()
    while True:
        country = input(f'[{fg}#{fw}] Which country to work on: ')
        if country in countries:
            break

    os.system('cls')
    logo()

    result_dir = f'Results/Output_{d1}/{country}'
    os.makedirs(result_dir, exist_ok=True)

    print(f'[{fg}#{fw}] Country: {fg}{country}{fw}')
    print(f'[{fg}#{fw}] Results will be saved in Results/Output_{d1}')

    checker()