"""Игра "угадай число"
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    minimum = 1
    maximum = 101
    while True:
        count += 1
        predict_number = np.random.randint(minimum, maximum)  # предполагаемое число
        
        if number > predict_number: # Если число, выбранное компьютером изначально, больше указанного
            minimum = predict_number # То это указанное число снавоится нижней границей рандомного подбора
            
        elif number < predict_number: # Аналогично поступаем, если загаданное чсило меньше указанного
            maximum = predict_number # После этого указанное число становится черхней планкой
            
        else:
            break # В единственном оставшемся случае - когда числа совпадают, происходит выход из цикла
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == "__main__":
    score_game(random_predict)