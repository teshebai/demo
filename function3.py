#Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно. 
a = int(input("a="))
b = int(input("b="))
for i in range(a, b+1):
    print(i)
#3 esep
#Dаны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. В этой задаче можно обойтись без инструкции if
a = int(input())
b = int(input())
for i in range(a-int((a%2)==0), b-1, -2):
    print(i)        
#2 esep  Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае. 
A = int(input())
B = int(input())
if A<B:
    for i in range(A, B+1):
        print(i)
else:
    for i in range(A, B-1, -1):
        print(i)

#4 esep
import random
# карта саны 
N = 10
# карта списогы
cntList = list(range(1,N+1))
mylist = list(range(1,N+1))
# Выбираем случайный элемент
# и удаляем из колоды
delNum = random.choice(mylist)
mylist.remove(delNum)
print ('Контрольный список карт: %s' % (cntList))
print ('Список без карты: %s' % (mylist))
print ('*Подсказка* - Удаленная карта: %s' % (delNum))
findCard = ((set(cntList)) - (set(mylist)))
print ('Удаленная карта: %s' % (findCard))
        