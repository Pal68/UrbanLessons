import random as rnd

code_numbers = range(1, 21)


def get_password(key_):
    result = ""
    for i in range(0, len(code_numbers)):
        for j in range(i + 1, len(code_numbers)):
            if key_ % (code_numbers[i] + code_numbers[j]) == 0:
                result = result + str(code_numbers[i]) + str(code_numbers[j])
    return result


for i in range(3, 21):
    print("Пароль для цифры ", i, " - ", get_password(i))

random_number = rnd.randint(3, 20)
print()
print("Пароль для цифры ", random_number, " - ", get_password(random_number))
