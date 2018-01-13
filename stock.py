while True :

    print("초기 잔액을 입력해주세요.")
    money = float(input())

    print("보유 기간을 입력해주세요.")
    period = float(input())

    print("연평균 수익률을 입력해주세요.")
    interest = float(input())


    money = money*((1 + interest/100)**period)

    print("최종 금액은 " + format(money, ",") + " 입니다.")
