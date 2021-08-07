import requests

logs = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
content = logs.content.decode()

with open('Logs.txt', 'w', encoding='utf-8') as f:
    f.write(f'{content}')

with open('Logs.txt', 'r', encoding='utf-8') as f:
    read = f.readlines()
    result = []
    for line in read:
        num_1 = line.find(' ')
        num_2 = line.find('GET')
        num_3 = line.find('/d')
        num_4 = line.find(' HTTP')
        value = (line[:num_1], line[num_2:num_3-1], line[num_3:num_4])
        result.append(value)

for i in range(len(result)):
    print(result[i])


