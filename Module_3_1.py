import random

calls = 0


def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(input_str):
    count_calls()
    return (len(input_str), input_str.upper(), input_str.lower())


def is_contain(input_str, input_list):
    count_calls()
    for items_ in input_list:
        if input_str.upper() == items_.upper():
            return True
        else:
            continue
    return False


bag_of_words = ["Задача", "Счётчик", "вызовов", "Порой", "необходимо", "отслеживать", "сколько", "раз", "вызывалась",
                "та", "или", "иная", "функция", "сожалению", "Python", "предусмотрен", "подсчёт", "вызовов",
                "автоматически", "Давайте", "реализуем", "данную", "фишку", "самостоятельно"]

for i in range(1, 11):
    input_string = bag_of_words[random.randint(0, len(bag_of_words) - 1)]
    input_list = []
    while len(input_list) < 5:
        tmp_word = bag_of_words[random.randint(0, len(bag_of_words) - 1)]
        if tmp_word not in input_list:
            input_list.append(tmp_word)
    print("Входные параметры: ", input_string, ", ", input_list)
    print("Вывод string_info: ", string_info(input_string))
    print("Вывод is_contain: ", is_contain(input_string, input_list))
    print("Количество вызовов: ", calls)
    print()
