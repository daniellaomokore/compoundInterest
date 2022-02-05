
#This program shows the user their saving account interest after yesr 1, 2 and 3

#"{:.2f}".format() <<<< used to format value to 2d.p

class compoundInterest:

 interestRate=0.04



 deposit = float(input("Enter your saving account deposit amount £:"))
 print("You have deposited £" + "{:.2f}".format(deposit))



 year1Interest= deposit * interestRate
 year1balance=deposit +year1Interest
 limit_float =round (year1balance,2)
 print("Your balance after 1 year will be £:" + "{:.2f}".format(year1balance))



 year2Interest = year1balance * interestRate
 year2balance = year1balance +year2Interest
 limit_float =round (year2balance,2)
 print("Your balance after 2 years is £:" + "{:.2f}".format(year2balance))



 year3Interest = year2balance * interestRate
 year3balance = year2balance +year3Interest
 limit_float =round (year3balance,2)
 print("Your balance after 3 years will be £" + "{:.2f}".format(year3balance))


 
