
import math

print("===================================")
print("       PROGRAM KALKULATOR          ")
print("===================================")

while True:
    print("\nPILIH OPERATOR")
    print("-----------------------------------")
    print("+   Penjumlahan")
    print("-   Pengurangan")
    print("*   Perkalian")
    print("/   Pembagian")
    print("%   Modulus (sisa bagi)")
    print("**  Pangkat")
    print("//  Pembagian bulat")
    print("sqrt Akar kuadrat")
    print("1   Persen")
    print("sin Sinus")
    print("cos Cosinus")
    print("tan Tangen")
    print("log Logaritma")
    print("exit Keluar")
    print("-----------------------------------")

    opr = input("Pilih operator = ").lower()

    if opr == "exit":
        print("Terima kasih telah menggunakan kalkulator!")
        break

    try:
        if opr == "sqrt":
            bil1 = float(input("Bilangan = "))
            if bil1 >= 0:
                print("Hasil =", math.sqrt(bil1))
            else:
                print("Error: bilangan tidak boleh negatif")

        elif opr == "sin":
            bil1 = float(input("Sudut (derajat) = "))
            hasil = math.sin(math.radians(bil1))
            print("Hasil =", hasil)

        elif opr == "cos":
            bil1 = float(input("Sudut (derajat) = "))
            hasil = math.cos(math.radians(bil1))
            print("Hasil =", hasil)

        elif opr == "tan":
            bil1 = float(input("Sudut (derajat) = "))
            sudut = math.radians(bil1)

            if abs(math.cos(sudut)) < 1e-10:
                print("Error: nilai tangen tidak terdefinisi")
            else:
                print("Hasil =", math.tan(sudut))

        elif opr == "log":
            bil1 = float(input("Bilangan = "))
            if bil1 > 0:
                print("Hasil =", math.log10(bil1))
            else:
                print("Error: bilangan harus lebih dari 0")

        elif opr in ["+", "-", "*", "/", "%", "**", "//", "1"]:
            bil1 = float(input("Bil 1 = "))
            bil2 = float(input("Bil 2 = "))

            if opr == "+":
                print(bil1, "+", bil2, "=", bil1 + bil2)

            elif opr == "-":
                print(bil1, "-", bil2, "=", bil1 - bil2)

            elif opr == "*":
                print(bil1, "x", bil2, "=", bil1 * bil2)

            elif opr == "/":
                if bil2 != 0:
                    print(bil1, ":", bil2, "=", bil1 / bil2)
                else:
                    print("Error: tidak bisa dibagi 0")

            elif opr == "%":
                if bil2 != 0:
                    print(bil1, "%", bil2, "=", bil1 % bil2)
                else:
                    print("Error: tidak bisa dibagi 0")

            elif opr == "**":
                print(bil1, "^", bil2, "=", bil1 ** bil2)

            elif opr == "//":
                if bil2 != 0:
                    print(bil1, "//", bil2, "=", bil1 // bil2)
                else:
                    print("Error: tidak bisa dibagi 0")

            elif opr == "1":
                print(bil1, "% dari", bil2, "=", bil1 / 100 * bil2)

        else:
            print("Error: Operator tidak tersedia!")

    except ValueError:
        print("Error: Masukkan angka dengan benar!")

    print("===================================")
