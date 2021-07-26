nums = {"one": "один", "two": "два", "three": "три", "four": "четыре",
        "five": "пять", "six": "шесть", "seven": "семь", "eight": "восемь",
        "nine": "девять", "ten": "десять"}


def num_translate(num):
    if num in nums:
        dig = nums[num]
        print(dig)
    else:
        print(None)

num_translate('two')