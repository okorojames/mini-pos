ussd = "*565#"
numOne = "1"
numTwo = "2"
numThree = "3"
balAmount = 130000
yourName = str(input("What is Your Name? "))
if yourName == "":
    print("You can't proceed with empty info. ")
else:
    putUssd = str(input(f"Please {yourName}, put \n Input The USSD: "))
    if putUssd == ussd:
        option = str(input(f"{yourName}, select from the followinf options: \n1: Deposit\n2: Withdraw\n3: Check Balance"))