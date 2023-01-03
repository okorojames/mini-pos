from time import sleep
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
        option = str(input(f"{yourName}, select from the following options: \n1: Deposit\n2: Withdraw\n3: Check Balance\n  "))
        #
        #
        if option == numOne:
            depoAmount = int(input(f"Please Enter Amount: ")) 
            print('Please wait...')
            sleep(5)
            print(f'Transaction successful\nNew bal is: {balAmount + depoAmount}')
        # 
        # 
    elif putUssd == "":
        print(f"{yourName}, You can't submit and empty option.")
    else:
        print(f"{yourName}, Please, this does\'nt look like a valid code.")