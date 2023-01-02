ussd = "*565#"
numOne = "1"
numTwo = "2"
yourName = str(input("What is Your Name? "))
if yourName == "":
    print("You can't proceed with empty info. ")
else:
    putUssd = str(input(f"Please {yourName}, put \n Input The USSD: "))
