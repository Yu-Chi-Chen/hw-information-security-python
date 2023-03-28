from PIL import Image
##open picture
image=Image.open("project2\Img_File.bmp")
##顯示L表示灰階->顯示P代表RGB
print(image.mode)
line_horizon=list()

for i_vertical in range (image.height):
    line_horizon=[image.getpixel((i_horizon,i_vertical))for i_horizon in range(image.width)]
    print(*line_horizon)

image.close()
