import random

huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
angka = "0123456789"

campur = huruf_kecil+huruf_besar+angka

panjang = 10
password = "".join(random.sample(campur, panjang))
print(password)
