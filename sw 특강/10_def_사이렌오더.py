'''
작성일 : 2023년 6월 16일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
사이렌 오더를 통해 음료를 미리 예약하는 프로그램을 만드시오.
메뉴는
1. 아메리카노 2500원
2. 카페라떼 3000원
3. 바닐라 라떼 3000원입니다
메뉴 번호를 선택하면 해당 메뉴와 가격을 출력해 주는 부분을 함수로 작성하시오.

선택한 메뉴는 인수로 전달되어 가격이 결과 값으로 반환되는 함수로 작성하시오.

사용자가 음료를 선택하면 음료의 가격을 알려주는 프로그램
'''
def menu(num):
    if dmafy == '아메리카노' :
        return "아메리카노를 주문하였습니다.\n가격은 2500원입니다"
    elif dmafy == '카폐라떼' :
        return "카폐라떼를 주문하였습니다.\n가격은 3000원입니다"
    elif dmafy == '바닐라라떼' :
        return "바닐라라떼를 주문하였습니다.\n가격은 3000원입니다"
    elif dmafy == '우마리카노' :
        return "우마리카노를 주문하였습니다.\n3일 이내에 완성될 에정입니다.\n음료 섭취는 무조건 원샷입니다^^\n가격은 섭취 후 정해주세요!"
    else :
        return "말씀하신 음료는 저희가게에서 팔지 않습니다."
        
while True :
    print("음료 주문")
    print("메뉴 : 아메리카노, 카페라떼, 바닐라 라떼 가 있습니다.")
    dmafy = input("어떤 음료를 주문하시겠습니까? : ")
    if dmafy == 'z' :
        break
    print('\n', menu(dmafy), '\n')


