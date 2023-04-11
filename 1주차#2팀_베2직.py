#Python
#1
a=[1,5,8,2,4,9]

a[2]=0
a[3]=0

print(a)

#2
i=int(input())
sum=0
if i <=100:
    for a in range(i+1):
        sum=sum+a
    print(sum)

#3
num_1 = input("정수를 입력하시오")
want = list(map(int, num_1.split()))
list.sort(want)
for i in range(0,len(want), 2):
    want[i] = str(want[i])
print(want)

#4
num_1 = input("정수를 입력하시오")
want = list(map(int, num_1.split()))
list.sort(want)
for i in range(1,len(want), 1):
    want[i]
print(want)

#5
fruitdb = [['사과', 1020], ['오렌지', 880], ['포도', 3160]]
print(fruitdb[2], fruitdb[0][0])

#6
fruits = {'사과', '오렌지', '포도'}
print('사과' in fruits)
print('메론' in fruits)

#7
training_data = [['연두', 3, '사과'], ['노랑', 3, '사과'], ['빨강', 2, '포도'], ['빨강', 1, '포도'], ['노랑', 3, '레몬']]
sum_apple = 0
sum_grape = 0
sum_lemon = 0
for i in range(5):
    if '사과' in training_data[i]:
        sum_apple += 1
    elif '포도' in training_data[i]:
        sum_grape += 1
    else:
        sum_lemon += 1
print("'사과': ", sum_apple, ", '포도': ", sum_grape, ", '레몬': ", sum_lemon)

#8
def solution(str1, str2):
    answer = 0
    if str2 in str1:
        return str1.replace(str2,"")
d=solution('abcdef','f')
print(d)

#9
divisor = []

def solution(n):
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    list.sort(divisor)
    print(divisor)

solution(7)

#10
M=int(input())
N=int(input())
arr=[]

for i in range(M,N+1):
    if i==1:
        pass
    elif i==2:
        arr.append(i)
    else:
        for j in range(2, i):
            if i%j==0:
                break
            elif j==i-1:
                arr.append(i)
if len(arr)==0:
    print('-1')
else:
    print(sum(arr))
    print(min(arr))


#R
#1
x<-c(4,6,5,7,10,9,4,15)

#2
rep(1,5)
rep(2,5)

#3
A <- c(2, 12, 5, 6, 3, 31, 35, 13, 5, 5, 7, 72)
m <- matrix(A, ncol=3, byrow = TRUE)
m

#4
name <- c("kim","lee","park","Oh")
sex <- c('f','m','f','m')
income <- c(100,102,300,204)
df <- data.frame(성명=name, 성별=sex, 수입=income)
df

#5
x <- c(34, 56, 55, 87, NA, 4, 77, NA, 21, NA, 39)
is.na(x)
sum(is.na(x))

#6
x <- c(1,5,1,3,5,7,5)
unique(x)

#7
data()
head(iris,5)
