#В переменную elem_5_3 сохраните элемент из 5 строки и 3 столбца

#В переменную last сохраните элемент из последней строки последнего столбца

#В переменную line_4 сохраните строку 4

#В переменную col_2 сохраните предпоследний столбец

#Из строк 2-4 (включительно) получите столбцы 3-5 (включительно). Результат сохраните в переменную part

#Сохраните в переменную rev последний столбец в обратном порядке

#Сохраните в переменную trans транспонированный массив

import numpy as np
mystery = np.array([[-13586,  15203,  28445, -27117,  -1781, -17182, -18049],
       [ 25936, -30968,  -1297,  -4593,   6451,  15790,   7181],
       [ 13348,  28049,  28655,  -6012,  21762,  25397,   8225],
       [ 13240,   7994,  32592,  20149,  13754,  11795,   -564],
       [-21725,  -8681,  30305,  22260, -17918,  12578,  29943],
       [-16841, -25392, -17278,  11740,   5916,    -47, -32037]],
      dtype=np.int16)

elem_5_3 = mystery[5,3]
last = mystery[-1,-1]
line_4 = mystery[4]
col_2 = mystery[:, -2]
part = mystery[2:5, 3:6]
rev = mystery[::-1,-1]
trans = mystery.transpose()
from collections import *
#print(mystery[::-1,-1])

#Получите булевый массив nans_index с информацией о np.nan в массиве mystery: True - значение пропущено, False - значение не пропущено

#В переменную `n_nan сохраните число пропущенных значений

#Скопируйте массив mystery в массив mystery_new. Заполните пропущенные значения в массиве mystery_new нулями

#Поменяйте тип данных в массиве mystery на int32 и сохраните в переменную mystery_int

#Отсортируйте значения в массиве по возрастанию и сохраните результат в переменную array

#Сохраните в массив table двухмерный массив, полученный из массива array. В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть по столбцам!
mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)

nans_index = np.isnan(mystery)
n_nan = Counter(nans_index)[True]
# создали список из булевых значений после перевили в счетчик Counter после вызвали по ключу True число Tue == 3
mystery_new = mystery
mystery_new[nans_index] = 0  
mystery_int = np.int32(mystery)
array = mystery
array.sort()
table = array.reshape((5, 3), order='F')
col = table[:,1]
print(mystery_new)
