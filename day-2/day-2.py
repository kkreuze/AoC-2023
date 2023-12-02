import re


#solution 1
sum = 0

def checkColor(reds, blues, greens, values):
    for i in range(len(values)):
            if 'red' in values[i]:
                red_digits = [] 
                redvalue = 0
                for char in values[i]:
                    if char.isdigit():
                        red_digits.append(char) 
                redvalue = int(''.join(red_digits))
                if redvalue > reds:
                    reds = redvalue
            elif 'blue' in values[i]:
                blue_digits = [] 
                bluevalue = 0
                for char in values[i]:
                    if char.isdigit():
                        blue_digits.append(char) 
                bluevalue = int(''.join(blue_digits))
                if bluevalue > blues:
                    blues = bluevalue
            elif 'green' in values[i]:
                green_digits = [] 
                greenvalue = 0
                for char in values[i]:
                    if char.isdigit():
                        green_digits.append(char) 
                greenvalue = int(''.join(green_digits))
                if greenvalue > greens:
                    greens = greenvalue
    if(reds <= 12 and blues <=14 and greens <= 13):
        return True

#solution 2 
sum_2 = 0

def checkColor2(reds, blues, greens, values):
    total = 0
    for i in range(len(values)):
            if 'red' in values[i]:
                red_digits = [] 
                redvalue = 0
                for char in values[i]:
                    if char.isdigit():
                        red_digits.append(char) 
                redvalue = int(''.join(red_digits))
                # print(redvalue, reds)
                if(reds == 0):
                    reds = redvalue
                elif redvalue > reds:
                    reds = redvalue
                    # print('new value', reds)
            elif 'blue' in values[i]:
                blue_digits = [] 
                bluevalue = 0
                for char in values[i]:
                    if char.isdigit():
                        blue_digits.append(char) 
                bluevalue = int(''.join(blue_digits))
                # print(bluevalue, blues)
                if blues == 0:
                    blues = bluevalue
                elif bluevalue > blues:
                    blues = bluevalue
                    # print('new value', blues)
            elif 'green' in values[i]:
                green_digits = [] 
                greenvalue = 0
                for char in values[i]:
                    if char.isdigit():
                        green_digits.append(char) 
                greenvalue = int(''.join(green_digits))
                # print(greenvalue, greens)
                if greens == 0:
                    greens = greenvalue
                elif greenvalue > greens:
                    greens = greenvalue
                    # print('new value', greens)
    # print(reds, blues, greens)
    total = reds*blues*greens
    return total


with open("day-2/input.txt", 'r') as file:
    data = file.read().splitlines()
    for line in data: 
        reds = 0
        blues = 0
        greens = 0
        values_temp = line.split(':')
        id = values_temp[0].split(' ')[1]
        values = values_temp[1]
        values = re.split(r'[;,]', values)
        if checkColor(reds, blues, greens, values) == True:
            # print('correct',  id)
            sum += int(id)
        
        sum_2 += checkColor2(reds, blues, greens, values)



print('solution 1 total:', sum)
print('solution 2 total:', sum_2)


