from def_decimalToBinary_int import decimalToBinary
from PIL import Image
##open picture
image=Image.open("project2\Img_File.bmp")
##顯示L表示灰階->顯示P代表RGB
print(image.mode)
line_horizon=list()
imageList=list()
for i_vertical in range (image.height):
    line_horizon=[image.getpixel((i_horizon,i_vertical))for i_horizon in range(image.width)]
    # print(*line_horizon)
    imageList.append(line_horizon)

horizon_count=image.width
vertical_count=image.height
image.close()

# call def of another program
# decimalToBinary would return a list and input is a string
# image_horizon is a two dimensional list
toBinList=list()
for i in range(0,vertical_count):
    for j in range(0,horizon_count):
       toBinList.append(decimalToBinary(imageList[i][j]))

path="project2\Output_BMP_binary.txt"
f=open(path,'a')
for i in range(0,len(toBinList)):
    tempList=toBinList[i]
    for j in range(0,len(tempList)):
        print(tempList[j],end="",file=f)

    

