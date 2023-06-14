'''
continue
'''
# 리스트의 값 10개 중에서 10보다 큰 수를 출력하시오.
numbers = [5,12,25,28,84,1,4,97,55,77]

print("리스트 값 중 10보다 큰 수 - 반복문 사용")

for i in numbers :
    if i >= 10 :
        print(i, end=', ')
        
print()

print("리스트 값 중 10보다 큰 수 - continue 사용")
for i in numbers :
    if i < 10 :
        continue
    print(i, end=', ')
    
print()

# 1~30 사이의 수 중에서 7의 배수만 출력허시오. - continue 사용 
for i in range(1,31) :
    if i % 7 != 0 :
        continue
    print(i, end=' ')
