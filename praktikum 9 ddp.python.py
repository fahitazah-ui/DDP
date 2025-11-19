#soal no 4
def bilangan (angka) :
    for i in range (1, angka) :
        if i % 2 != 0:
            print (i, end= ", ")

bilangan (20)

print()

#soal no 3
def nilai (n = 0):
    if n <= 60:
        print("tidak lulus")
    elif n > 60 and n <= 100:
        print("lulus")
    else:
        print("tidak diketahui")

nilai(88)
nilai()


#soal no 2
def is_genap(n):
    return n % 2 == 0

print(is_genap(2))
print(is_genap(7))

#soal no 1
def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))