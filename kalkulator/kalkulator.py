# Kalkulator Mini
def penjumlahan(x, y):
    return x + y


def pengurangan(x, y):
    return x - y


def perkalian(x, y):
    return x * y


def pembagian(x, y):
    return x / y


print("Pilih operasi bilangan!")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

while True:
    pilihan = input("Pilihanmu (1/2/3/4): ")

    if pilihan in ('1', '2', '3', '4'):
        angka1 = float(input("Masukkan angka pertama : "))
        angka2 = float(input("Masukkan angka kedua : "))

        if pilihan == '1':
            print(angka1, "+", angka2, "=", penjumlahan(angka1, angka2))

        elif pilihan == '2':
            print(angka1, "-", angka2, "=", pengurangan(angka1, angka2))

        elif pilihan == '3':
            print(angka1, "*", angka2, "=", perkalian(angka1, angka2))

        elif pilihan == '4':
            print(angka1, "/", angka2, "=", pembagian(angka1, angka2))
        break
    else:
        print("Pilihan tidak sesuai.")
