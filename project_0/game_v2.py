""""Игра угадай число
компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) #предполагаемое число
        if number == predict_number:
            break #выход из цикла если угадали
    return (count)


def score_game(random_predict) ->int:
    """За какое количество попыток в среднем за 1000 подходов угадывает компьютер

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] #список для сохранения количества попыток
    np.random.seed(1) #фиксируем random seed, чтоб наш эксперимент был воспроизводим
    random_array = np.random.randint(1, 101, size=(1000)) #загадали список чисел 
   
    for number in random_array:
        count_ls.append(random_predict(number)) #заносим в этот список попытки на каждом запуске функции, в аргументы вставляем предыдущую функция которая вернула кол-во попыток count
    
    score = int(np.mean(count_ls)) #Находим среднее количество попыток np.mean
    print(f'Ваш алгоритм угадывает в среднем число за: {score} попыток')
    return score

if __name__ == "__main__": #сделали чтобы импортировать эту библиотеку в будущем например в юпитер нотбук 
    #RUN
    score_game(random_predict)
