# stack_push(스택 변수, 접시 가격) 함수 정의
def stack_push(stack, price): # 함수 선언(정의)
    stack.append(price)
    
# stack_pop(스택 변수) 함수 정의
# 스택변수 길이가 0이면 "없음" 반환, 스택변수 마지막 데이터 삭제(pop)하여 반환
def stack_pop(stack):
    if len(stack) == 0:
        return '없음'
    return stack.pop()

print("[초밥 접시 계산하기]")

# 초밥 접시 리스트
stack = [] 

# 총 가격
totalPrice = 0

# 스택 자료구조 리스트로 초기화
while True:
    price = input('접시가격 : ')
    price = int(price)
    if price == 0:
        break
    stack_push(stack, price) #함수 호출

print('쌓인 접시 : ', stack)
print()

while True:
    pop_data = stack_pop(stack)
    if pop_data == '없음':
        break
    totalPrice += int(pop_data)
    print('계산접시 : ', pop_data)
    print('남은접시 : ', stack)

print('계산 완료')
print('총 가격 : ', totalPrice)