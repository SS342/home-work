#задача номер 1


while True:
    q = int(input())
    if q % 7 == 0 :
        print('yes')
    else:
        print('no')



#задача номер 2;
#1 способ


n = int(input())
c = []
for i in range(n):
    tmp = int(input())
    if tmp == 2:
        c.append(tmp)
print(len(c))


#2 способ(без списка)


n = int(input())
j = 0 
for i in range(n):
    tmp = int(input())
    if tmp == 2:
        j = j + 1
print(j)