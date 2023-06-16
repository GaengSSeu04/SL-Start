'''
작성일 : 2023년 6월 14일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현

숫자 추측 게임 만들기

[문제 분석]
사용자가 입력한 값과 컴퓨터가 생성한 랜덤 값을 비교한다.
몇번만에 맞혔는지 알려준다.

사용자에게 힌트를 준다.
사용자가 입력한 값이 랜덤값 보다 크면 숫자는 작다라고 한다.
사용자가 입력한 값이 랜덤값 보다 작으면 숫자는 크다라고 한다.

사용자가 값을 입력하여 힌트를 받을 떄 마다 count 를 증가한다.
'''
import random

num = random.randint(1,30)  #랜덤 변수 저장
count = 0 
while True:
    tkfka = int(input("컴퓨터가 1부터 30까지 중 몇번을 골랐을까요? : "))
    
    if tkfka > 30 or tkfka < 1 :
        print("범위 안에 있는 숫자로 다시 입력해주세요")
    
    elif tkfka > num :
        print("컴퓨터는 당신의 숫자 {}보다 작게 생각했습니다.".format(tkfka))
        count = count + 1
    elif tkfka < num :
        print("컴퓨터는 당신의 숫자 {}보다 높게 생각했습니다.".format(tkfka))
        count = count + 1
    elif tkfka == num :
        print("당신은 {}번의 시도 끝에 컴퓨터가 생각해낸 숫자 {}를 맞췄습니다!".format(count,num))
        
        break
