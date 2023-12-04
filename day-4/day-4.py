total = 0
valueperline = 0

#solution 1

with open("day-4/input.txt", 'r') as file:
    data = file.read().splitlines()
    for line in data: 
        winning_nums_list = []
        your_nums_list = []
        total += valueperline
        valueperline = 0
        

        #split data
        split_data = line.split('|')
        winning_nums =  split_data[0].split(':')
        winning_nums = winning_nums[1]
        your_nums =  split_data[1]

        #split into numbers
        winning_nums_list = winning_nums.split(' ')
        your_nums_list = your_nums.split(' ')

        matches = set(your_nums_list).intersection(set(winning_nums_list))
        matches = list(filter(None, matches))



        for match in matches:
            if(valueperline == 0):
                valueperline = 1
            elif(valueperline > 0):
                valueperline *= 2

print('solution 1 total:', total)
