bil1 = int(input("Bil 1 = "))
opr = input("Operator (+, -, *, /, %, **, //, sin, cos, tan) = ")

if opr == "+":
    print(bil1, "+", bil2, "=", bil1 + bil2)
elif opr == "-":
    print(bil1, "-", bil2, "=", bil1 - bil2)
elif opr == "*":
    print(bil1, "x", bil2, "=", bil1 * bil2)
elif opr == "/":
    print(bil1, ":", bil2, "=", bil1 / bil2)
elif opr == "%":
    print(bil1, "%", bil2, "=", bil1 % bil2)
elif opr == "**":
    print(bil1, "^", bil2, "=", bil1 ** bil2)
elif opr == "//":
    print(bil1, "//", bil2, "=", bil1 // bil2)
elif opr == "sin":
    sudut = math.radians(bil1)
    print("Hasil =", math.sin(sudut))
elif opr == "cos":
    sudut = math.radians(bil1)
    print("Hasil =", math.cos(sudut))
elif opr == "tan":
    sudut = math.radians(bil1)
    print("Hasil =", math.tan(sudut))