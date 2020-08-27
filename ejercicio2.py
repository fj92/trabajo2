def primo():
    num = int(input("ingrese un numero : "))
    contador = 0
    for i in range(1, num+1):
        if num % i ==0:
            contador += 1
    if contador == 2:
        print("es primo")
        return True
    else:
        print(" no es primo")
    return False
        

def main():
    primo()
if __name__ == "__main__":
    main()