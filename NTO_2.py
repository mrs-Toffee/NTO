#функция check_primer
#входные данные:
    # последовательность праймера (в любом регистре)
    # минимально допустимый ГЦ-состав (процент нуклеотидов Г и Ц от всех нуклеотидов в последовательности) (значение по умолчанию 50)
    # максимально допустимый ГЦ-состав (значение по умолчанию 60)
    # минимально допустимая длина праймера (значение по умолчанию 18)
    # максимально допустимая длина праймера (значение по умолчанию 25)
#вычислить ГЦ-состав и длину праймера и, если значения ГЦ-состава и длины праймера находятся в допустимых пределах, функция должна вернуть True, иначе - False.

def check_primer(g_c, l):
    if (min_gc <= g_c <= max_gc) and (min_l <= l <= max_l):
        return "True"
    else:
        return "False"    


line = input().upper().split()    
min_gc = int(line[1]) if len(line) > 1 else 50
max_gc = int(line[2]) if len(line) > 2 else 60
min_l = int(line[3]) if len(line) > 3 else 18
max_l = int(line[4]) if len(line) > 4 else 25
primer = line[0]
l = len(primer)
g_c = int((primer.count("G") + primer.count("C")) / l * 100)
print(check_primer(g_c, l))

# проверка: ATGGCAGGCACACGATACAGG (T)
#CCAGCATATGACAGGCACAGTTGC 55 65 20 25 (F)
#CGTATGCAGCAGTATAGGGCAGCCCAC 52 62 20 (F)
#cgtatgcatcagtataggcaatcc 40 60 20 30 (T)