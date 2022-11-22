#[хромосома]:[позиция на хромосоме] [референсный нуклеотид]/[альтернативный нуклеотид] 
#chr1:1267483 G/A
#если служебная строка - False
#номер хромосомы - позиция на хромосоме - идентификатор из dbSNP - референсный аллель - альтернативный аллель - служебные столбцы

def formating(line):
    if line[0] == "#":
        return("False")
    else:
        chr = line[0]
        pos = line[1]
        r_a, a_a = line[3], line[4]
        return(f"chr{chr}:{pos} {r_a}/{a_a}")


line = input().split("\t")
print(formating(line))

##fileformat=VCFv4.2
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	NA00001	NA00002	NA00003
# 20	14370	rs6054257	G	A	29	PASS	NS=3;DP=14;AF=0.5;DB;H2	GT:GQ:DP:HQ	0|0:48:1:51,51	1|0:48:8:51,51	1/1:43:51:51
# 5	112151205	-	G	.
