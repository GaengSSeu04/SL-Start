'''
작성일 : 2023년 6월 16일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
학생 정보를 사전에 저장하고,
특정 학생의 정보(학번)를 입력하여 학생을 찾아주세요.

[알고리즘]
1. 학생 정보 저장 사전 만들기 - 빈 사전 만들기
2. 학생 정보 입력 - 사전에 저장 (z 키를 누르면 종료 - 무한반복)
3. 학번으로 검색하여 학생 찾기 (학번이 빈칸이면 검색 종료 - 무한 반복)
'''
student = {}

while True :
    gkrqjs = input("학번 입력 : ")
    if gkrqjs == 'z' :
        break
    dlfma = input("이름 입력 : ")
    student[gkrqjs] = dlfma

print("학생 검색")
while True :
    gkrqjs = input("학번 입력 : ")
    if gkrqjs == '' :
        break
    print("학생 : ", student[gkrqjs])
    
    






