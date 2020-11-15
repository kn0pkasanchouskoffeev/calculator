deystvie = input("выберите действие. 1. сложение. 2. вычитание. 3. умножение. 4. деление. или exit для завершения программы.")
while deystvie != "exit":
    firstnumber = int(input("введите первое число"))
    secondnumber = int(input("введите второе число"))
    if deystvie == "1" or deystvie == "сложение":
        print(firstnumber + secondnumber)
    elif deystvie == "2" or deystvie == "вычитание":
        print(firstnumber - secondnumber)
    elif deystvie == "3" or deystvie == "умножение":
        print(firstnumber * secondnumber)
    elif deystvie == "4" or deystvie == "деление":
        print(firstnumber / secondnumber)
    deystvie = input("выберите действие. 1. сложение. 2. вычитание. 3. умножение. 4. деление. или exit для завершения программы.")
