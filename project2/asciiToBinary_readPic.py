from def_decimalToBinary_int import decimalToBinary
from PIL import Image
import math

##open picture
image=Image.open("project2\Img_File.bmp")
path="project2\Output_BMP_binary.txt"
f=open(path,'a')

line_horizon=list()
imageList=list()
for i_vertical in range (image.height):
    line_horizon=[image.getpixel((i_horizon,i_vertical))for i_horizon in range(image.width)]
    for j in range(0,len(line_horizon)):
        str=''.join(decimalToBinary(line_horizon[j]))
        f.write(str)
    #end for
    str=''
image.close()
f.close()

# call def of another program
# decimalToBinary would return a list and input is a string
# image_horizon is a two dimensional list
toBinList=list()
for i in range(0,vertical_count):
    for j in range(0,horizon_count):
       toBinList.append(decimalToBinary(imageList[i][j]))


for i in range(0,len(toBinList)):
    tempList=toBinList[i]
    for j in range(0,len(tempList)):
        print(tempList[j],end="",file=f)
    # end for
#end for

# convert output bmp binary file into initial bmp file
path="project2\Output_BMP_binary.txt"
bmpBinary=list()
with open(path,'r') as f:
    for i in f:
       bmpBinary.append(i)

str="".join(bmpBinary)
bmpBinary=list()
for c in str:
     num=int(c)
     bmpBinary.append(c)
#end for

num=int(0)
#此時bmpBinary已經儲存圖片二進制
f=open("project2\Output_image.bmp",'w',encoding='UTF-8')
'''
for i in range(0,len(bmpBinary),8):
        j=int(0)
        sum=int(0)
        while(j<8):
                num=bmpBinary.pop(0)
                if(num=='1'):
                        sum+=int(math.pow(2,7-j))
                j+=1
        #end while
        print(chr(sum),end="",file=f)
     ##end for
'''

new_data = []
for i in range(0, len(bmpBinary), 8):
    new_data.append(bmpBinary[i:i+8])  # 8 digit binary list
int_data = [] 
for i in new_data:
    int_data.append(int(i,2))  # bytearray will convert decimal to hex
a= bytearray(int_data)
f.write(a)
f.close()  