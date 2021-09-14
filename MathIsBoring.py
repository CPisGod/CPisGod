################################
import random
################################

def Loot(N): #루트
    return float(N ** 0.5)

def twice(N): #제곱
    return float(N ** 2)

def twice2(a, b): #제곱근
    return (float(a ** b))

def plus(a, b): #덧셈
    return (float(a + b))

def minus(a, b): #뺄셈
    return float(a - b)

def multipl(a, b): #곱셈
    return float(a * b)

def division(a, b): #나눗셈
    return (float(a / b))

def down(N): #내림
    return float(N // 1)

def up(N): #올림
    return float((N // 1) + 1)

def updown(N): #반올림
    if N + 0.5 < (N // 1) + 1: # 5.60 < 6
        return float(N // 1)
    elif N + 0.5 >= (N // 1) + 1: # 6.1 > 6
        return float((N // 1) + 1)
    else: return None

def Pytha(a, b): #피타고라스정리
    c2 = a ** 2 + b ** 2
    return float(c2 ** 0.5)

for i in range(1,101):
    print(" ")
choose = False
while not choose:
    a = int(input("****주의****\n1 : 10억자리 숫자 미만, 너무 복잡한 숫자는 제외 바랍니다.\n2 : 2개의 숫자가 필요한 수식에는 기호 없이 띄어쓰기만 합니다.\n하는 방법 : 하고 싶은 기호의 숫자를 누르세요\n1. 덧셈\n2. 뺄셈\n3. 곱셈\n4. 나눗셈\n5. 반올림\n6. 루트\n7. 제곱\n8. 제곱근\n9. 피타고라스정리\n>> "))
    if a == 1:
        choose = True
        b, c = map(float, input("예) 1 5로 숫자를 입력하세요\n>> ").split())
        print("답 :", plus(b, c))
    elif a == 2:
        choose = True
        b, c = map(float, input("예) 1 5로 숫자를 입력하세요\n>> ").split())
        print("답 :", minus(b, c))
    elif a == 3:
        choose = True
        b, c = map(float, input("예) 1 5로 숫자를 입력하세요\n>> ").split())
        print("답 :", multipl(b, c))
    elif a == 4:
        choose = True
        b, c = map(float, input("예) 1 5로 숫자를 입력하세요\n>> ").split())
        print("답 :", division(b, c))
    elif a == 5:
        choose = True
        b = float(input("예) 5로 숫자를 입력하세요 >> "))
        print("답 :", updown(b))
    elif a == 6:
        choose = True
        b = float(input("예) 5로 숫자를 입력하세요 >> "))
        print("답 :", Loot(b))
    elif a == 7:
        choose = True
        b = float(input("예) 5로 숫자를 입력하세요 >> "))
        print("답 :", twice(b))
    elif a == 8:
        choose = True
        b, c = map(float, input("예) 1 5로 숫자를 입력하세요 (첫번째 숫자는 밑, 두번째 숫자는 지수) >> ").split())
        print("답 :", twice2(b, c))
    elif a == 9:
        choose = True
        b, c = map(float, input("예) 1 5로 숫자를 입력하세요 >> ").split())
        print("답 :", Pytha(b, c))
    else:
        for i in range(1,101):
            print(" ")
        print("옳지 않은 답입니다. 다시 입력 바랍니다")