import string
import math

## read file
f=None
try:
     f=open("project2\Txt_File .txt","r")
     word=f.read()
     contList=list(word)
except IOError:
     print("Error can't find file")
     if f:
          f.close()
finally:
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

    path='project2\Output.txt'
    f=open(path,'a')
    for i in range(0,len(arrList)):
        print(arrList[i],end="",file=f)

    f.close()
    

for i in range(0,len(contList)):
  decimalToBinary(contList[i])
## end for

##-----------start to turn output file into origin file-----------------
f=None
storeList=list()
try:
     f=open('project2\Output.txt','r')
     for c in f:
        storeList.append(c)
     ##end for
except:
     print("Error can't find file")
     if f:
        f.close()
finally:
     f.close()

str="".join(storeList)
storeList=list()
for c in str:
     num=int(c)
     storeList.append(c)
     
##此時storeList已經一個一個數字儲存Output File
f=open("project2\Output_textFile.txt",'a')
for i in range(0,len(storeList),8):
        j=int(0)
        sum=int(0)
        while(j<8):
                num=storeList.pop(0)
                if(num=='1'):
                        sum+=int(math.pow(2,7-j))
                j+=1
        #end while
        print(chr(sum),end="",file=f)
     ##end for
     
f.close()     

