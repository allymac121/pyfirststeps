#declare variables

loanamount = 0
interestRate = 0
loanperiodinyears = 0
monthlyinstallment = 0
numberofpayments = 0

#get the variables frm the user in string format

loanamount = float(input("How much money did you borrow ?: "))
interestRate = float(input("how much interest is to be charged on this loan?: "))
loanperiodinyears = float(input("how loan is your payment period,in years ?: "))

#get your total number of payments 

numberofpayments = loanperiodinyears * loanperiodinyears

#calculate the actual monthly payments

monthlyinstallment = loanamount * interestRate * (1+ interestRate) * numberofpayments \
    / ((1 + interestRate)* numberofpayments - 1)

#print your results

print("your monthly installments will be ksh. %2f" % monthlyinstallment)