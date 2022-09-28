import numpy as np
import matplotlib.pyplot as plt

# Расчёт напряжения коллектор-эмиттер (минимальная граница)
def Uke_min_(d_Ut, d_Unel, Un):
    return (d_Ut + d_Unel + Un)

# Расчёт напряжения питания (минимальная граница)
def Ep_min_(Uke, d_Ut, Un, k):
    return (Uke + d_Ut + Un + k * Un)

# Расчёт напряжения коллектор-эмиттер (рабочее значение)
def EkeA_(U, k):
    if k > 0 and k < 1:
        return (k * U)
    else:
        print("Error: k имеет недопустимое значение")
        return None

# Расчёт тока коллектора
def Ik_(In, k):
    return k * (In)

# Расчёт тока эмиттера
def Ie_(Ib, Ik):
    return (Ib + Ik)

# Расчёт сопротивления по постоянному току
def R_post_(Ep, UkeA, IkA):
    return ((Ep - UkeA) / IkA)

# Расчёт напряжения по переменному току
def Em_min_(d_Ut, Un, UkeA):
    return (d_Ut + Un + UkeA)

# Расчёт сопротивления по переменному току
def R_per_(Em, UkeA, IkA):
    return ((Em - UkeA) / IkA)

# Расчёт сопротивления коллектора
def R_k_(R_per, Rn):
    return ((Rn * R_per) / (Rn - R_per))

# Расчёт сопротивления базы (R1)
def R1_(Ep, Ie, Re, Ube, Rb, Ib):
    return (Ep / (((Ie * Re + Ube) / Rb) + Ib))

# Расчёт сопротивления базы (R2)
def R2_(Rb, R1):
    return (Rb * R1) / (R1 - Rb + 0.001)

# Расчёт входного сопротивления
def Rvh(h11, h21, Re_arr, Rb_arr):
    return (((h11 + ((h21 + 1) * Re_arr)) * Rb_arr) / ((h11 + ((h21 + 1) * Re_arr)) + Rb_arr))

# Округление до номинального ряда напряжения питания
def to_E_rad(U):
    E_24 = [6, 7.5, 9, 10, 12, 15, 18, 20]
    index = 0
    min_dif = E_24[len(E_24) - 1] - E_24[0]
    for i in range(len(E_24)):
        if abs(E_24[i] - U) < min_dif:
            index = i
            min_dif = abs(E_24[i] - U)
    return E_24[index]

# округление величины сопротивления до номинального ряда
def to_E24_(R):
    E_24 = [100, 110, 120, 130, 150, 160, 180, 200,
            220, 240, 270, 300, 330, 360, 390, 430,
            470, 510, 560, 620, 680, 750, 820, 910,
            1000, 1100, 1200, 1300, 1500, 1600, 1800,
            2000, 2200, 2400, 2700, 3000, 3300, 3600,
            3900, 4300, 4700, 5100, 5600, 6200, 6800,
            7500, 8200, 9100, 10000, 11000, 12000, 13000,
            15000, 16000, 18000, ]
    index = 0
    for i in range(R.shape[0]):

        try:
            for j in range(R.shape[1]):

                try:
                    for k in range(R.shape[2]):
                        # ___________________________________________#
                        min_dif = E_24[len(E_24) - 1]
                        for v in range(len(E_24)):
                            if abs(E_24[v] - R[i][j][k]) < min_dif:
                                index = v
                                min_dif = abs(E_24[v] - R[i][j][k])
                        R[i][j][k] = E_24[index]

                except:
                    print('массив двумерный')
                    min_dif = E_24[len(E_24) - 1]
                    for v in range(len(E_24)):
                        if abs(E_24[v] - R[i][j]) < min_dif:
                            index = v
                            min_dif = abs(E_24[v] - R[i][j])
                    R[i][j] = E_24[index]

        except:
            print('массив одномерный')
            min_dif = E_24[len(E_24) - 1]
            for v in range(len(E_24)):
                if abs(E_24[v] - R[i]) < min_dif:
                    index = v
                    min_dif = abs(E_24[v] - R[i])
            R[i] = E_24[index]
    return R

# Округление сопротивления
def to_E25_(R):
    E25 = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900,
           1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000,
           9000, 10000, 15, 150, 250, 350, 450, 550,
           650, 750, 850, 950, 1500, 2500, 3500,
           4500, 5500, 6500, 7500, 8500, 9500, 15000]
    index = 0
    for i in range(R.shape[0]):
        try:
            for j in range(R.shape[1]):
                try:
                    for k in range(R.shape[2]):
                        # ___________________________________________#
                        min_dif = E25[len(E25) - 1]
                        for v in range(len(E25)):
                            if abs(E25[v] - R[i][j][k]) < min_dif:
                                index = v
                                min_dif = abs(E25[v] - R[i][j][k])
                        R[i][j][k] = E25[index]
                except:
                    print('двумерный массив')
                    min_dif = E25[len(E25) - 1]
                    for v in range(len(E25)):
                        if abs(E25[v] - R[i][j]) < min_dif:
                            index = v
                            min_dif = abs(E25[v] - R[i][j])
                    R[i][j] = E25[index]
        except:
            print('одномерный массив')
            min_dif = E25[len(E25) - 1]
            for v in range(len(E25)):
                if abs(E25[v] - R[i]) < min_dif:
                    index = v
                    min_dif = abs(E25[v] - R[i])
            R[i] = E25[index]
    return R

# Функция нормализации данных в матрице
def softmax(matrix):
    mean = np.mean(matrix)
    print("Среднее:", mean)
    matrix = matrix - mean
    disp = np.sqrt(np.sum(matrix ** 2))
    print("Дисперсия:", disp)
    if disp > 0:
        x = 1 / disp
    else:
        print("Матрица состоит только из нулей!")
        return None
    matrix = matrix * x
    disp = np.sqrt(np.sum(matrix ** 2))
    print("Дисперсия:", disp)
    m = abs(np.min(matrix))
    return (matrix + m)

# Функция ввода пользователя данных его рабочей точки
def _input_(Ep, Uke, Ik):
    E = float(input('Введите Eпит:'))
    U = float(input('Введите Uкэ А:'))
    I = float(input('Введите Iк А:'))
    index_i = 0
    index_j = 0
    index_k = 0

    min_dif = Ep[len(Ep) - 1]
    for i in range(len(Ep)):
        if abs(Ep[i] - E) < min_dif:
            index_i = i
            min_dif = abs(Ep[i] - E)

    min_dif = Uke[index_i][len(Uke[index_i]) - 1]
    for i in range(len(Uke[index_i])):
        if abs(Uke[index_i][i] - U) < min_dif:
            index_j = i
            min_dif = abs(Uke[index_i][i] - U)

    min_dif = Ik[len(Ik) - 1]
    for i in range(len(Ik)):
        if abs(Ik[i] - I) < min_dif:
            index_k = i
            min_dif = abs(Ik[i] - I)
    print(
        f"Значения округлённые до расчитанных:\nEp = {Ep[index_i]}В\nUkeA = {Uke[index_i][index_j]}В\nIkA = {Ik[index_k]}А")
    return index_i, index_j, index_k

# Функция обновления статус бара
def status_bar(procents, full):
    if (procents != full):
        print(f"{' ' * 60}Status of the process: [|{'=' * procents}>{' ' * (full - procents)}|]")
    else:
        print(f"{' ' * 60}Status of the process: [|{'=' * procents}={' ' * (full - procents)}|]")
        print('Success!')
    return procents + 1

# Расчёт коэффициента усиления
def Ke0(Rn, Rk, Rg, Rb, h11, betta, x, flag=False):
    E_out = Rn / (Rn + Rk)
    if (flag):
        print("Е вых:", E_out)
    Ku_xx = (-betta) * (Rk / (h11 + (betta + 1) * x))
    if (flag):
        print("Кu хх:", Ku_xx)
    R_in = (Rb * h11 + x * Rb * (betta + 1)) / (Rb + h11 + x * (betta + 1))
    if (flag):
        print("R вх:", R_in)
    E_in = (R_in) / (R_in + Rg)
    if (flag):
        print("Е вх:", E_in)
    return Ku_xx * E_in * E_out, R_in

# ===================================================================================
# ===================================================================================
# ===================================================================================
# ===================================================================================

def start_calculate(dict_values):
    print("Start okey")
    Un = float(dict_values['Напряжение нагрузки'])                       # Напряжение нагрузки
    Rn = float(dict_values['Сопротивление нагрузки'])                    # Сопротивление нагрузки
    In = float(dict_values['Ток нагрузки'])/1000                         # Ток нагрузки
    Rg = float(dict_values['Сопротивление генератора'])                  # Сопротивление генератора
    K0 = float(dict_values['Коэффициент усиления'])                      # Коэффициент усиления
    Emax = float(dict_values['E максимально допустимое'])                  # E максимально допустимое
    dT = float(dict_values['Максимальное отклонение темпиратуры'])       # Максимальное отклонение темпиратуры
    fn = float(dict_values['Нижняя граничная частота'])                  # Нижняя граничная частота
    C_e_per = float(dict_values['Ёмкость эмиттерного перехода'])/(10**(-12))  # Ёмкость эмиттерного перехода
    C_k_per = float(dict_values['Ёмкость коллекторного перехода'])/(10**(-12))# Ёмкость коллекторного перехода
    Cn = float(dict_values['Ёмкость нагрузки'])/(10**(-9))               # Ёмкость нагрузки
    f_T = float(dict_values['Частота единичного усиления'])*(10**6)       # Частота единичного усиления

    # Параметры

    d_Unel = float(dict_values['Дельта U нелинейное'])           # Дельта U нелинейное
    d_Ut = float(dict_values['Дельта U тепловое'])             # Дельта U тепловое
    Ik0 = float(dict_values['Тепловой ток коллектора'])/1000  # Тепловой ток коллектора
    e = float(dict_values['Температурный коэффициент'])     # Температурный коэффициент

    # Расчитываемые в п.2 параметры транзистора

    betta = float(dict_values['Коэффициент усиления по току'])  # Усиление по току (получить из малосигнальных параметров)
    Ube = float(dict_values['Напряжение база-эмиттер'])       # Напряжение база-эмиттер (получить из малосигнальных параметров)
    h11 = float(dict_values['Входное сопротивление транзистора (h11)'])
    dB = max([abs(120 - betta), abs(40 - betta)])            # Максимальное отклонение усиления по току

    # Гиперпараметры для программы
    z = 1  # Запас по напряжению по переменному току (не рекомендуется брать больше 2 и оставлять 0)
    resolution = 64  # разрешение выходной карты
    full = 8
    procents = 1

    #'                   Определение возможных напряжений питиния                   '
    # Массив с возможными для данного транзистора напряжениями питания

    Ep_arr = []
    if float(dict_values['E максимально допустимое']) != 0:
        Ep_arr = [float(dict_values['E максимально допустимое'])]
        print('Напряжение питания',Ep_arr)
    else:
        for i in range(1, 10):
            # Нижняя граница напряжения на коллектор-эммитер
            Uke = Uke_min_(d_Ut, d_Unel, Un)
            Ep = Ep_min_(Uke, d_Ut, Un, i)
            Ep = to_E_rad(Ep)
            if Ep <= Emax and Ep > 9:
                if Ep not in Ep_arr:
                    Ep_arr.append(Ep)
        print("Напряжения питания:", np.array(Ep_arr).shape)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '      Определение возможных напряжений коллектор-эмиттер в рабочей точке       '
    UA_arr = []
    if float(dict_values['Напряжение коллектор-эмиттер']) != 0:
        UA_arr = [float(dict_values['Напряжение коллектор-эмиттер'])]
        print('Напряжение кол-эмит',UA_arr)
    else:
        # Напряжения в рабочей точке для разных E пит.
        x = np.linspace(0.4, 0.7, resolution)
        for j in Ep_arr:
            UA_arr_part = []
            for i in x:
                UA_arr_part.append(round(EkeA_(j, i), 2))
            UA_arr.append(UA_arr_part)  # Объединение частей массива в общий массив
        print("Напряжение UкА:", np.array(UA_arr).shape)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '            Определение возможных токов коллектора в рабочей точке             '
    Ik_arr = []
    # Токи коллектора IкА:
    try:
        if float(dict_values['Ток коллектора']) != 0:
            Ik_arr = [float(dict_values['Ток коллектора'])/1000]
        else:
            x = np.linspace(2, 5, resolution)
            for i in x:
                Ik_arr.append(round(Ik_(In, i) + Ik0, 5))
    except:
        x = np.linspace(2, 5, resolution)
        for i in x:
            Ik_arr.append(round(Ik_(In, i) + Ik0, 5))
    Ik_arr = np.array(Ik_arr)


    Ib_arr = []
    # Токи базы IбА:
    try:
        if float(dict_values['Ток базы']) != 0:
            Ib_arr = [float(dict_values['Ток базы'])/(10**(-6))]
            print('Ток базы',Ib_arr)
        else:
            for i in Ik_arr:
                Ib_arr.append(round(i / betta, 9))
    except:
        for i in Ik_arr:
            Ib_arr.append(round(i / betta, 9))
    Ib_arr = np.array(Ib_arr)


    Ie_arr = []
    # Токи эмиттера IэА:
    try:
        if float(dict_values['Ток эммитера']) != 0:
            Ie_arr = [float(dict_values['Ток эммитера'])/1000]
            print('Ток эммитера',Ie_arr)
        else:
            Ie_arr = Ie_(Ib_arr, Ik_arr)
    except:
        Ie_arr = Ie_(Ib_arr, Ik_arr)
    Ie_arr = np.array(Ie_arr)

    if Ik_arr.shape[0] != 1:
        print("Ток коллектора:", Ik_arr.shape)
    else:
        print("Ток коллектора:", Ik_arr)

    if Ib_arr.shape[0] != 1:
        print("Ток базы:      ", Ib_arr.shape)
    else:
        print("Ток базы:      ", Ib_arr)

    if Ib_arr.shape[0] != 1:
        print("Ток эмиттера:  ", Ie_arr.shape)
    else:
        print("Ток эмиттера:  ", Ie_arr)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '        Определение матрицы возможных сопротивлений по постоянному току        '

    # Сопротивления по постоянному току
    try:
        R_post_arr = []
        for i in range(len(Ep_arr)):
            E = []
            for j in UA_arr[i]:
                U = []
                for k in Ik_arr:
                    U.append(round(R_post_(Ep_arr[i], j, k), 3))
                E.append(U)
            R_post_arr.append(E)
        R_post_arr = np.array(R_post_arr)
        print("Сопротивления по пост. току:", R_post_arr.shape)
    except:
        R_post_arr = np.array([round(R_post_(Ep_arr[0], UA_arr[0], Ik_arr[0]), 3)])
        print("Сопротивления по пост. току:", R_post_arr)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '                          Определение возможных Em                             '

    # Напряжение по переменному току
    Em_arr = []
    try:
        for i in range(len(Ep_arr)):
            Em_part = []
            # Отступ от минимального
            for k in UA_arr[i]:
                Em_part.append(round(Em_min_(d_Ut, Un, k) + z, 2))
            Em_arr.append(Em_part)
        print("Напряжение по пер. току:", np.array(Em_arr).shape)
    except:
        Em_arr = np.array([round(Em_min_(d_Ut, Un, UA_arr[0]) + z, 2)])
        print("Напряжение по пер. току:", Em_arr)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '                Определение возможных сопротивлений цепи ОЭ                    '
    # Расчёт сопротивлений по переменному току
    threshold = 0
    R_per_arr = []
    try:
        for i in range(len(Ep_arr)):
            E = []
            for j1, j2 in zip(Em_arr[i], UA_arr[i]):
                U = []
                for k in Ik_arr:
                    U.append(R_per_(j1, j2, k))
                E.append(U)
            R_per_arr.append(E)

        R_per_arr = np.array(R_per_arr)
        print("Сопротивления по переменному току:\n", R_per_arr.shape)
    except:
        R_per_arr = np.array([R_per_(Em_arr[0], UA_arr[0], Ik_arr[0])])
        print("Сопротивления по переменному току:\n", R_per_arr)

    # Расчёт сопротивлений коллектора
    R_k_arr = R_k_(R_per_arr, Rn)
    if R_k_arr.shape[0] != 1:
        print("Сопротивления коллектора:\n", R_k_arr.shape)
    else:
        print("Сопротивления коллектора:\n", R_k_arr)
    # Округление Rк до ряда
    R_k_arr = to_E24_(R_k_arr)
    if R_k_arr.shape[0] != 1:
        print("Сопротивления коллектора:\n", R_k_arr.shape)
    else:
        print("Сопротивления коллектора:\n", R_k_arr)


    # Расчёт сопротивлений эмиттера
    R_e_arr = R_post_arr - R_k_arr
    if R_e_arr.shape[0] != 1:
        print("Сопротивления эмиттера:\n", R_e_arr.shape)
    else:
        print("Сопротивления эмиттера:\n", R_e_arr)

    # Расчёт сопротивлений базы
    Rb_arr = []
    Rb_arr_E25 = []
    d_I_dop = d_Ut / R_post_arr
    for i in range(len(Ib_arr)):
        Rb_arr.append(((betta * ((d_I_dop.T[i]) * (R_e_arr.T[i]) - (e * dT))) / ((Ib_arr[i] * dB) - (d_I_dop.T[i]))) - R_e_arr.T[i] - threshold)
    Rb_arr = np.array(Rb_arr).T
    Rb_arr_E25 = np.array(Rb_arr)

    if Rb_arr.shape[0] != 1:
        print("Сопротивления базы:\n", Rb_arr.shape)
    else:
        print("Сопротивления базы:\n", Rb_arr)


    # Округление Rб до ряда
    Rb_arr_E25 = to_E25_(Rb_arr_E25)

    # Расчёт сопротивлений базы R1
    R1_arr = []
    for i in range(len(Ep_arr)):
        R1_arr.append(R1_(Ep_arr[i], Ie_arr, R_e_arr[i], Ube, Rb_arr_E25[i],
                          Ib_arr))  # Eпит,Iэ,Rэ,Uбэ,Rб,Iб

    R1_arr = np.array(R1_arr)
    R1_arr = to_E24_(R1_arr)  # Округление R1 до ряда
    if R1_arr.shape[0] != 1:
        print("Сопротивления R1:\n", R1_arr.shape)
    else:
        print("Сопротивления R1:\n", R1_arr)


    # Расчёт сопротивлений базы R2
    R2_arr = R2_(Rb_arr_E25, R1_arr)
    R2_arr = to_E24_(R2_arr)  # Округление R2 до ряда
    if R2_arr.shape[0] != 1:
        print("Сопротивления R2:\n", R2_arr.shape)
    else:
        print("Сопротивления R2:\n", R2_arr)

    # Расчёт сопротивлений базы
    Rb_arr_E25 = (R1_arr * R2_arr) / (R1_arr + R2_arr)
    if Rb_arr_E25.shape[0] != 1:
        print("Сопротивлений базы 2:\n", Rb_arr_E25.shape)
    else:
        print("Сопротивлений базы 2:\n", Rb_arr_E25)

    procents = status_bar(procents, full)

    # ===============================================================================#
    '                         Определение возможных Eсм                             '

    Ecm = []
    for i in range(len(Ep_arr)):
        Ecm.append((Ep_arr[i] * R2_arr[i]) / (R1_arr[i] + R2_arr[i]))
    Ecm = np.array(Ecm)
    # print(Ecm.shape)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '                      Определяем возможный разброс тока                        '

    # коэффициент перераспределения тока базы
    y = R_e_arr / (R_e_arr + Rb_arr_E25 + 0.001)
    dIt = (e * dT * betta) / (Rb_arr_E25 + (R_e_arr * (1 + betta)))
    dIB = dB * Ik_arr / (betta * (1 + betta * y))
    dI = (dIt + dIB)

    dUt_2_orig = dI * R_post_arr

    Up_orig = (Ik_arr * R_per_arr) - dUt_2_orig
    mask_1 = np.array([Up_orig > 0][0], dtype='int32')
    Up = abs(Up_orig - Un)

    mask_2 = np.array([Up < Un * 0.9][0], dtype='int32')
    mask_V = mask_1 * mask_2

    mask_1 = np.array([dUt_2_orig > 0][0], dtype='int32')
    dUt_2 = abs(dUt_2_orig - d_Ut)
    mask_2 = np.array([dUt_2 < d_Ut * 0.9][0], dtype='int32')
    mask_U = mask_1 * mask_2
    procents = status_bar(procents, full)

def start_calculate(dict_values):
    Un = float(dict_values['Напряжение нагрузки'])  # Напряжение нагрузки
    Rn = float(dict_values['Сопротивление нагрузки'])  # Сопротивление нагрузки
    In = float(dict_values['Ток нагрузки'])/1000  # Ток нагрузки
    Rg = float(dict_values['Сопротивление генератора'])  # Сопротивление генератора
    K0 = float(dict_values['Коэффициент усиления'])  # Коэффициент усиления
    Emax = float(dict_values['E максимально допустимое'])  # E максимально допустимое
    dT = float(dict_values['Максимальное отклонение темпиратуры'])  # Максимальное отклонение темпиратуры
    fn = float(dict_values['Нижняя граничная частота'])  # Нижняя граничная частота
    C_e_per = float(dict_values['Ёмкость эмиттерного перехода'])/(10**(-12))  # Ёмкость эмиттерного перехода
    C_k_per = float(dict_values['Ёмкость коллекторного перехода'])/(10**(-12))  # Ёмкость коллекторного перехода
    Cn = float(dict_values['Ёмкость нагрузки'])/(10**(-9))  # Ёмкость нагрузки
    f_T = float(dict_values['Частота единичного усиления'])*(10**6)  # Частота единичного усиления

    # Параметры

    d_Unel = float(dict_values['Дельта U нелинейное'])  # Дельта U нелинейное
    d_Ut = float(dict_values['Дельта U тепловое'])  # Дельта U тепловое
    Ik0 = float(dict_values['Тепловой ток коллектора'])/1000  # Тепловой ток коллектора
    e = float(dict_values['Температурный коэффициент'])  # Температурный коэффициент

    # Расчитываемые в п.2 параметры транщистора

    betta = float(dict_values['Коэффициент усиления по току'])  # Усиление по току (получить из малосигнальных параметров)
    Ube = float(dict_values['Напряжение база-эмиттер'])  # Напряжение база-эмиттер (получить из малосигнальных параметров)
    h11 = float(dict_values['Входное сопротивление транзистора (h11)'])
    dB = max([abs(120 - betta), abs(40 - betta)])  # Максимальное отклонение усиления по току

    # Гиперпараметры для программы
    z = 1  # Запас по напряжению по переменному току (не рекомендуется брать больше 2 и оставлять 0)
    resolution = 64  # разрешение выходной карты
    full = 8
    procents = 1
    '                   Определение возможных напряжений питиния                   '
    # Массив с возможными для данного транзистора напряжениями питания
    Ep_arr = []
    for i in range(1, 10):
        # Нижняя граница напряжения на коллектор-эммитер
        Uke = Uke_min_(d_Ut, d_Unel, Un)
        Ep = Ep_min_(Uke, d_Ut, Un, i)
        Ep = to_E_rad(Ep)
        if Ep <= Emax and Ep > 9:
            if Ep not in Ep_arr:
                Ep_arr.append(Ep)
    print("Напряжения питания:", np.array(Ep_arr).shape)
    Ep_arr = np.array(Ep_arr)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '      Определение возможных напряжений коллектор-эмиттер в рабочей точке       '

    # Напряжения в рабочей точке для разных E пит.
    UA_arr = []
    x = np.linspace(0.4, 0.7, resolution)
    for j in Ep_arr:
        UA_arr_part = []
        for i in x:
            UA_arr_part.append(round(EkeA_(j, i), 2))
        UA_arr.append(UA_arr_part)  # Объединение частей массива в общий массив
    UA_arr = np.array(UA_arr)
    print("Напряжение UкА:", UA_arr.shape)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '            Определение возможных токов коллектора в рабочей точке             '

    # Токи коллектора IкА:
    Ik_arr = []
    # Токи базы IбА:
    Ib_arr = []

    x = np.linspace(2, 5, resolution)
    for i in x:
        Ik_arr.append(round(Ik_(In, i) + Ik0, 5))
    Ik_arr = np.array(Ik_arr)

    for i in Ik_arr:
        Ib_arr.append(round(i / betta, 9))
    Ib_arr = np.array(Ib_arr)

    # Токи эмиттера IэА:
    Ie_arr = Ie_(Ib_arr, Ik_arr)
    print("Ток коллектора:", Ik_arr.shape)
    print("Ток базы:      ", Ib_arr.shape)
    print("Ток эмиттера:  ", Ie_arr.shape)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '        Определение матрицы возможных сопротивлений по постоянному току        '

    # Сопротивления по постоянному току
    R_post_arr = []
    for i in range(len(Ep_arr)):
        E = []
        for j in UA_arr[i]:
            U = []
            for k in Ik_arr:
                U.append(round(R_post_(Ep_arr[i], j, k), 3))
            E.append(U)
        R_post_arr.append(E)
    R_post_arr = np.array(R_post_arr)
    print("Сопротивления по пост. току:", R_post_arr.shape)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '                          Определение возможных Em                             '

    # Напряжение по переменному току
    Em_arr = []
    for i in range(len(Ep_arr)):
        Em_part = []
        # Отступ от минимального
        for k in UA_arr[i]:
            Em_part.append(round(Em_min_(d_Ut, Un, k) + z, 2))
        Em_arr.append(Em_part)
    Em_arr = np.array(Em_arr)
    print("Напряжение по пер. току:", Em_arr.shape)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '                Определение возможных сопротивлений цепи ОЭ                    '
    threshold = 0
    # Расчёт сопротивлений по переменному току
    R_per_arr = []
    for i in range(len(Ep_arr)):
        E = []
        for j1, j2 in zip(Em_arr[i], UA_arr[i]):
            U = []
            for k in Ik_arr:
                U.append(R_per_(j1, j2, k))
            E.append(U)
        R_per_arr.append(E)

    R_per_arr = np.array(R_per_arr)
    print("Сопротивления по переменному току:\n", R_per_arr.shape)

    # Расчёт сопротивлений коллектора
    R_k_arr = R_k_(R_per_arr, Rn)

    # Округление Rк до ряда
    R_k_arr = to_E24_(R_k_arr)
    print("Сопротивления коллектора:\n", R_k_arr.shape)

    # Расчёт сопротивлений эмиттера
    R_e_arr = R_post_arr - R_k_arr
    print("Сопротивления эмиттера:\n", R_e_arr.shape)

    # Расчёт сопротивлений базы
    Rb_arr = []
    d_I_dop = d_Ut / R_post_arr
    for i in range(len(Ib_arr)):
        Rb_arr.append(((betta * ((d_I_dop.T[i]) * (R_e_arr.T[i]) - (e * dT))) / ((Ib_arr[i] * dB) - (d_I_dop.T[i]))) - R_e_arr.T[i] - threshold)
    Rb_arr = np.array(Rb_arr).T
    Rb_arr_E25 = np.array(Rb_arr)

    # Округление Rб до ряда
    Rb_arr_E25 = to_E25_(Rb_arr_E25)
    print("Сопротивления базы:\n", Rb_arr.shape)

    # Расчёт сопротивлений базы R1
    R1_arr = []
    for i in range(len(Ep_arr)):
        R1_arr.append(R1_(Ep_arr[i], Ie_arr, R_e_arr[i], Ube, Rb_arr_E25[i],Ib_arr))  # Eпит,Iэ,Rэ,Uбэ,Rб,Iб

    R1_arr = np.array(R1_arr)
    R1_arr = to_E24_(R1_arr)  # Округление R1 до ряда
    print("Сопротивления R1:\n", R1_arr.shape)

    # Расчёт сопротивлений базы R2
    R2_arr = R2_(Rb_arr_E25, R1_arr)
    R2_arr = to_E24_(R2_arr)  # Округление R2 до ряда
    print("Сопротивления R2:\n", R2_arr.shape)

    # Расчёт сопротивлений базы
    Rb_arr_E25 = (R1_arr * R2_arr) / (R1_arr + R2_arr)
    print("Сопротивлений базы 2:\n", Rb_arr_E25.shape)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '                         Определение возможных Eсм                             '

    Ecm = []
    for i in range(len(Ep_arr)):
        Ecm.append((Ep_arr[i] * R2_arr[i]) / (R1_arr[i] + R2_arr[i]))
    Ecm = np.array(Ecm)
    # print(Ecm.shape)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '                      Определяем возможный разброс тока                        '

    # коэффициент перераспределения тока базы
    y = R_e_arr / (R_e_arr + Rb_arr_E25 + 0.001)
    dIt = (e * dT * betta) / (Rb_arr_E25 + (R_e_arr * (1 + betta)))
    dIB = dB * Ik_arr / (betta * (1 + betta * y))
    dI = (dIt + dIB)

    dUt_2_orig = dI * R_post_arr

    Up_orig = (Ik_arr * R_per_arr) - dUt_2_orig
    mask_1 = np.array([Up_orig > 0][0], dtype='int32')
    Up = abs(Up_orig - Un)

    mask_2 = np.array([Up < Un * 0.9][0], dtype='int32')
    mask_V = mask_1 * mask_2

    mask_1 = np.array([dUt_2_orig > 0][0], dtype='int32')
    dUt_2 = abs(dUt_2_orig - d_Ut)
    mask_2 = np.array([dUt_2 < d_Ut * 0.9][0], dtype='int32')
    mask_U = mask_1 * mask_2
    procents = status_bar(procents, full)
    dict_results = {'Ток коллектора': Ik_arr,
                      'Ток базы': Ib_arr, 'Ток эмиттера': Ie_arr, 'Допустимый тепловой ток': d_I_dop,
                      'Напряжение питания': Ep_arr, 'Напряжение коллектор-эмиттер': UA_arr,
                      'Напряжение по переменному току': Em_arr, 'Сопротивление по постоянному току': R_post_arr,
                      'Сопротивление по переменному току': R_per_arr, 'Сопротивление коллектора': R_k_arr,
                      'Первый расчёт Rб': Rb_arr, 'Коэффициент перераспределения тока коллектора': y,
                      'Тепловой разброс тока': dIt, 'Разброс тока из-за усиления': dIB,
                      'Суммарный разброс по току': dI, 'Напряжение смещения': Ecm,
                      'Тепловой запас напряжения': dUt_2_orig, 'Нпряжение Uп': Up_orig,
                      'Сопротивление эмиттера': R_e_arr, 'Сопротивление R1': R1_arr, 'Сопротивление R2': R2_arr,
                      'Результирующее Rб': Rb_arr_E25}
    return dict_results

def start_calculate_2(dict_values):
    Un = float(dict_values['Напряжение нагрузки'])  # Напряжение нагрузки
    Rn = float(dict_values['Сопротивление нагрузки'])  # Сопротивление нагрузки
    In = float(dict_values['Ток нагрузки']) / 1000  # Ток нагрузки
    Rg = float(dict_values['Сопротивление генератора'])  # Сопротивление генератора
    K0 = float(dict_values['Коэффициент усиления'])  # Коэффициент усиления
    Emax = float(dict_values['E максимально допустимое'])  # E максимально допустимое
    dT = float(dict_values['Максимальное отклонение темпиратуры'])  # Максимальное отклонение темпиратуры
    fn = float(dict_values['Нижняя граничная частота'])  # Нижняя граничная частота
    C_e_per = float(dict_values['Ёмкость эмиттерного перехода']) / (10 ** (-12))  # Ёмкость эмиттерного перехода
    C_k_per = float(dict_values['Ёмкость коллекторного перехода']) / (10 ** (-12))  # Ёмкость коллекторного перехода
    Cn = float(dict_values['Ёмкость нагрузки']) / (10 ** (-9))  # Ёмкость нагрузки
    f_T = float(dict_values['Частота единичного усиления']) * (10 ** 6)  # Частота единичного усиления

    # Параметры

    d_Unel = float(dict_values['Дельта U нелинейное'])  # Дельта U нелинейное
    d_Ut = float(dict_values['Дельта U тепловое'])  # Дельта U тепловое
    Ik0 = float(dict_values['Тепловой ток коллектора']) / 1000  # Тепловой ток коллектора
    e = float(dict_values['Температурный коэффициент'])  # Температурный коэффициент

    # Расчитываемые в п.2 параметры транщистора

    betta = float(
        dict_values['Коэффициент усиления по току'])  # Усиление по току (получить из малосигнальных параметров)
    Ube = float(
        dict_values['Напряжение база-эмиттер'])  # Напряжение база-эмиттер (получить из малосигнальных параметров)
    h11 = float(dict_values['Входное сопротивление транзистора (h11)'])
    dB = max([abs(120 - betta), abs(40 - betta)])  # Максимальное отклонение усиления по току

    # Гиперпараметры для программы
    z = 1  # Запас по напряжению по переменному току (не рекомендуется брать больше 2 и оставлять 0)
    resolution = 64  # разрешение выходной карты
    full = 8
    procents = 1

    '                   Определение возможных напряжений питиния                   '
    # Массив с возможными для данного транзистора напряжениями питания

    Ep_arr = []
    if (float(dict_values['Нарпяжение пинатия Eпит']) != 0) and (float(dict_values['Нарпяжение пинатия Eпит']) < float(dict_values['E максимально допустимое'])):
        Ep_arr = [float(dict_values['Нарпяжение пинатия Eпит'])]
        print('Напряжение питания', Ep_arr)
    else:
        # TODO:вывести меседж бокс, о невозможности проводить дальнейшие вычисления
        print("Неверно введено: Напряжения питания")
        return

    procents = status_bar(procents, full)

    # ===============================================================================#
    '      Определение возможных напряжений коллектор-эмиттер в рабочей точке       '
    UA_arr = []
    try:
        if float(dict_values['Напряжение коллектор-эмиттер']) != 0:
            UA_arr = [float(dict_values['Напряжение коллектор-эмиттер'])]
            print('Напряжение кол-эмит', UA_arr)
        else:
            print("Неверно введено: Напряжение UкА")
    except:
        print("Неверно введено: Напряжение UкА")
    procents = status_bar(procents, full)

    # ===============================================================================#
    '            Определение возможных токов коллектора в рабочей точке             '
    Ik_arr = []
    # Токи коллектора IкА:
    try:
        if float(dict_values['Ток коллектора']) != 0:
            Ik_arr = [float(dict_values['Ток коллектора']) / 1000]
        else:
            print('Неверно введено: Ток коллектора')
    except:
        print('Неверно введено: Ток коллектора')
    Ik_arr = np.array(Ik_arr)

    Ib_arr = []
    # Токи базы IбА:
    try:
        if float(dict_values['Ток базы']) != 0:
            Ib_arr = [float(dict_values['Ток базы']) / (10 ** (-6))]
            print('Ток базы', Ib_arr)
        else:
            for i in Ik_arr:
                Ib_arr.append(round(i / betta, 9))
    except:
        for i in Ik_arr:
            Ib_arr.append(round(i / betta, 9))
    Ib_arr = np.array(Ib_arr)

    Ie_arr = []
    # Токи эмиттера IэА:
    try:
        if float(dict_values['Ток эммитера']) != 0:
            Ie_arr = [float(dict_values['Ток эммитера']) / 1000]
            print('Ток эммитера', Ie_arr)
        else:
            Ie_arr = Ie_(Ib_arr, Ik_arr)
    except:
        Ie_arr = Ie_(Ib_arr, Ik_arr)
    Ie_arr = np.array(Ie_arr)

    if Ik_arr.shape[0] != 1:
        print("Ток коллектора:", Ik_arr.shape)
    else:
        print("Ток коллектора:", Ik_arr)

    if Ib_arr.shape[0] != 1:
        print("Ток базы:      ", Ib_arr.shape)
    else:
        print("Ток базы:      ", Ib_arr)

    if Ib_arr.shape[0] != 1:
        print("Ток эмиттера:  ", Ie_arr.shape)
    else:
        print("Ток эмиттера:  ", Ie_arr)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '        Определение матрицы возможных сопротивлений по постоянному току        '

    # Сопротивления по постоянному току
    try:
        R_post_arr = []
        for i in range(len(Ep_arr)):
            E = []
            for j in UA_arr[i]:
                U = []
                for k in Ik_arr:
                    U.append(round(R_post_(Ep_arr[i], j, k), 3))
                E.append(U)
            R_post_arr.append(E)
        R_post_arr = np.array(R_post_arr)
        print("Сопротивления по пост. току:", R_post_arr.shape)
    except:
        R_post_arr = np.array([round(R_post_(Ep_arr[0], UA_arr[0], Ik_arr[0]), 3)])
        print("Сопротивления по пост. току:", R_post_arr)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '                          Определение возможных Em                             '

    # Напряжение по переменному току
    Em_arr = []
    try:
        for i in range(len(Ep_arr)):
            Em_part = []
            # Отступ от минимального
            for k in UA_arr[i]:
                Em_part.append(round(Em_min_(d_Ut, Un, k) + z, 2))
            Em_arr.append(Em_part)
        print("Напряжение по пер. току:", np.array(Em_arr).shape)
    except:
        Em_arr = np.array([round(Em_min_(d_Ut, Un, UA_arr[0]) + z, 2)])
        print("Напряжение по пер. току:", Em_arr)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '                Определение возможных сопротивлений цепи ОЭ                    '
    # Расчёт сопротивлений по переменному току
    threshold = 0
    R_per_arr = []
    try:
        for i in range(len(Ep_arr)):
            E = []
            for j1, j2 in zip(Em_arr[i], UA_arr[i]):
                U = []
                for k in Ik_arr:
                    U.append(R_per_(j1, j2, k))
                E.append(U)
            R_per_arr.append(E)

        R_per_arr = np.array(R_per_arr)
        print("Сопротивления по переменному току:\n", R_per_arr.shape)
    except:
        R_per_arr = np.array([R_per_(Em_arr[0], UA_arr[0], Ik_arr[0])])
        print("Сопротивления по переменному току:\n", R_per_arr)

    # Расчёт сопротивлений коллектора
    R_k_arr = R_k_(R_per_arr, Rn)
    if R_k_arr.shape[0] != 1:
        print("Сопротивления коллектора:\n", R_k_arr.shape)
    else:
        print("Сопротивления коллектора:\n", R_k_arr)
    # Округление Rк до ряда
    R_k_arr = to_E24_(R_k_arr)
    if R_k_arr.shape[0] != 1:
        print("Сопротивления коллектора:\n", R_k_arr.shape)
    else:
        print("Сопротивления коллектора:\n", R_k_arr)

    # Расчёт сопротивлений эмиттера
    R_e_arr = R_post_arr - R_k_arr
    if R_e_arr.shape[0] != 1:
        print("Сопротивления эмиттера:\n", R_e_arr.shape)
    else:
        print("Сопротивления эмиттера:\n", R_e_arr)

    # Расчёт сопротивлений базы
    Rb_arr = []
    Rb_arr_E25 = []
    d_I_dop = d_Ut / R_post_arr
    for i in range(len(Ib_arr)):
        Rb_arr.append(
            ((betta * ((d_I_dop.T[i]) * (R_e_arr.T[i]) - (e * dT))) / ((Ib_arr[i] * dB) - (d_I_dop.T[i]))) -
            R_e_arr.T[i] - threshold)
    Rb_arr = np.array(Rb_arr).T
    Rb_arr_E25 = np.array(Rb_arr)

    if Rb_arr.shape[0] != 1:
        print("Сопротивления базы:\n", Rb_arr.shape)
    else:
        print("Сопротивления базы:\n", Rb_arr)

    # Округление Rб до ряда
    Rb_arr_E25 = to_E25_(Rb_arr_E25)

    # Расчёт сопротивлений базы R1
    R1_arr = []
    for i in range(len(Ep_arr)):
        R1_arr.append(R1_(Ep_arr[i], Ie_arr, R_e_arr[i], Ube, Rb_arr_E25[i],
                          Ib_arr))  # Eпит,Iэ,Rэ,Uбэ,Rб,Iб

    R1_arr = np.array(R1_arr)
    R1_arr = to_E24_(R1_arr)  # Округление R1 до ряда
    if R1_arr.shape[0] != 1:
        print("Сопротивления R1:\n", R1_arr.shape)
    else:
        print("Сопротивления R1:\n", R1_arr)

    # Расчёт сопротивлений базы R2
    R2_arr = R2_(Rb_arr_E25, R1_arr)
    R2_arr = to_E24_(R2_arr)  # Округление R2 до ряда
    if R2_arr.shape[0] != 1:
        print("Сопротивления R2:\n", R2_arr.shape)
    else:
        print("Сопротивления R2:\n", R2_arr)

    # Расчёт сопротивлений базы
    Rb_arr_E25 = (R1_arr * R2_arr) / (R1_arr + R2_arr)
    if Rb_arr_E25.shape[0] != 1:
        print("Сопротивлений базы 2:\n", Rb_arr_E25.shape)
    else:
        print("Сопротивлений базы 2:\n", Rb_arr_E25)

    procents = status_bar(procents, full)

    # ===============================================================================#
    '                         Определение возможных Eсм                             '

    Ecm = []
    for i in range(len(Ep_arr)):
        Ecm.append((Ep_arr[i] * R2_arr[i]) / (R1_arr[i] + R2_arr[i]))
    Ecm = np.array(Ecm)
    # print(Ecm.shape)
    procents = status_bar(procents, full)

    # ===============================================================================#
    '                      Определяем возможный разброс тока                        '

    # коэффициент перераспределения тока базы
    y = R_e_arr / (R_e_arr + Rb_arr_E25 + 0.001)
    dIt = (e * dT * betta) / (Rb_arr_E25 + (R_e_arr * (1 + betta)))
    dIB = dB * Ik_arr / (betta * (1 + betta * y))
    dI = (dIt + dIB)

    dUt_2_orig = dI * R_post_arr

    Up_orig = (Ik_arr * R_per_arr) - dUt_2_orig
    mask_1 = np.array([Up_orig > 0][0], dtype='int32')
    Up = abs(Up_orig - Un)

    mask_2 = np.array([Up < Un * 0.9][0], dtype='int32')
    mask_V = mask_1 * mask_2

    mask_1 = np.array([dUt_2_orig > 0][0], dtype='int32')
    dUt_2 = abs(dUt_2_orig - d_Ut)
    mask_2 = np.array([dUt_2 < d_Ut * 0.9][0], dtype='int32')
    mask_U = mask_1 * mask_2
    procents = status_bar(procents, full)