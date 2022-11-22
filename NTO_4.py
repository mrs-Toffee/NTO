def calculate_tm(n):
    w = n.count("A")
    x = n.count("T")
    y = n.count("G")
    z = n.count("C")
    Tm = 64.9 + 41 * (y + z - 16.4) / (w + x + y + z)
    return(round(Tm))


n = input().upper()
print(calculate_tm(n))
#ATGGCAGGCACACGATACAGG
#ATGCCAATGGGTCCAGCTTTA