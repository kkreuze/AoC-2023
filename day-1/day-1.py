total = 0

#solution 1
with open("day-1/input.txt", 'r') as data_file:
    for line in data_file:
        numslist = []
        data = line.split()
        for i in range(len(data)):
            for char in data[i]:
                if char.isdigit():
                    numslist.append(int(char))
        
        first_digit = numslist[0]
        last_digit = numslist[-1]
        temp = int(str(first_digit) + str(last_digit))
        total += temp


print('solution 1 total:', total)

#solution 2
total_2 = 0

def getFirstDigit(data_2, i, charlist, charvalue):
    for char in data_2[i]:
        charlist.append(char)
        charvalue = ''.join(charlist)
        if('one' in charvalue):
            return 1
        elif('two' in charvalue):
            return 2
        elif('three' in charvalue):
            return 3
        elif('four' in charvalue):
            return 4
        elif('five' in charvalue):
            return 5
        elif('six' in charvalue):
            return 6
        elif('seven' in charvalue):
            return 7
        elif('eight' in charvalue):
            return 8
        elif('nine' in charvalue):
            return 9
        elif (char.isdigit()):
            return int(char)
        
def getLastDigit(data_2, i, charlist, charvalue):
    charlist = []
    for char in reversed(data_2[i]):
        charlist.append(char)
        charvalue = ''.join(charlist)
        if('eno' in charvalue):
            return 1
        elif('owt' in charvalue):
            return 2
        elif('eerht' in charvalue):
            return 3
        elif('ruof' in charvalue):
            return 4
        elif('evif' in charvalue):
            return 5
        elif('xis' in charvalue):
            return 6
        elif('neves' in charvalue):
            return 7
        elif('thgie' in charvalue):
            return 8
        elif('enin' in charvalue):
            return 9
        elif (char.isdigit()):
            return int(char)


with open("day-1/input.txt", 'r') as data_file:
    for line in data_file:
            numslist_2 = []
            charlist = []
            charvalue = ''
            data_2 = line.split()
            for i in range(len(data_2)):
                numslist_2.append(getFirstDigit(data_2, i, charlist, charvalue))
                numslist_2.append(getLastDigit(data_2, i, charlist, charvalue))
            first_digit_2 = numslist_2[0]
            last_digit_2 = numslist_2[1]
            temp_2 = int(str(first_digit_2) + str(last_digit_2))
            total_2 += temp_2

print('solution 2 total:', total_2)
