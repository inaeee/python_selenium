#필수 패키지 가져오기
import cv2
import numpy as np


dogname="BorderCollieAdult"

num=2
#for i in range(2,510):
#img파일 가져오기
path="C:\\Users\\inaee\\Desktop\\MAKERS\\Dog\\REAL\\BorderCollieadult\\14_BorderCollieadult.jpg"
image=cv2.imread(path)
print(image)
print("가져옴")

#크기설정
y=13
x=8
h=163
w=169
print("원본: ",image.shape[0],image.shape[1]) # len(image) = height크기, len(image[0]) = weight크기
img_cut = image[y:y+h, x:x+w]  # y값부터 설정하게됨. (image의 y는 y~y+h 까지, x는 x~x+w 까지)
print("잘라낸것 : ", len(img_cut), len(img_cut[0]))  # len(image) = height크기, len(image[0]) = weight크기
cv2.imshow("Input", image)     # 원본이미지 출력
cv2.imshow("Output", img_cut)  # 바꾼이미지 출력

# 지정한 영역 잘라서 resize하기
if(w-x > 200 and h-y > 200):
    if(w-x > 200):
        fixX = round(200/(w-x), 2)  # 자리수 2자리로 제한
        print("x가 200보다 큼")
        fix = fixX
    else:
        fixY = round(200/(h-y), 2)  # 자리수 2자리로 제한
        print("y가 200보다 큼")
        if(fixX < fixY):
            fix = fixY
    
    print("%.2lf"%(fix))
    img_cut = cv2.resize(img_cut, None, fx=fix, fy=fix, interpolation=cv2.INTER_AREA)
    y,x,h,w = (0,0,len(img_cut),len(img_cut[0]))
    cv2.imshow("Output2", img_cut)  # 바꾼이미지 출력
    print("잘라서 200밑으로 만든것 : ",len(img_cut), len(img_cut[0]))

# y, x, h, w 를 내가 지정한 영역 size로 지정
y,x,h,w = (0,0,len(img_cut),len(img_cut[0]))

# 그림 주변에 검은색으로 칠하기
w_x = (200-(w-x))/2
h_y = (200-(h-y))/2

if(w_x < 0):
    w_x = 0
elif(h_y < 0):
    h_y = 0
    
print("%d, %d"%(w_x, h_y))
M = np.float32([[1,0,w_x], [0,1,h_y]])  #(2*3 이차원 행렬)
M2 = np.float32([[1,0,0], [0,1,0]])
img_re2_ori = cv2.warpAffine(img_cut, M2, (200, 200))
img_re2 = cv2.warpAffine(img_cut, M, (200, 200))

# 그림 배경을 늘리기...
img_re3 = cv2.copyMakeBorder(img_cut, 100, 100, 100, 100, cv2.BORDER_REPLICATE)

cv2.imshow("img_re2", img_re2)
#cv2.imshow("img_re2_ori", img_re2_ori)

# 이미지 저장하기
cv2.imwrite("C:\\Users\\inaee\\Desktop\\MAKERS\\Dog\\PADDING\\BorderCollieAdult_size\\"+dogname+"_14.jpg",img_re2)
#num=num+1
print("완료")
