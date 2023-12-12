li1 = [int(x) for x in input().split()]
li2 = [int(x) for x in input().split()]

# bubble sort

for i in range(len(li1)-1):
    for j in range(len(li1)-1-i):
        if li1[j] > li1[j+1]:
            li1[j], li1[j+1] = li1[j+1], li1[j]
            li2[j], li2[j+1] = li2[j+1], li2[j]

# for x in li2:
#     print(x, end=" ")
print(li2)