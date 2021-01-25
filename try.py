m = 12
four = 2
three = 2
two = 2
x = m//4
l1, list1 = [], []
if(x > four):
    d = x-four
    for i in range(four):
        l1.append(4)
    x1 = ((d*4)//3)
    r1 = ((d*4) % 3)
    print(x1)
    if(x1 > three):
        d1 = x1-three
        x2 = ((d*3)//2)
        r2 = ((d*3) % 2)

    else:
        for i in range(x1):
            l1.append(3)
else:
    for i in range(x):
        l1.append(4)
y = m % 4
if(y == 2):
    l1.append(2)
elif(y == 3):
    l1.append(3)
list1.append(l1)
print(list1)

# hag
