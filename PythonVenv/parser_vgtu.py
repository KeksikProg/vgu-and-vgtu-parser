import requests
from bs4 import BeautifulSoup
import csv
import subprocess

URL = 'https://rating.cchgeu.ru/x/getProcessor'
HEADERS = {
    'Host': 'rating.cchgeu.ru',
    'Origin': 'https://rating.cchgeu.ru',
    'Referer': 'https://rating.cchgeu.ru/',
    'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.75 (Edition Yx GX)'
}
LIST_SPEC_INF = ['{"КонкурснаяГруппа":{"type":"CatalogRef","catalog":"КонкурсныеГруппы",'
                 '"uid":"34b9e9cc-899d-11ec-fb90-36863ec15fb1","name":"ИиВТ_ФИТКБ_2022 (бак, очное, бюджет)"},'
                 '"Сортировка":null,"ОтображатьЗачисленных":false}',

                 '{"КонкурснаяГруппа":{"type":"CatalogRef","catalog":"КонкурсныеГруппы",'
                 '"uid":"f29f8176-8d95-11ec-789f-36863ec15fb1",'
                 '"name":"ИСиТ (ИСиТЦ, ИТвД, САПиРИС)_ФИТКБ_2022 (бак, очное, бюджет)"},'
                 '"Сортировка":{"type":"EnumRef","catalog":"ВидСортировокРейтингаWebБР","name":"ПоРейтингу",'
                 '"title":"По месту в рейтинге"},"ОтображатьЗачисленных":false}',

                 '{"КонкурснаяГруппа":{"type":"CatalogRef","catalog":"КонкурсныеГруппы",'
                 '"uid":"0681da56-90b9-11ec-d781-36863ec15fb1","name":"КБ_ФИТКБ_2022 (спец, очное, бюджет)"},'
                 '"Сортировка":{"type":"EnumRef","catalog":"ВидСортировокРейтингаWebБР","name":"ПоРейтингу",'
                 '"title":"По месту в рейтинге"},"ОтображатьЗачисленных":false}',

                 '{"КонкурснаяГруппа":{"type":"CatalogRef","catalog":"КонкурсныеГруппы",'
                 '"uid":"0593526e-92df-11ec-d781-36863ec15fb1","name":"ИБТС_ФИТКБ_2022 (спец, очное, бюджет)"},'
                 '"Сортировка":{"type":"EnumRef","catalog":"ВидСортировокРейтингаWebБР","name":"ПоРейтингу",'
                 '"title":"По месту в рейтинге"},"ОтображатьЗачисленных":false}',

                 '{"КонкурснаяГруппа":{"type":"CatalogRef","catalog":"КонкурсныеГруппы",'
                 '"uid":"93673ef8-92e3-11ec-d781-36863ec15fb1",'
                 '"name":"ИБАС_ФИТКБ_2022 (спец, очное, бюджет)"},'
                 '"Сортировка":{"type":"EnumRef","catalog":"ВидСортировокРейтингаWebБР",'
                 '"name":"ПоРейтингу","title":"По месту в рейтинге"},"ОтображатьЗачисленных":false}'
                 ]
ID_H = []
FILE = 'ВГТУ_3.csv'

for i in LIST_SPEC_INF:
    DATA = {
        'processor': 'rating_getRating_v2',
        'jsonParams': i
    }

    r = (requests.post(URL, DATA, HEADERS).json())['data']['ТЗ']
    for x in r:
        if x['СуммаБаллов'] > 223:
            ID_H.append(x['ФизическоеЛицоИдентификатор'])


def save_in_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Снилсы'])
        for item in items:
            writer.writerow([item])


save_in_file(ID_H, FILE)
