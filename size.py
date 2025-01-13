from PIL import Image
import os


num=0
for i in range(0,500):
    try:
        img=Image.open("C:\\Users\\inaee\\Desktop\\MAKERS\\강아지크롤러\\SiberianHusky puppy\\"+str(i)+"_SiberianHuskypuppy.jpg")
        #print(str(i))
        img2=img.resize((200,200))
        print(str(i)+"사이즈변경")
        img2.save("C:\\Users\\inaee\\Desktop\\MAKERS\\강아지크롤러\\SiberianHuskyPuppy\\"+str(num)+"_SiberianHuskyPuppy.jpg")
        num=num+1
        print(str(i)+"사이즈변경완료")
    except:
        print(str(i)+"존재안함")
