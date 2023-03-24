####
def max_two(x,y):
    if x>y:
        return x
    return y
def max_three(x, y ,z):
    return max_two(x,max_two(y,z))
print(max_three(3,8,-1))
########

########
l1=['abc','def','ghi']
up = lambda x:x.upper()
map(up,l1)
#########

########
l2 = [1,2,3,4,-2,-3,-5]
ln4=  lambda x: x>0
for i in l2:
    l2.append(ln4(i))
print(l2)
########

#######
l = [1,-9,8,9,0,8,-7]
ln = lambda x:x>0
list(filter(ln,l))
#######

#######
l1=[22,3,4,55,33,56,98,80]
ln1 = lambda x:x%2!=0
f1 = list(filter(ln1,l1))
print(f1)
#######

#######
def lis(l):
    list=[]
    for i in l:
        if i%2==0:
            list.append(i)
    return list
print(lis([1,5,92,6,8,7]))
#######

#######
#call by value
def myfunction(a):
    print("\t value in a is:",a)
    a+=2
    print("\t value of a changes to:",a)
num = 13
print("initial value of number is:",num)
myfunction(num)
print("the value of number is:",num)
#######

######
string="hello"
def function(string):
    string = "hello world"
    print("inside function , value of string is ",string)
function(string)
print("outside function,value of string is",string)
######

######
#call by reference 
def myfunction(mylist):
    print("\t list received:",mylist)
    mylist.append(3)
    mylist.extend([7,1])
    print("\t list after adding some elements :",mylist)
    mylist.remove(7)
    print("\t list within called function",mylist)
    return
list1 = [1]
print("list before function call:",list1)
myfunction(list1)
print("\t list after function call",list1)
######

######
#lambda function anonymous function
#lambda arguments:expression
sum = lambda x,y:x+y
print("sum of two numbers is",sum(4,4))
######

#######
#lambda fn in ordinary fn
def increment(y):
    return(lambda x:x+1)(y)
a = 100
print("a:",a)
print("a after incrementing:")
b=increment(a)
print(b)
#########

#####
def func(f,n):
    print(f(n))
twice = lambda x:x*2
thrice = lambda x:x*3
func(twice,4)
func(thrice,3)
#####

######
x= int(input("enter x:"))
y= int(input("enter y:"))
a= lambda x,y:x>y 
print(x ,"is larger than",y,":",a(x,y))
#######

#######
sum = 0
for i in range(1,6):
    num = int(input("enter number"))
    sum += num
    av = sum/5
print("the sum is",sum)
print("the average is ",av)
#######

######
n1 = int(input("enter number 1:"))
n2 = int(input("enter number 2:"))
n3 = int(input("enter number 3:"))
if (n1>n2 and n2>n3):
    print(n1, "is the largest")
    print("sorted order is :",n1,">",n2,">",n3)
elif (n1>n3 and n3>n2):
    print(n1, "is the largest")
    print("sorted order is :",n1,">",n3,">",n2)
elif (n2>n3 and n3>n1):
    print(n2, "is the largest")
    print("sorted order is :",n2,">",n3,">",n1)
elif (n2>n1 and n1>n3):
    print(n2, "is the largest")
    print("sorted order is :",n2,">",n1,">",n3)
elif (n3>n2 and n2>n1):
    print(n3, "is the largest")
    print("sorted order is :",n3,">",n2,">",n1)
elif (n3>n1 and n1>n2):
    print(n3, "is the largest")
    print("sorted order is :",n3,">",n1,">",n2)
elif (n1==n2 and n1>n3):
    print(n1,"is largest")
    print("sorted order is:",n1,"=",n2,">",n3)
elif (n1==n2 and n3>n1):
    print(n3,"is largest")
    print("sorted order is:",n3,">",n1,"=",n2)
elif (n1==n3 and n1>n2):
    print(n1,"is largest")
    print("sorted order is:",n1,"=",n3,">",n2)
elif (n1==n3 and n2>n1):
    print(n2,"is largest")
    print("sorted order is:",n2,">",n1,"=",n3)
elif (n2==n3 and n2>n1):
    print(n2,"is largest")
    print("sorted order is:",n2,"=",n3,">",n1)
elif (n2==n3 and n1>n2):
    print(n1,"is largest")
    print("sorted order is:",n1,">",n2,"=",n3)

else:
    print("all three are same")
######

#####
f = open('xyz.txt','w')
print("hi welcome",file = f)
f.close()

#@###
#####
num = int(input("enter number for the operation to be done:"))
a = int(input("enter number 1:"))
b = int(input("enter number 2:"))
if(num == 1):
    #a = int(input("enter number 1:"))
   # b = int(input("enter number 2:"))
    result = a+b
    print(result)
elif(num == 2):
    result = a-b
    print(result)
elif(num == 3):
    result = a*b
    print(result)
else:
    exit
######

######
name = input("name:")
batch = input("Batch: ")
f    = input("Father's name:")
m    = input("Mother's name:")
print(25*"-")
print("THE RESUME IS AS FOLLOWS")
print(25*"-")
print("Student's name:", name)
print("course:",batch)
print("father's name:",f)
print("mother's name:",m)
######

######
import math
def distance(x1,y1,x2,y2):
    return(math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)*1.0))

print("%.6f"%distance(23,23,44,44))
######

######
n = int(input())
t = n
s = 0
while (t >0):
    digit =t%10
    s+=digit**3
    t//=10
if (n==s):
    print("no is armstrong ")
else:
    print("no is not armstrong ")
######

######
lower = int(input("enter lower limit:"))
upper = int(input("enter upper limit:"))
for n in range(lower,upper+1):
    if n>1:
        for i in range(2,n):
            if (n%i==0):
                #print("number is not prime")
                break
        else:
            print(n)
######

#######
lower = int(input("enter lower limit:"))
upper = int(input("enter upper limit:"))
count = 0
for n in range(lower,upper+1):
    if n>1:
        for i in range(2,n):
            if (n%i==0):
                break
        else:
            print(n)
            count+=1
print(count)
#######

#####
num = int(input("enter number: "))
a = 0
b = 1
print(a)
print(b)
for i in range(1,num+1):
    c = a+b
    a = b
    b = c
    print(c)

#######

#########
num = int(input("enter number:"))
sum = 0
for i in range(1,num+1):
    sum+=i
print(sum)
#########

##########
num = int(input("enter number:"))
sum = 0
for i in range(1,num+1):
    sum+=i**3
print(sum)
###########

#####
n= int(input("enter number :"))
for i in range(0,n+1):
    #if i%2!=0:
        #print(i)
    if i%2==0:
        exit
    else:
        print(i)

#####
#####
list =[0,1]
num = int(input("enter number: "))
a = 0
b = 1
for i in range(1,num+1):
    c = a+b
    a = b
    b = c
    list.append(c)
print(list)
check = int(input("enter number to be checked:"))
if check in list:
    print("true")
else:
    print("false")
#####
#####
n = int(input())
li = []
for i in range(n):
    num = int(input("enter number:"))
    li.append(num)
print(li)
c = li[0]
li[0]=li[-1]
li[-1]=c
print("list after updation")
print(li)
######
######
n = int(input())
li = []
for i in range(n):
    num = int(input("enter number:"))
    li.append(num)
print(li)
li.sort()
print("second largest element is",li[-2])
#######

######
s = [1,2,3,4,5,6]
for i in range(0,6,2):
    print(s[i])
#####
#####
list1 = [1,2,3,4,5,6]
list2 = list1[-1:]+list1[:-1]
print(list2)

#####

#####
num = int(input())
list = []
for i in range(num):
    n = int(input("enter number:"))
    list.append(n)
print(list)
for j in range(0,n+1,2):
    print(list [j] )

#####

######
s = [1,2,3,4,5,6]
for i in range(0,6,2):
    print(s[i])
######

#####
def fact_N(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        n=n-1
    return f
l = int(input())
sum = 0
t = 1
for j in range(1,l+1):
    sum = sum+t/fact_N(t)
    t+=1
print(sum)
#####

#####
n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=n:
        print(n-i+1,end=" ")
        j = j+1
    print()
    i = i+1
#####

#####
n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=n:
        print(n-j+1,end=" ")
        j = j+1
    print()
    i = i+1
#####

######
n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=n:
        print(j,end = " ")
        j = j+1
    print()
    i = i+1
######

######
n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=n:
        print(i,end=" ")
        j = j+1
    print()
    i = i+1
    
######

######
n = int(input())
i = 1
while i<=n:
	j=1
	whilej<=i:
		print(j,end="")
		j=j+1
	print()
	i =i+1
######

####
n = int(input())
i = 1
while i<=n:
    j=1
    p=i
    while j<=i:
        print(p,end=" ")
        j=j+1
        
    print()
    i =i+1
####

#####
n = int(input())
i = 1
while i<=n:
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print()
    i =i+1
#####

########
l1=[]
l2=[]
l3=[]
li =[l1.append(int(input())),l2.append(int(input())),l3.append(int(input()))]
l4=[]
l5=[]
l6=[]
li1 =[l4.append(int(input())),l5.append(int(input())),l6.append(int(input()))]
l7=[]
l8=[]
l9=[]
li2 =[l7.append(int(input())),l8.append(int(input())),l9.append(int(input()))]
print(li)
print(li1)
print(li2)
#########

######
x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[9,8,7],[6,5,4],[3,2,1]]
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k]*y[k][j]
for r in result:
    print(r)
######

######
x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[9,8,7],[6,5,4],[3,2,1]]
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j]+y[i][j]
for r in result:
    print(r)
######

######
n = int(input())
l=[]
k = 0
for i in range(0,n):
    l.append(int(input()))
for i in range(len(l)):
    if (l[i]>k):
        k = l[i]
c = 0
for j in range(len(l)):
    if l[j]==k:
        c= c+1
print(c)
######

######
thislist = ["square","circle","triangle","octagon"]
if "triyangle" in thislist:
    print("yes!triangle is in the list")
else:
    print("no triangle here")
######

#####
def person(message,times = 1):
    print(message*times)
person("aman")
person("niya"*5)
######

######
x = 5
def func(x):
    print("x is",x)
    x = 20
    print("changed local x to",x)
func(x)
print("x is now",x)
##########

#######

r = int(input())
c = int(input())
matrix = []
for i in range(r):
    a =[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
​
#######
######
r = int(input())
c = int(input())
matrix = []
result   =[[0,0,0],
       [0,0,0],
       [0,0,0]]
for i in range(r):
    a =[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
#R = int(input())
#C = int(input())
Matrix = []
for i in range(R):
    A =[]
    for j in range(C):
        A.append(int(input()))
    Matrix.append(A)
for i in range(R):
    for j in range(C):
        print(Matrix[i][j],end=" ")
    print()
for i in range(len(matrix)):
    for j in range(len(Matrix[0])):
        result[i][j] = matrix[i][j] +Matrix[i][j]
for w in result:
               print(w)
    
    
######
PRINT :
I 
IN
IND
INDI
INDIA
USING SLICING
............

str = input()
l = len(str)
for i in range(l):
    s = str[0:i+1]
    print(s)
...............
###########

##########
str = " hello india"
str.replace("india","bharat")
str.find("india")
###########
3#####
str = input()
#for i in range(len(str)):
rev = str[::-1]
#print(rev)
if str == rev:
    print("string is palindrome")
else:
    print("string is not palindrome")
#####
#####
str = input()
for i in range(len(str)):
    l = str[1:i+1]+str[0]
print(l)


######
#####3
str = "INDIA"
l = str[1:5]+str[0]
print(l)

######
######
str = input()
rev = str[::-1]
for i in range(len(str)//2):
    print(str)
    print(rev)
######
        
######
str = input()
for i in range(len(str)):
    l = str[i]
    s = str[0]
    t = str[1:i]
print(l+t+s)
######

######
str= input()
for i in range(len(str)):
    l = str[1:i+1]+str[0]
print(l)
######
######
str = input()
rev = str[::-1]
print(rev)
######
#####
str = input()
for i in range(len(str)):
    l = str[i:]+str[:i]
    print(l)
#####
####
a = [[1,2,3],[2,4,5],[6,7,9]]
c1 = 0
c2 = 1
l = len(a)
temp = 0
for i in range(l):
    a[i][c1],a[i][c2] = a[i][c2],a[i][c1]
    print(a[i][:],end = " ")
    print()

####

####
a = [(10,20,40),(40,50,60),(70,80,90)]
list(a)
for i in range(len(a)):
    l = list(a[i])
    l[-1]= 100
    a[i ]= tuple(l)
print(a)
####

#####
a = [(),(),('',),('a','b'),('a','b','c'),('d')]
c = []
for i in a:
    b= list(i)
    if len(b)!=0:
        c.append(tuple(b))
print(c)

                  or
def remove(tuples):
    for i in tuples:
        if(len(i)==0):
            tuples.remove(i)
    return tuples
remove([(),(),('',),('a','b'),('a','b','c'),('d')])
#####

######
li = [('red','white','blue'),('green','pink','purple'),('orange','yellow','lime')]
for i in range(len(a)):
    l = list(li[i])
    if 'white' in l:
        print("True")
    if 'olive'  not in l:
        print("false")
        break
######
######
fruits = ["apple","banana","mango","orange"]
newlist = [x for x in fruits if "orange" in x]
print(newlist)
######

#####
def check_in_tuples(colours,c):
    result  = any(c in tu for tu in colours)
    return result
colours = [('red','white','blue'),('orange','yellow','pink'),('orange','lime','purple')]
print("original list:")
print(colours)
c1 = 'white'
print("\n check if",c1,"present in said tuples of tuples!")
print(check_in_tuples(colours, c1))
c1 = 'olive'
print("\n check if ",c1,"present in said tuples of tuples!")
print(check_in_tuples(colours ,c1))
#####

#####
tu  = (1,"abc",99)
t1 = list(tu)
t1[0] = "abc"
tu = tuple(t1)
print(tu)
#####

#####
l = int(input("enter number of nested list needed:"))
n = int(input("enter number of values needed:"))
li = []
t = []
for i in range(l):
    for j in range(n):
        t.append(input())
    li.append(t)
    t =[]
print(li)


#####
######
li = [(10,20,30),(40,50,60),(70,80,90)]
print([t[:-1]+(100,)for t in li])
######

#####
li = [1,2,4,9,0]
l  = [0,9,8,7,6]
l1 = []
for i in li:
    if i not in l:
        l1.append(i)
print(l1)
#####
#####
str = input()
for i in str:
    if ord(str>= ord('a')) or ord(str>= ord('A')) and ord(str<= ord('z')) or ord(str<= ord('z')):
        if len(set(str))==len(str):
            print("string is heterogram")
#####
#####
a = {1:"a",2:"b",3:"c"}
b = {1:"c",2:"v",4:"k"}
del(a[1])
print(a)
#####

#####
a = {1:"a",2:"b",3:"c"}
b = {1:"c",3:"v",4:"k"}
a.update(b)
print(a)
#####

#####
dict = {1:"january",2:"february",3:"march",4:"april",5:"may",6:"june",7:"july",8:"august",9:"september",10:"october",
       11:"november",12:"december"}

print(dict.keys())
print(dict.values())
#####
######
dict = {1:"january",2:"february",3:"march",4:"april",5:"may",6:"june",7:"july",8:"august",9:"september",10:"october",
       11:"november",12:"december"}

print(dict[1])
print(dict[6])
print(dict.get(1))
dict.get("sun",0)

######
######
dict = {"xyz" : 10,"abc":10,10:"k"}
dict['li']=[1,5,9]
print(dict)
######
https://bootcamp.cvn.columbia.edu/blog/python-projects-for-beginners-to-gain-skills/

N = int(input("ENTER THE SIZE OF LIST:"))
li = []
for i in range(N):
    n = int(input("ENTER VALUES OF THE LIST:"))
    li.append(n)
    n = int(input())
i = 1
while n>0:
    i = i*n
    n = n-1
    
print(i)
    
   li = [2,3,4,6]
li1 = []
for i in li:
    li1.append(i*i)
print(li1)
    
gender = input("MALE/FEMALE:")
salary = int(input("SALARY:"))
if gender == "FEMALE":
    bonus = (15/100*salary )+salary
    if salary<10000:
        bonus = bonus+(2.5/100*bonus)
if gender =="MALE":
    bonus = (10/100*salary )+salary
    if salary<10000:
        bonus = bonus+(2.5/100*bonus)
print(bonus)
    
#to reverse a list
l = [10,60,88,99,90]
l.reverse()
print(l)
print(l[::-1])

n = int(input("ENTER PASS CODE:"))
t = n
rev = 0
while t!=0:
    mod = t%10
    t = t//10
    rev = (rev*10)+mod
print(rev)
if rev == n:
    print("TRANSACTION MAY PROCEED")
else:
    print("TRANSACTION DECLINED")

#wap to print the sum of non-duplicate values of a list
li = [1,3,9,9,8,0,7,7]
sum = 0
s = set(li)
for i in s:
    sum+=i
print(sum)

#wap to print the sum of non-duplicate values of a dictionary
dict = {1,3,9,9,8,0,7,7}
sum = 0
s = set(li)
for i in s:
    sum+=i
print(sum)

#wap to print intersection of two sets
a = {1,1,2,4,9}
b = {5,9,8,6,9}
a.intersection(b)
a

#wap to insert element in set
set1 = {1,"set",4,5}
set1.add("hello")
set1

#wap to remove data value from set using pop fn.
set1 = {1,"set",4,5}
set1.pop()
set1

#wap to find union of two sets
set1 = {1,"set",4,5}
set2 = {2,3,4,5}
set1.union(set2)
set1

#wap to append two sets using update fn.
set1 = {1,"set",4,5}
set2 = {2,3,4,5}
set1.update(set2)
set1

#wap to find the factorial 
n = int(input())
product = 1
for i in range(1,n+1):
    product=product*i
print(product)
    OR
n = int(input())
product = 1
i = 1
while i<=n:
    product = product*i
    i = i+1
print(product)
import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Apple:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("blockcopy.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,25)*SIZE
        self.y = random.randint(1,20)*SIZE

class Snake:
    def __init__(self,parent_screen,length):
        self.parent_screen= parent_screen
        self.image = pygame.image.load("blockcopy.jpg").convert()
        self.direction = 'down'

        self.length = length
        self.x = [40]*length
        self.y = [40]*length

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill((168, 50, 86))

        for i in range(self.length):
            self.parent_screen.blit(self.image,(self.x[i],self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 600))
        self.snake = Snake(self.surface,5)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False
            self.play()
            time.sleep(.2)



if __name__ == '__main__':
    game = Game()
    game.run()


####
import random
s = [1,2,3,4,5,6]
random.choice(s)

#####
import random
dict ={1:2,2:3,4:5}
random.choice(dict)

#####
random.Random().random()

####
random.uniform(1,9)

####
random.randrange(0,100000000000000)

#####
for i in range(6):
    print(random.randrange(i,100,5))

####
import datetime
a = datetime.date(2019,2,1)
b = datetime.date(2019,3,1)
t = b-a
days = t.days
random_days= random.randrange(days)
random_date= a +datetime.timedelta(days = random_days)
print(random_date)

####
a = (0,100)
b = random.sample(a,10)
elements = (b,4)

#####
def ordered_binary_search(olist,item):
    if len(olist)==0:
        return False
    else:
        midpoint = len(olist)//2
        if olist[midpoint]==item:
            return True
        else:
            if item<olist[midpoint]:
                return binarysearch(olist[:midpoint],item)
            else:
                return binarysearch(olist[midpoint+1:],item)
    def binarysearch(alist,item):
        first = 0
        last = len(alist)
        found = False
        while first <=last and not found:
            midpoint = (first+last)//2
            if alist[midpoint]==item:
                found = False
            else:
                if item<alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
    return found
print(ordered_binary_search([0,1,2,5,4,8,24,35],3))
print(ordered_binary_search([0,1,3,28,9,3],3))

######
def selectionsort(array,size):
    for ind in range(size):
        min_index=ind
        for j in range(ind+1,size):
            if array[j]<array[min_index]:
                min_index = j
            array[ind],array[min_index] = array[min_index],array[ind]
arr = [-2,3,55,0,8,9,7]
size = len(arr)
selectionsort(arr,size)
print(arr)

#####
def mergesort(nlist):
    #print("splitting",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        
        mergesort(lefthalf)
        mergesort(righthalf)
        i = j = k = 0
        while j<len(righthalf):
            nlist[k]=righthalf[j]
            j = j+1
            k = k+1         
        while i<len(lefthalf):
            nlist[k]=lefthalf[i]
            i+=1
            k+=1
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                nlist[k] =lefthalf[i]
                i+=1
            else:
                nlist[k] = righthalf[j]
                j+=1
                k+=1
        #print("Merging ",nlist)
        
nlist=[int(x) for x in input().split()]
mergesort(nlist)
print(nlist)

                









    