
with open('C:/Users/Андрей/Desktop/code/users.csv', 'r', encoding='utf-8') as f:
    users = f.readlines()
with open('C:/Users/Андрей/Desktop/code/hobby.csv', 'r', encoding='utf-8') as f:
    hobby = f.readlines()


users = [u.strip() for u in users]
hobby = [h.strip() for h in hobby]

if len(users) == len(hobby):
    general_file_1 = {k: v for k, v in zip(users, hobby)}
    with open('Dict_u_h.csv', 'w', encoding='utf-8') as f:
        f.write(str(general_file_1))

elif len(users) > len(hobby):
    for i in range(len(users) - len(hobby)):
        hobby.append(str(None))
    general_file_2 = {k: v for k, v in zip(users, hobby)}
    with open('Dict_u_h.csv', 'w', encoding='utf-8') as f:
        num = f.write(str(general_file_2))
