#SUM OF ALL 1

list=[10,20,30,40,50,100]
sum=0
for i in list:
    sum+=i
print("sum :",sum)

#LARGEST NUMBER 2

list=[10,20,30,40,50,100]
largest=0
for i in list:
    if i>largest:
        largest=i
print("largest",i)

#SMALLEST NUMBER 3

list=[10,20,30,40,50,100]
small=list[0]
for i in list:
    if i<small:
        small=i
print("smallest :",small)


#REMOVE DOPLICATE ELEMENT 4

list=[10,20,30,100,40,50,100]
a=[]
for i in list:
    if i not in a:
        a.append(i)
print(a)


#COPY LIST 5

list=[10,20,30,40,50,100]
list2=[]
for i in list:
    list2.append(i)
print(list2)


#REVERSE LIST 6

list=[10,20,30,40,50,100]
for i in range(len(list)-1,-1,-1):
    print(list[i],end=" ")
    

#LIST WITH DIFFERENT DATA TYPES 7
    
list=[10,20,"saravanan",True,4.7]
for i in list:
    print(i,end=" ")
    

#REMOVE EMPTY ELEMENT 8
    
list=[10,20,"",True,4.7]
for i in list:
    if i !="":
        print(i,end=" ")
        


#APPEND SECOND LIST OF FIRST LIST 9
        
list1=[10,20,"",True,4.7]
list2=[10,20,30,40,50,100]
for i in list2:
       list1.append(i)
print(list1)


#RANDOM ITEM 10

import random
a=[10,20,30,40,50]
print(random.choice(items))



#ODD AND EVEN 11

a=int(input("enter the value :"))
if a in [2,4,6,8,10]:    
    print("even")
elif a in [1,3,5,7,9,11]:
    print("odd")
else:
    print("not suported")
    
        

#ASCENDING ORDER 12


a=[5,6,8,4,3,2,1]
a.sort()
print(a)


#DESCENDING ORDER 13

a=[5,6,8,4,3,2,1]
a.sort(reverse=True)
print(a)


#COUNT ELEMENT 14

a=[10,20,30,40,50]
print(len(a))


#AVERAGE 15

a=[10,20,30,40,50]
average=sum(a)/ len(a)
print(average)



#OCCURRENCE OF ELEMENT 16

a=[10,20,30,40,50]
print(a.count(20))



#CHECK ELEMENT 17

a=[10,20,30,40,50]
if 20 in a:
    print("found")
else:
    print("not found")
    


#INSERT ELEMENT 18
a=[10,20,30,40,50]
a.insert(1,35)
print(a)


#REMOVE ELEMENT 19

a=[10,20,30,40,50]
a.remove(20)
print(a)


#SECOND LARGEST NUMBER 20

a=[10,20,30,40,50]
a.sort()
print(a[-2])


#MERGE TWO LIST 21

A=[1,2,3]
B=[4,5,6]
result=A+B
print(result)



#COMMON ELEMENT 22

a=[1,2,3]
b=[4,5,3]
common=[]
for i in a:
    if i in b:
        common.append(i)
print(common)


#OPSITIVE NUMBER 23

a=[-1,-2,-3,4,5]
for i in a:
    if i>0:
        print(i,end=" ")
        
    
#REPLACE ALL NEGATIVE 24

a=[5,2,3,4,1]
for i in range(len(a)):
    if a[i]<0:
        a[i]=0
print(a)
    

#INDEX POSITION ELEMENT 25

a=[5,2,3,4,1]
print(a.index(3))


#STUDENT NAME ORDER 26

list=["saro","saravanan","vishal","gokul"]
for i in list:
    print(i,end=", ")
    
    
#HIGHEST AND LOWEST 27
    
mark=[50,40,20,90,55,66,77]
print(max(mark))
print(min(mark))


#CALCULATE THE TOTAL BILL 28

price=[50,70,60,40,20]
print("total bill=",sum(price))



#SALARY GREATER THEN $25000 29

salary=[18000,26000,25000]
for i in salary:
    if i>25000:
        print(i)

       
#PERSENT AND ABSENT COUNT 30

attendance=["persent","absent","persent","absent","persent"]
count=attendance.count("persent")
print("persent students =",count)

