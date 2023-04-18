from def_decimalToBinary_int import decimalToBinary
from PIL import Image
import numpy as np
import PIL

'''
##open picture
image=Image.open()
path=
 #px is a two dimension list

'''

with Image.open("project2/Img_File.bmp") as img:
    img = img.convert('L')
    img_array = np.array(img)  # create two dimension matrix
    # img_matrix=img_array.tolist()
# close image
f = open("project2/Output_BMP_binary.txt", 'w')
i_vertical, i_horizon = img_array.shape
line_horizon = list()
imageList = list()
line = list()

for vertical in range(0, i_vertical):
    for horizon in range(0, i_horizon):
        pixelData = img_array[vertical, horizon]
        dataBinary = decimalToBinary(pixelData)
        for element in dataBinary:
            print(element, end='', file=f)
        # end for
    # end for
# end for
f.close()


'''    for horizon in range(line):
        str="".join(decimalToBinary(str(line[vertical])))
        print(str,end="")'''
# end for
# end for

'''
for i_vertical in range (image.height):
    line_horizon=[image.getpixel((i_horizon,i_vertical))for i_horizon in range(image.width)]
    print(len(line_horizon))
    for j in range(0,len(line_horizon)):
        str=''.join(decimalToBinary(line_horizon[j]))
        #f.write(str)
        print(j,line_horizon[0],len(line_horizon))
    #end for
    str=''
image.close()
f.close()
'''

# call def of another program
# decimalToBinary would return a list and input is a string
# image_horizon is a two dimensional list
'''
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
'''

# convert output bmp binary file into initial bmp file
path = "project2/Output_BMP_binary.txt"
with open(path, 'r') as f:
    bmpBinary = f.read()

str = "".join(bmpBinary)
bmpBinary = list()

for c in str:
    num = int(c)
    bmpBinary.append(num)
# end for

num = int(0)
# 此時bmpBinary已經儲存圖片二進制
arr = np.asarray(bmpBinary)
OutputImg = PIL.Image.fromarray(np.uint8(arr))
OutputImg.save("Output_image.bmp")
# f=open("project2\Output_image.bmp",'w')
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
'''
