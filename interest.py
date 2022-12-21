# Author: Oladapo Okikiola
money = input("Enter amount to invest: $")
interest_rate = input("Enter the interest rate: ")
money = float(money)
interest_rate = float(interest_rate) * .01
for i in range(10):
    money = money + (money * interest_rate)
    print("Investment after 10 years : {:.2f}".format(money))
    break
