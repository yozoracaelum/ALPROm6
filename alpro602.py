# Percobaan 2: Fungsi dengan parameter
# alpro602.py

'''

luasPersegiPanjang(m,n) = m x n
f(x,y) = x * y
luasPersegiPanjang(5,3) = 5 x 3 = 15
'''
def luasPersegiPanjang(m, n):
    return m * n

panjang = float(input("Panjang = "))
lebar = float(input("Lebar = "))

print("Luas persegi panjang = %.f" % luasPersegiPanjang(panjang, lebar))