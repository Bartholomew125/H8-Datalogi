def Convert(n:int) -> str:
    string = ""
    while n > 0:
        kvotient = n//2
        rest = n%2
        string += str(rest)
        n = kvotient

    return string[::-1]

if __name__ == "__main__":
    while True:
        number = int(input("Number to convert: "))
        print(Convert(number))
