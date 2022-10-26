# Percobaan 4: Lambda
# alpro603.py

'''
def = fungsi dengan nama
lambda = fungsi tanpa nama (anonymous function)

variabel = lambda param: statement

def hitungPangkat(x):
    return x**3


#hitungPangkat = lambda x: x**3
def hitungPangkat(x):
    return hitungPangkat(x)

nilai = float(input("Hitung pangkat 3 dari = "))
nilai2 = 2
#hasil = hitungPangkat(nilai)
hasil = lambda x,y: x**3 + y
print("Pangkat 3 dari %.2f adalah %.2f" % (nilai, hasil(nilai,nilai2)))

5! = 5 x 4 x 3 x 2 x 1
0! = 1
1! = 1

Faktorial(3)
3! = 3 x 2 x 1
3 * (3-1) = 6
'''
def Faktorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*Faktorial(n-1)
n = int(input("Basis: "))
print(Faktorial(n))
'''
Faktorial(3)
3 * Faktorial(2)
3 * 2 * Faktorial(1)
3 * 2 * 1 = 6

Faktorial(4)
4 * Faktorial(3)
4 * 3 * Faktorial(2)
4 * 3 * 2 * Faktorial(1)
4 * 3 * 2 * 1 = 24

def pi(n):
    a = 1
    kali = -1
    hitung += kali*4/a
    a += 2
    kali *= -1
'''