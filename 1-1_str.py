# calculate
First_number = int(input("덧셈을 할 첫번째 숫자 : "))
Second_number = int(input("덧셈을 할 두번째 숫자 : "))

result = First_number + Second_number

## input data를 int로 넣었는데 print할 때, 문자열과 같이 추출을 해야하기 때문에 str로 감싸서 문자열로 변환해줘서 출력
# print(str(First_number) + "와 " + str(Second_number) + "를 더하면 " + str(result) + "입니다.")

## 문자열 포멧 코드 사용
print(" ")
print("="*20)
print("문자열 포멧 코드 사용")
print("="*20)
print("%d와 %d를 더하면 %d입니다" %(First_number, Second_number, result))


## formating 방법 (제일 최신 버전)
print(" ")
print("="*20)
print("Formating 사용")
print("="*20)
Answer = f"{First_number}와 {Second_number}를 더하면 {result}가 됩니다."
print(Answer)
