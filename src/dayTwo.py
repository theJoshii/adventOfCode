

with open("src/resources/dayTwo.txt", "r") as file:
    
    totalIds = 0

    # MAX RED = 12 MAX GREEN = 13 MAX BLUE = 14 
    currentId = 0
    while(line := file.readline().strip()):
        reds, greens, blues, possible, = 0, 0, 0, True
        currentId += 1
        offsets = line.find(":") + 1
        position = 0
        while(line.find("red")!= -1):
            position = line.find("red", position + 1)
            subStr = line[position-3: position]
            value = 0
            for char in subStr:
                if char.isdigit() and value == 0:
                    value = int(char)
                elif char.isdigit():
                    value *= 10
                    value += int(char)
            if value > 12:
                possible = False       
            position += len("red")
        while(line.find("green")!= -1):
            position = line.find("green", position + 1)
            subStr = line[position-3: position]
            value = 0
            for char in subStr:
                if char.isdigit() and value == 0:
                    value = int(char)
                elif char.isdigit():
                    value *= 10
                    value += int(char)
            if value > 13:
                possible = False       
                
            position += len("green")
        while(line.find("blue")!= -1):
            position = line.find("blue", position + 1)
            subStr = line[position-3: position]
            value = 0
            for char in subStr:
                if char.isdigit() and value == 0:
                    value = int(char)
                elif char.isdigit():
                    value *= 10
                    value += int(char)
            if value > 14:
                possible = False       
        if possible:
            totalIds += currentId
            




