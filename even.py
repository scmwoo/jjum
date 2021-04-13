# 짝수
def isEven(num):
    if num % 2 == 1:
        abc = "홀수"
    else:
        abc = "짝수"

    print(abc)

kwy = int(input(" 숫자를 입력하세요 : "))
isEven(kwy)
