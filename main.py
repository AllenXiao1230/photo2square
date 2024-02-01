
from PIL import Image, ImageDraw
import os

output_size = (1920, 1920) #(X, Y)

color = input("選擇背景顏色:\n1. 黑色\n2. 白色\n")
if color == "2":
    bg_color = (255, 255, 255)
else:
    bg_color = (0, 0, 0)

input_link = input("請輸入資料夾位址:")
link_list = os.listdir(input_link)

count = 0
total_file_count = len(link_list)

for file_name in link_list:

    text = '轉換進度: ' + str(count) + ' /' + str(total_file_count)
    print(text, end="\r")

    bg = Image.new("RGB", output_size, color = bg_color)
    drew = ImageDraw.Draw(bg)

    full_link = input_link + "\\" + file_name
    ft = Image.open(full_link)

    if ft.size[0] > ft.size[1]:
        #橫
        
        ft = ft.resize((output_size[0], int(ft.size[1] * output_size[0] / ft.size[0])))
        bg.paste(ft, (0, int(output_size[1] / 2) - int(ft.size[1] / 2)))

        bg.save('C:\\Allen\\photo2square\\output\\' + file_name )

        count += 1
        

    else:
        #直

        ft = ft.resize((int(ft.size[0] * output_size[1] / ft.size[1]), output_size[1]))
        bg.paste(ft, (int(output_size[0] / 2) - int(ft.size[0] / 2), 0))

        bg.save('C:\\Allen\\photo2square\\output\\' + file_name )

        count += 1
        


print('完成，共計 ' + str(count) + '個檔案')