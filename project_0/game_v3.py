import numpy as np
def random_predict(number: int=1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        число попыток за которое угадывается число
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) #предполагаемое число
        if number == predict_number:
            break #выход из цикла если угадали
    return count


def game_core_v2 (number: int=1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict +=1
        elif number < predict:
            predict -=1
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): предыдущая функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000)) #загадали список из 10000 чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    return score
    print (f"Ваш алгоритм угадывает число в среднем за: {score} попыток")

#Run benchmarking to score effectiveness of all algorithms
print('Run benchmarking for random_predict: ', end='')
print(score_game(random_predict))

print('Run benchmarking for game_core_v2: ', end='')
print(score_game(game_core_v2))

def game_core_v3(number:int = 1) ->int:
    """Версия игры где мы попытаемся сделать среднее число попыток угадать число менее 20

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    predict_num_ls = [] #создаем пустой список куда вставим 10 чисел используя рандом от 1 до 100
    for i in range(10):
        predict_num_ls.append(np.random.randint(1, 101)) #наполняем цифрами список
    predict_num_ls.sort() #сортируем, для корректной работы бинарного поиска (так указано в инструкции)
    print(predict_num_ls)
    left_num = 0 #создаем левую границу списка
    right_num = len(predict_num_ls) - 1 #создаем правую границу списка
    mid = (left_num + right_num) // 2 #ищем середину списка
    current_num = int(input('Введите угадываемое число: ')) #вводим число которое будет угадывать есть ли оно в списке
    count = 0 
    while predict_num_ls[mid] != current_num: #создаем цикл, который будет выполняться до тех пор, пока середина (mid) в этом списке не совпадет с угадываемым числом
        count += 1
        if current_num > predict_num_ls[mid]: # если угадываемое число больше того, что в списке, мы переносим левую границу, чтобы убрать из левой границы поиск числа и таким образом уменьшить количество итераций
            left_num = mid + 1
        else:
            right_num = mid - 1 # иначе же если угадываемое число меньше того, что в списке, переносим правую границу на 1 меньше сережины.
        mid = (left_num + right_num) // 2
        if left_num > right_num: #чтобы цикл не был бесконечным, ставим break если левая и правая граница пересекуться, ведь это значит что в списке не оказалось угадываемого числа. 
            print('Искомого числа нет в списке')
            break
    print(f'количество попыток: {count}') #выводим количество попыток
    return count
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
