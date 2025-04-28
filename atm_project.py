
def pull_money(amount_of_money):
    print("how much money do you want to withdraw?")
    how_much_to_withdraw= int(input())
    change_in_the_bunk= amount_of_money- how_much_to_withdraw
    return change_in_the_bunk, how_much_to_withdraw
def add_money(amount_of_money):
    print("how much money do you want to add?")
    how_much_to_add= int(input())
    change_in_the_bunk= amount_of_money+ how_much_to_add
    return change_in_the_bunk, how_much_to_add

#inputs
name_of_user= input("write your full name")
while( not name_of_user.isalpha()):## what to do with te
    name_of_user = input("write your full name, just in letters")
amount_of_money= int(input("what is the amount of money that you have? in Shekels"))
while( not amount_of_money<100000):##רקורסיה
    amount_of_money = int(input("insert the real amount in shekels"))
## ATM actions
print("what do you want to do?"
      " 1- withdraw money"
      " 2- add money"
      " 3- exit")
what_action= int(input())
if(what_action==1):## withdraw money
    corrent_amount_in_account, withdraw_from_the_bunk = pull_money(amount_of_money)
    print("the corrent amount in the bank is"+ str(corrent_amount_in_account))
    print("the money that you draw was"+ str(withdraw_from_the_bunk))
if(what_action==2):
    corrent_amount_in_account, add_from_the_bunk = add_money(amount_of_money)
    print("the corrent amount in the bank is"+ str(corrent_amount_in_account))
    print("the money that you added was"+ str(add_from_the_bunk))
else:
    print("have a good day!")



