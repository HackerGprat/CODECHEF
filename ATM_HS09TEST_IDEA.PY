import os

saving_ac = []
current_ac = []

def clear():
    if os.name == 'nt':     # nt for windows
        os.system('cls')    
    else:   # posix for linux and mac
        os.system('clear')


def first():
    
    print("".center(50,'='))
    print("Wellcome to the bank of rbi atm".upper().center(50,' '))
    print("".center(50,'-'))

    print("\nCautions:")
    print("Never share your atm pin with anyone\n".title())
    
    print("".center(50,'-'))
    print("press any key to continue...".upper().center(50,' '))
    print("".center(50,'='))
    input("")

    
def second():
    print("".center(50,'='))
    print("choose any one".upper().center(50,' '))
    print("".center(50,'-'))
    
    options = "1) Deposit\t\t2) withdraw \n\n3) mini statement\t4) a/c details".upper()
    print(options)    
    
    print("".center(50,'-'))
    print("press the number".upper().center(50,' '))
    print("".center(50,'='))
    
    response = int(input("I want : "))
    if response == 1:
        clear()
        deposit()
    elif response == 2:
        print("Withdraw")
    elif response == 3:
        print("Mini Statement")
    elif response == 4:
        print("A/c Details")

def deposit():
    print("".center(50,'='))
    print("deposit account".upper().center(50,' '))
    print("".center(50,'-'))

    options = "1) saving a/c\t\t2) current a/c ".upper()
    print(options) 
    
    response = int(input("I want : "))
    if response == 1:
        print("saving account")
    elif response == 2:
        print("current account")
        
        
def withdraw():
    pass

if __name__ == "__main__":
    first()
    clear()
    second()
    