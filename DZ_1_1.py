duration = int(input('Введите количество секунд - '))

seconds = duration % 60
minutes = (duration - seconds) / 60 % 60
hours = (duration - (minutes * 60) - seconds) / 3600 % 24
days = (duration - seconds - (minutes * 60) - (hours * 3600)) / 3600 / 24

if days > 365:
    print('Срок больше года')
else:
    print(int(days), 'дней', int(hours), 'час.', int(minutes), 'мин.', int(seconds), 'сек.')
