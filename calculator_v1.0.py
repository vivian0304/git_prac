print("-Calculator v1.0-")
while 1 :
	global result
	if result == 0 :
		result = int(input("주연산자(수)를 입력하세요."))
	else :
		print(result)
	unResult = result

	sign = input("부호를 입력하세요. ! 를 입력하면 종료합니다.")
	if sign == '!' :
		break
	try :
		num = int(input("피연산자(수)를 입력하세요."))
	except :
		print("입력이 잘못되었습니다.")

	if sign == '+' :
		add(num)
		print(unResult," ",sign," ",num," = ",result)

	elif sign == '-' :
		sub(num)
		print(unResult," ",sign," ",num," = ",result)