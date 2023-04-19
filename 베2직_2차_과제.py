#연습 문제 1
#넘파이를 사용하여 다음과 같은 행렬을 만든다.
#10 20 30 40 50 60 70 80

import numpy as np
x=np.array([10,20,30,40,50,60,70,80])
print(x)

#또 다른 풀이 식
import numpy as np
x=np.arange(10, 81, 10)
print(x)

#연습 문제 2
#이 행렬에서 값 7 을 인덱싱한다.
#이 행렬에서 값 14 을 인덱싱한다.
#이 행렬에서 배열 [6, 7] 을 슬라이싱한다.
#이 행렬에서 배열 [7, 12] 을 슬라이싱한다.
#이 행렬에서 배열 [[3, 4], [8, 9]] 을 슬라이싱한다

m = np.array([[ 0, 1, 2, 3, 4], [ 5, 6, 7, 8, 9], [10, 11, 12, 13, 14]])
#1
m[1,2]
#2
m[2,-1]
#3
m[1,1:3]
#4
m[1:3, 2]
#5
m[0:2, 3:5]

#연습문제3 numpy이용해서 bmi 구하기
#21이하 > 저체중
#21초과 24미만 > 정상
#24이상 > 비만
#bmi_level 배열에 저장

import numpy as np
height = np.array([173, 168, 171, 189, 179])
weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi=weight/(height*height)*10000
bmi_level=[]

for di in bmi:
    if di<=21:
        bmi_level.append('저체중')
    elif di <24:
        bmi_level.append('정상')
    elif di >=24:
        bmi_level.append('비만')
bmi_level