import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://raex-rr.com/education/russian_universities/top-100_universities/2023/"



def save_to_txt(data, filename="universities.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        p = 1
        for number, (name, ball) in enumerate(data, 1):
            file.write(f"Строка номер {number}\n")
            file.write(f"ВУЗ:   {name}\n")
            file.write(f"Баллы поступления:   {ball}\n\n")


def parsing(html_read):
    arr_name_vuz = []
    soup = bs(html_read.text, 'html.parser')
    table_vuz = soup.find("table" , class_="rrp-table")
    rows_vuz = soup.find_all("tr")[1:]


    for row_vuz in rows_vuz:
        try:
            name_vuz = row_vuz.find_all(["th","td"])[1]
            ball_vuz = row_vuz.find_all(["th","td"])[3]

            name = name_vuz.get_text(strip=True)
            ball = ball_vuz.get_text(strip=True)


            arr_name_vuz.append([name , ball])
        except IndexError:
            print(f"Ошибка в строке {rows_vuz}")



    save_to_txt(arr_name_vuz)




def main():
    html_read = requests.get(URL_TEMPLATE)

    if html_read.status_code == 200:
        parsing(html_read)
    else:
        print("Ошибка подключения")




if __name__ == "__main__":
    main()
