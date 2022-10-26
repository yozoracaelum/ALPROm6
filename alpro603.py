# Percobaan 3: Fungsi dengan parameter
# alpro603.py

'''
def tulisVertikal("Python"):
    for i in "Python":
        print(i)

'''

def tulisVertikal(kata):
    for i in kata:
        j = i
        print(i)
    return j

ketikan = input("Tulisan = ")
tulisVertikal(ketikan)