from requests import get, utils


def currency_rates(code_of_currency):

    ins = get('http://www.cbr.ru/scripts/XML_daily.asp')
    dec = utils.get_encoding_from_headers(ins.headers)
    result = ins.content.decode(encoding=dec)
    code_of_currency = code_of_currency.upper()                               # приведение к нужному регистру

    if code_of_currency in result:                                            # проверка кода валюты
        num = result.find(code_of_currency)
        num_2 = result.find('Value', num, )
        value = result[num_2 + 6: num_2 + 11]
        value = value.replace(',', '.')                                       # преобразование к числу (float)
        value = float(value)
        str_for_work = result[num: num_2 + 6]
        str_for_work = str_for_work.replace('</CharCode><Nominal>', ':  ')    # вывод сопутствующей информации
        str_for_work = str_for_work.replace('</Nominal><Name>', ' ')
        str_for_work = str_for_work.replace('</Name><Value>', ' = ')
        return f'{str_for_work} {value} "руб."'
    else:
        return None


print(currency_rates('Usd'))
print(currency_rates('EUR'))
print(currency_rates('CzK'))