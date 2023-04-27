
import numpy as np
def random_predict(number:int=1, low_limit:int=1, up_limit:int=100) -> int:
    """Ищет число алгоритмом бинарного поиска

    Args:
        number (int, optional): Загаданне число, по умолчанию 1. Defaults to 1.
        low_limit(int, optional): Нижняя граница диапазона поиска. Defaults to 1.
        up_limit(int, optional):  Верхняя граница диапазона поиска. Defaults to 100.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number =  (up_limit + low_limit)//2# предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
        elif predict_number > number:
            up_limit = predict_number-1
        else:
            low_limit = predict_number+1
    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    low_limit = 1
    up_limit = 100
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(low_limit, up_limit+1, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number, low_limit, up_limit))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)