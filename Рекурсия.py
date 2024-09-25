def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        if int(str_number) == 0:
            return 1
        return int(str_number)

result = get_multiplied_digits(420)
print(result)
