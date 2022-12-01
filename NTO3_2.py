#функция get_primer
#принимает:
    #последовательность
    #длину праймера
    #минимально допустимый ГЦ-состав (значение по умолчанию 50)
    #максимально допустимый ГЦ-состав (значение по умолчанию 60)
    #минимально допустимая температура плавления (значение по умолчанию 50)
    #максимально допустимая температура плавления (значение по умолчанию 60)
    #максимально допустимое количество самокомплиментарных нуклеотидов на 3'-конце (значение по умолчанию 4)
#вернуть первый попавшийся праймер, который будет удовлетворять всем условиям и остановиться
#если не удалось найти - False

def get_primer(line, l, *arg):
    line, l = line.upper(), int(l)  #изменяем входные данные для удобства
    k = len(line)
    for i in range(0, len(line)+1):     #цикл плавающих окон
        if (i + l) > k:                 #прервать цикл при достижении конца последовательности
            break  
        
        primer = line[i:i+l]            #находим праймер нужной длины
        w, x, y, z = primer.count("A"), primer.count("T"), primer.count("G"), primer.count("C") #ищем температуру плавления
        Tm = 64.9 + 41 * (y + z - 16.4) / (w + x + y + z)
        
        arg_len = len(arg)
        min_gc = arg[0] if arg_len > 0 else 50  #устанавливаем значения для параметров
        max_gc = arg[1] if arg_len > 1 else 60
        min_t = arg[2] if arg_len > 2 else 50
        max_t = arg[3] if arg_len > 3 else 60
        num_comp = arg[4] if arg_len > 4 else 4
        
        g_c = int((primer.count("G") + primer.count("C")) / l * 100)  #считаем ГЦ-состав
        
        site = primer[-1:(- int(num_comp)):-1]  #ищем самокомплементарные участки
        comp_site = ""
        for s in site:
            if s in ("A", "T"):
                s = "A" if s == "T" else "T"
            else:
                s = "G" if s == "C" else "C"
            comp_site += s
    
    if (int(min_gc) <= g_c <= int(max_gc)) and (int(min_t) <= Tm <= int(max_t)) and (comp_site not in primer):
        return primer        
        exit
    else:
        return False    

 
a, b, c, d, e, f, z = input(), input(), input(), input(), input(), input(), input()
print(get_primer(a, b, c, d, e, f, z))

