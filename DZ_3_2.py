nums = {"one": "один", "two": "два", "three": "три", "four": "четыре",
        "five": "пять", "six": "шесть", "seven": "семь", "eight": "восемь",
        "nine": "девять", "ten": "десять"}


def num_translate_adv(num):
    first_big = num[0]
    if first_big.isupper():
        num = num.lower()
        dig = nums[num]
        print(dig.capitalize())
    elif num.islower():
        dig_2 = nums[num]
        print(dig_2)
    else:
        print(None)


num_translate_adv('two')
