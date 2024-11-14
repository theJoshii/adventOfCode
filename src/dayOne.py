


with open("src/resources/dayOne.txt", "r") as file:
    result = 0
    while (line := file.readline().strip()):
        a = 0
        b = 0
        for char in line:
            if char.isdigit():
                if a == 0:
                    a = int(char)
                    b = int(char)
                else:
                    b = int(char)
        result += a * 10 + b
    print(result)                