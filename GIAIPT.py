import math
def GiaiPTBac1(a,b):
    if a!=0:
        return -b/a
    else:
        return "Phuong trinh vo nghiem"
def GiaiPTBac2(a,b,c):
    denta=b**2-a*c*4
    if denta>0:
        return f'Phuong trinh co 2 nghiem x1 = {(-b+math.sqrt(denta)/(2*a))} va x2 = {(-b-math.sqrt(denta)/(2*a))}'
    elif denta==0:
        return f'Phuong trinh co nghiem kep x = {-b/(2*a)}'
    else:
        return 'Phuong trinh vo nghiem'
def Tongabc(a,b,c):
    return a+b+c