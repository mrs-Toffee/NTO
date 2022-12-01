#функциz is_self_compliment
#последовательность праймера (в любом регистре, в направлении 5'-3') 
#максимально допустимое количество самокомпелментарных нуклеотидов на 3'-конце (целое число)
#функция должна возвращать True, если заданное количество нуклеотидов является самокомплиментарными, и False в противном случае.

def is_self_compliment(line, num_comp):
    primer = line.upper()
    print(primer)
    site = primer[-1:(-1 - int(num_comp)):-1]
    print(site)
    comp_site = ""
    for s in site:
        if s in ("A", "T"):
            s = "A" if s == "T" else "T"
        else:
            s = "G" if s == "C" else "C"
        comp_site += s
    print(comp_site)
    if comp_site in primer:
        return True
    else:
        return False


line, num_comp = input(), input()
print(is_self_compliment(line, num_comp))

#ATGGCAGCCCACACGATACAGGG 3 (T)
#ACACTAACGACCGTATCGA 4 (T)
#GATTTGTAACTTCCTTTTTTCGC 4 (F)
