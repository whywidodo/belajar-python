from random import choice

nama_orang = []
file = open('nama.txt', 'r')
nama_orang = file.read().splitlines()
print(nama_orang)

Tim1 = []
Tim2 = []

while len(nama_orang) > 0:
    orang1 = (choice(nama_orang))
    Tim1.append(orang1)
    nama_orang.remove(orang1)

    if nama_orang == []:
        break

    orang2 = (choice(nama_orang))
    Tim2.append(orang2)
    nama_orang.remove(orang2)

print('Team A : ', Tim1)
print('Team B : ', Tim2)
