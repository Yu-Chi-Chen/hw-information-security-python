import string
import math

## read file
f=open("project2\testFile.txt","r")
word=f.read()
contList=list(word)
print(contList)
f.close()

## change ascii(decimal) to binary
def decimalToBinary(c:string):
    num=ord(c)
    divisor=0
    divisor=int(divisor)
    arrList=list()
    arrList.clear()

    dividend=num
    while(dividend/2!=0):
            divisor+=1
            dividend/=2
    ## end while

    while(divisor>=0):
            if(num>=pow(2,divisor)):
                num-=pow(2,divisor)
                divisor-=1
                arrList.append(1)
            else:
                divisor-=1
                arrList.append(0)
            ##end if-else

    ## end while

    while(len(arrList)<8):
            arrList.insert(0,0)
    ## end while
    
    print(arrList)


for i in range(0,len(contList)):
  decimalToBinary(contList[i])
  print(" ")
## end for