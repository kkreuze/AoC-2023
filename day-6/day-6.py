def calculatewinningways(time, distance):
    times = 0
    timesmore = 0
    for t, d in zip(time, distance):
        if times == 0:
            times = timesmore
        else:
            times *= timesmore
        timesmore = 0

        for i in range(int(t)):
            distancedone = 0
            timesince = i + 1
            speed = i + 1
            remainingtime = int(t) - timesince
            distancedone += speed * remainingtime

            if distancedone > int(d):
                timesmore += 1
    times *= timesmore
    return times

def calculatewinningways2(time, distance):
    times_2 = 0

    for i in range(int(time)):
        distancedone = 0
        timesince = i + 1
        speed = i + 1
        remainingtime = int(time) - timesince
        distancedone += speed * remainingtime

        if distancedone > int(distance):
            times_2 += 1
    return times_2

# solution 1
with open("day-6/input.txt", 'r') as file:
    time = []
    distance = []
    for line in file:
       if(line.split(':')[0] == 'Time'):
            a = line.split(':')[1]
            c = a.split(' ')
            for i in range(0, len(c)):
                if(c[i] != ''):
                    time.append(c[i])
       else:
            a = line.split(':')[1]
            c = a.split(' ')
            for i in range(0, len(c)):
                if(c[i] != ''):
                    distance.append(c[i])

# solution 2
with open("day-6/input.txt", 'r') as file:
    all_time = []
    all_distance = []
    for line in file:
       if(line.split(':')[0] == 'Time'):
            a = line.split(':')[1]
            c = a.split(' ')
            for i in range(0, len(c)):
                if(c[i] != ''):
                    all_time.append(c[i])
            all_time = int(''.join(all_time))

       else:
            a = line.split(':')[1]
            c = a.split(' ')
            for i in range(0, len(c)):
                if(c[i] != ''):
                    all_distance.append(c[i])
            all_distance = int(''.join(all_distance))


print('solution 1 total:', calculatewinningways(time, distance))
print('solution 2 total:', calculatewinningways2(all_time, all_distance))