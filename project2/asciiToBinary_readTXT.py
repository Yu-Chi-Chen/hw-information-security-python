import string
import math

## read file
f=open("project2\Txt_File .txt","r")
word=f.read()
contList=list(word)
f.close()

## change ascii(decimal) to binary
def decimalToBinary(c:string):
    num=ord(c)
    divisor=0
    arrList=list()
    arrList.clear()

    dividend=num
    ## 沒有寫floor會出錯
    while(dividend/2!=0):
            divisor+=1
            dividend=math.floor(dividend/2)
    ## end while

    while(divisor>=0):
            if(num>=math.pow(2,divisor)):
                num-=math.pow(2,divisor)
                divisor-=1
                arrList.append('1')
            else:
                divisor-=1
                arrList.append('0')
            ##end if-else
    ## end while


    while(len(arrList)<8):
            arrList.insert(0,0)
    ## end while

    for i in range(0,len(arrList)):
        print(arrList[i],end="")
    

for i in range(0,len(contList)):
  decimalToBinary(contList[i])
## end for