# Q. 스택 자료구조로 초밥 접시를 계산하는 프로그램 작성하기
# 초밥 접시 가격을 입력받고, 0을 입력하면 접시 쌓기를 멈춤
# test03.py 코드 함수화 

print('[초밥 접시 계산하기]')

# 접시 가격 리스트
priceList = []

# 먹은 접시 쌓기
def stack_push(priceList, price):
    priceList.append(int(price))
    
# 맨 뒤부터 접시 계산하기
def stack_pop(priceList):
    # 접시 총가격
    global totalPrice
    totalPrice = 0
    calculatedPrice = priceList.pop()
    print('계산접시: ', calculatedPrice)
    totalPrice += calculatedPrice
    print('남은접시: ', priceList)
    
# --------------------------------------------- 실행
# 먹은 접시 쌓기 시작
while True:
    price = input('접시가격: ')
    if int(price) == 0:
        break
    stack_push(priceList, price)
print("쌓인접시: ", priceList)
print("\n")

# 접시 가격 계산하기
while True:
    if len(priceList) == 0:
        print('계산 완료')
        break
    stack_pop(priceList)
print('총 가격: ', totalPrice)