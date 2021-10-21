
# ! Question
# Ram would like to withdraw ** amount from atm
# accept if withdraw amount is multiple of 5
# make sure enough balance on his account
# bank changes for each transaction will be 0.5
# ? calculate the account balace of ram after transaction

# todo example
# input : 30 120.00 # first is withdrawal amount, second is current balance
# output : 89.50 # now he have after transaction sucessfull

# Solution

w_amount, balance = map( float, input().split() )

if ( w_amount % 5 == 0 )  and ( w_amount <= ( balance - 0.5 ) ):
    
    print( ( balance - 0.5 ) - w_amount )
    
else:
    print( balance )
    