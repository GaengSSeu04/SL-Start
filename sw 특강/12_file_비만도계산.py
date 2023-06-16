'''
작성일 : 2023년 6월 16일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
키와 몸무게로 비만도 계산하기
'''
with open("info.txt", "r") as file :
    for line in file :          # strip() 공백제거, split(",") 구분자
        (name, weight, height) = line.strip().split(",")
        
        if (not name) or (not weight) or (not height) :
            continue
        
        # 비만도 계산하기
        bmi = int(weight) / ((int(height) / 100) ** 2)
        if bmi >= 25 :
            result = "과제중"
        if bmi >= 18.5 :
            result = "정상 체중"
        else :
            result = "저체중"
            
        print("\n".join([
            "이름 : {}",
            "몸무게 : {}",
            "키 : {}",
            "BMI : {:.2f}",
            "결과 : {}"]).format(name, weight, height, bmi, result))
        print()