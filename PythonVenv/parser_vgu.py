from bs4 import BeautifulSoup
import csv

FILE = 'ВГУ.csv'


def get_content():
    ID_H = []
    for i in range(1, 11):
        HTML = open(f'C:/Users/Maksim/Desktop/PythonQuick/PythonVenv/html/p{i}.html', 'r', encoding='utf-8')

        soup = BeautifulSoup(HTML, 'html.parser')
        items = soup.find_all('tr')

        for item in items:
            if item.find('td', class_='ajr_smplrat_result_col8').get_text() == '':
                continue
            if int(item.find('td', class_='ajr_smplrat_result_col8').get_text()) > 223:
                ID_H.append(item.find('nobr').get_text())
    return ID_H


def save_in_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Снилсы'])
        for item in items:
            writer.writerow([item])


save_in_file(get_content(), FILE)
