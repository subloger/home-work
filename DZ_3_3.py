def thesaurus(*args):
    names = {}
    for i in sorted(args):
        key = i[0]
        if key in names:
            names[key] += [i]
        else:
            names[key] = [i]
    return names

print(thesaurus('Иван', 'Петр', 'Илья', 'Мария'))

