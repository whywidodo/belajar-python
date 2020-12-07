import random
import sys

# Pertanyaan
orang, p, grup = [], int(input('Masukkan jumlah orang: ')), int(
    input('Masukkan jumlah grup: '))

if p < grup:
    # Jika kondisi ini benar maka akan menampilkan pesan
    # Program berhenti dengan menggunakan code dibawahnya
    print('Jumlah orang terlalu sedikit!')
    sys.exit()

for i in range(p):
    n = input('Masukkan orang {}: '.format(i+1))
    n = n[0].upper() + n[1:]  # Huruf pertama Kapital
    orang.append(n)
print(orang)

# make an empty list and inside it append each empty list
# length of grup times using list comprehension.
# use _ when you don't ever use it
team_g = [list() for _ in range(grup)]

while len(orang) > 0:
    for i in range(grup):
        p = random.choice(orang)
        team_g[i].append(p)
        orang.remove(p)
        if not orang:  # Jika tidak ada orang
            break
    continue  # Looping

for i in range(grup):
    print('Hasil grup {} adalah {}'.format(i+1, team_g[i]))
