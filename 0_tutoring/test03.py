# Q. 스택 자료구조로 초밥 접시를 계산하는 프로그램 작성하기

print('[초밥 접시 계산하기]')

# 초밥 접시 가격을 입력받고, 0을 입력하면 접시 쌓기를 멈춤
# 접시 가격 리스트
priceList = []

# 먹은 접시 쌓기
while True:
    price = input('접시가격: ')
    if int(price) == 0:
        break
    priceList.append(int(price))
print("쌓인접시: ", priceList)
print("\n")

# 맨 뒤부터 접시 계산하기
totalPrice = 0

while True:
    if len(priceList) == 0:
        print('계산 완료')
        break
    # totalPrice += priceList.pop()
    priceList.pop()
    # calculatedPrice = priceList.pop()
    print('계산접시: ')
    # totalPrice += calculatedPrice
    print('남은접시: ', priceList)

print('총 가격: ', totalPrice)