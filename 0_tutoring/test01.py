# Q. 문자열의 알파벳, 숫자, 스페이스 개수를 출력하는 프로그램 작성하기
# 튜티 코드

# 사용자 정의함수(매개변수 x, 반환값x) 정의
statement = input('문자열 입력: ')
alpha = 0
digit = 0
space = 0

for a in statement:
    if a.isalpha():
        alpha += 1
    elif a.isdigit():
        digit += 1
    elif a.isspace():
        space += 1 

# 딕셔너리 자료형 정의
mydic = {'알파벳': alpha, '숫자': digit, '스페이스': space}

# 입력, 함수 호출, 출력
print(mydic)
print('알파벳 개수: ', alpha)
print('숫자 개수: ', digit)
print('스페이스 개수: ', space)
