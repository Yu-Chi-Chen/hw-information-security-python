import math

def decimalToBinary(num:int):
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

    if __name__=='_main_':
        return arrList
    
    return arrList
##end define