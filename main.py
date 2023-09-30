from PIL import Image, ImageDraw
import os

input_link = input("請輸入資料夾位址:")
link_list = os.listdir(input_link)

count = 0
total_file_count = len(link_list)

for file_name in link_list:

    text = '轉換進度: ' + str(count) + ' /' + str(total_file_count)
    print(text, end="\r")

    bg = Image.new("RGB", (1920, 1920), color = (255, 255, 255))
    drew = ImageDraw.Draw(bg)

    full_link = input_link + "\\" + file_name
    ft = Image.open(full_link)

    if ft.size[0] > ft.size[1]:
        #橫
        
        ft = ft.resize((1920, int(ft.size[1] * 1920 / ft.size[0])))
        bg.paste(ft, (0, 960 - int(ft.size[1] / 2)))

        bg.save('output\\' + file_name + ".jpg")

        count += 1
        # print(str(count) + '/' + str(total_file_count), flush=True)

    else:
        #直

        ft = ft.resize((int(ft.size[0] * 1920 / ft.size[1]), 1920))
        bg.paste(ft, (960 - int(ft.size[0] / 2), 0))

        bg.save('output\\' + file_name + ".jpg")

        count += 1
        # print(str(count) + '/' + str(total_file_count), flush=True)


print('完成，共計 ' + str(count) + '個檔案')