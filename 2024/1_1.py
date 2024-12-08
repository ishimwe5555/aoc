list1 = [1, 2, 2, 4, 5]
set1 = [1, 2,4, 5] #

p1,p2 = 0,0
k = None
print(k) if k else print("none value")

while p1 < len(list1):
    if list1[p1]!= set1[p2]:
        k = list1[p1]
        break
    p1 +=1
    p2+=1
print(k)
