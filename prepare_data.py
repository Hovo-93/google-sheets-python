# Обработка данных из google_sheets_
def prepare_date(data):
    info_list = []
    for i in data.get('values')[1:]:
        dict_list = {
            'number': i[0],
            'order_id': i[1],
            'coast': i[2],
            'delivery': i[3]
        }
        info_list.append(dict_list)
    print(f' Всего полученно - {len(info_list)}')

    return info_list
