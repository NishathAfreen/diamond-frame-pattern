n=int(input())
x=(n*2)-1
x1=x-1
#To be clear this is for whole upper half
for i in range(x,0,-1):
   for j in range(i): 
          print("*",end=" ")
   for k in range(0,2*(x-i)):
          print(" ",end=" ")
   for l in range(i,0,-1):
         print("*",end=" ")
   print()
#this is for whole lower half
for i in range(0,x):
     for j in range(0,i+1):
            print("*",end=" ")
     for k in range(2*(x1-i),0,-1): 
            print(" ",end=" ")
     for l in range(0,i+1):
            print("*",end=" ")
     print()
