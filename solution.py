import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from statsmodels.stats.weightstats import ztest

# Задаем уровень значимости
alpha = 0.03

chat_id = 5072617748 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    z_stat, p_val = ztest(x, y, equal_var=False)
    if p_val < alpha:
        return True
    else:
        return False
