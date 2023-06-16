'''
작성일 : 2023년 6월 16일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
사전 : 키와 값으로 이루어 짐.
'''
list1 = [[1, '하나'],[2, '둘'],[3, '셋']]
dict1 = dict(list1)

print("리스트 : ", list1)
print("사전 : ", dict1)

# 사전 생성
dict2 = {'제목' : '어벤저스 엔드게임', '장르' : '히어로 무비'}
print("영화 : ", dict2)

# 특정 키의 값을 출력
# 키 값은 리스트의 [] 사용, dict2('제목') => 오류 발생.
print("영화 제목 : ", dict2['제목'])
print("영화 장르 : ", dict2['장르'])

# 영화 감독 이름 추가 - 딕셔너리 내부 값에 리스트로 자료 추가
print("딕셔너리에 요소 추가")
dict2['감독'] = ['안소니 루소', '조 루소']
print("영화 : ", dict2)

# 출연진 추가
dict2['출연진'] = ['토르', '헐크','아이언맨','블랙팬서','캡틴 아메리카','리카르도','빌리','deep dark Fantage']
print("영화 : ", dict2)
print("영화 출연진 : ", dict2['출연진'])

# 장르 변경
dict2['장르'] = 'SF'
print("영화 : ", dict2)

# 다음 코드의 결과를 작성하시오.
dict2['출연진'][1] = '타노스'
print("영화 출연진 : ", dict2['출연진'])

print("특별 캐스팅 : ", dict2['출연진'][1])

# 출연진 삭제
del dict2['출연진']
print("영화 : ", dict2)

# 빈 사전 생성
student = {}
print("학생 추가 전 : ", student)

student['학과'] = '컴퓨터공학부'
student['학번'] = '202395003'
student['이름'] = '김경현'

print("학생 추가 후 : ", student)

# 딕셔너리에 키가 있는지 확인 
key = input("찾고 싳은 키 입력 : ")
if key in student :
    student(student[key])
else :
    print("존재하지 않는 키 입니다!")
