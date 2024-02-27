# Write a program to accept Account Number, Name, balance of account holder.
# Calculate interest as following:
# if balance >= 2,50,000 interest rate is 3.97%
# if balance >= 2,00,000 interest rate is 3.73%
# if balance >= 1,50,000 interest rate is 3.33%
# else interest is 2.59%
# Display Account no, Name, Balance and interest amount.
# Take input age if age >= 65 then add 1% extra interest 

account_number = int(input("Enter Account no: "))
account_name = input("Enter Account holder name: ")
account_balance= float(input("Enter Account Balance: "))
account_holder_age= int(input("Enter Age of account holder: "))

if account_holder_age >=65 :
    if account_balance >= 2500000 :
        interest_amount = account_balance * 0.0497
    elif account_balance >= 200000 :
        interest_amount = account_balance * 0.0473
    elif account_balance >= 150000 :
        interest_amount = account_balance * 0.0433
    else :
        interest_amount = account_balance * 0.0359
else :
    if account_balance >= 2500000 :
        interest_amount = account_balance * 0.0397
    elif account_balance >= 200000 :
        interest_amount = account_balance * 0.0373
    elif account_balance >= 150000 :
        interest_amount = account_balance * 0.0333
    else :
        interest_amount = account_balance * 0.0259

print("The Account Number is : ", account_number)
print("The Account holder name is : ",account_name)
print("The Account Balance is : ",account_balance)
print("The interest amount is : ",interest_amount)