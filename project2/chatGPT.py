'''
import os

# 读取 bmp 文件并转换为二进制码
with open('./project2/Img_File.bmp', 'rb') as f:
    bmp_bytes = f.read()
    bmp_binary = ''.join(format(byte, '08b') for byte in bmp_bytes)


# 写入二进制码到文本文件
with open('./project2/chatGPTOutputTXT.txt', 'w') as f:
    f.write(bmp_binary)

# 从文本文件中读取二进制码并转换为 bmp 文件
with open('./project2/Output.txt', 'r') as f:
    bmp_binary = f.read()

    # 将二进制码转换回 bmp 文件
    if bmp_binary[28:30] == '01':  # 判断是否为 8 位灰度 BMP 格式
        bmp_bytes = bytearray(int(bmp_binary[i:i+8], 2) for i in range(128, len(bmp_binary), 8))
        bmp_header = bmp_bytes[:128]
    elif bmp_binary[28:30] == '11':  # 判断是否为 24 位彩色 BMP 格式
        bmp_bytes = bytearray(int(bmp_binary[i:i+8], 2) for i in range(54, len(bmp_binary), 8))
        bmp_header = bmp_bytes[:54]
    else:
        raise ValueError('Invalid BMP format')

    # 保存为 bmp 文件
    with open('./project2/chatGPTOutput.bmp', 'wb',encoding='UTF-8' ) as outfile:
        outfile.write(bmp_header + bmp_bytes)

# 打开生成的 bmp 文件，检查是否与原始文件相同
os.system('open ./project2/Output.bmp')

'''
from PIL import Image

# 讀取 BMP 檔案，轉換為二進制碼，並輸出到 Output.txt 中
with Image.open('project2\Img_File.bmp') as img:
    # 轉換為 8 位灰度 BMP 檔案
    img = img.convert('L')
    # 取得 BMP 檔頭
    header = img.tobytes()[:54]
    # 取得 BMP 檔像素資料，轉換為二進制碼
    pixels = img.tobytes()[54:]
    count=int(0)
    for byte in pixels: count+=1
    binary_pixels = ''.join('{:08b}'.format(byte) for byte in pixels)
    # 將二進制碼輸出到 Output.txt 中
    with open('project2\Output_BMP_binary.txt', 'w') as f:
        f.write(binary_pixels)
        print(count)

# 從 Output.txt 中讀取二進制碼，轉換為 BMP 檔案
with open('project2\Output_BMP_binary.txt', 'r') as f:
    binary_pixels = f.read()
    # 取得 BMP 檔像素資料，將二進制碼轉換為 bytes
    pixels = bytes(int(binary_pixels[i:i+8], 2) for i in range(0, len(binary_pixels), 8))
    # 將 BMP 檔頭和像素資料合併為 BMP 檔案
    img_data = header + pixels
    # 將 BMP 檔案寫入磁碟
    with open('project2\Output_image.bmp', 'wb') as f:
        f.write(img_data)
