'''
작성일 : 2023년 6월 16일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
랜덤으로 10명의 학생의 키와 몸무게 생성하여 파일에 저장
'''
import random

f_name = list('김이엄천박최윤문')
s_name = list('가나다라마바사아자차타파하')

with open("info.txt","w") as file :
    for i in range(10) :
        name = random.choice(f_name) + random.choice(s_name) + random.choice(s_name)
        weight = random.randint(40,100)
        height = random.randint(140,250)
        
        file.write("{},{},{}\n".format(name,weight,height))