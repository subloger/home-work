import re


def email_parse(email_addres):
    add = email_addres
    parse_expression = re.compile(r'^(\w+)+(\b[@])+(\b\w+[.]+\w+)')
    list_of_pars = re.findall(parse_expression, email_addres)
    try:
        if '.' and '@' in add:
            dict_of_pars = {'username': list_of_pars[0][0], 'domain': list_of_pars[0][2]}
            return print(dict_of_pars)
    except IndexError:
        return print('Неправильный адрес!')


email_parse('someone@geekbrains.ru')
