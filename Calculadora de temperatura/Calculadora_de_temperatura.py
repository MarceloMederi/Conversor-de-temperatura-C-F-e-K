def regra():
    print("+" * 65)
    print("CONVERSOR DE TEMPERATURA CELSIUS(C), FAHRENHEIT(F) E KELVIN(K)")
    print("+" * 65)

def menu():

        opcao = 0
        opcao = int(input("Qual tabela de conversão você gostaria de usar:[1- C/F], [2- C/K], [3- F/C], [4- F/K], [5- K/C], [6- K/F]:"))
        print("")
        while (opcao != "1" and "2" and "3" and "4" and "5" and "6"):
            if opcao == 1:
                X = float(input("Qual a temperatura:"))
                F = (X * 9 / 5) + 32
                print("A temperatura em Fahrenheit é {:.1f}" .format(F) ,"°F")
                break
            elif opcao == 2:
                X = float(input("Qual a temperatura:"))
                K = (X + 273.15)
                print("A temperatura em Kelvin é {:.1f}" .format(K) , "°K")
                break
            elif opcao == 3:
                X = float(input("Qual a temperatura:"))
                C = (X - 32) * 5/9
                print("A temperatura em Celsius é {:.1f}" .format(C) , "°C")
                break
            elif opcao == 4:
                X = float(input("Qual a temperatura:"))
                K = (X - 32) * 5/9 + 273.15
                print("A temperatura em Kelvin é {:.1f}" .format(K) , "°K")
                break
            elif opcao == 5:
                X = float(input("Qual a temperatura:"))
                C = X - 273.15
                print("A temperatura em Celsius é {:.1f}" .format(C) , "°C")
                break
            elif opcao == 6:
                X = float(input("Qual a temperatura:"))
                F = (X - 273.15) * 9/5 + 32
                print("A temperatura em Fahrenheit é {:.1f}" .format(F) , "°F")
                break
            else:
                print("OPÇÃO ERRADA! . ESCOLHA ENTRE AS OPÇOES DE 1 A 6.")
                break

while True:
    regra()
    menu()