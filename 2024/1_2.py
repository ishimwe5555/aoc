
data = open('inputs/1_1.txt', 'r').read().splitlines()
print(data)
list1 = []
list2 = []
score = 0

def getAppeanceTimes(number,refList):
    n = 0
    for i in range(len(refList)):
        if number == refList[i]:
            n+=1
    return n


for loc in data:
    list1.append(int(loc.split("   ")[0]))
    list2.append(int(loc.split("   ")[1]))


for i in (list1):
    nbrOfTimes = getAppeanceTimes(i,list2)
    score += nbrOfTimes * i


print(score)