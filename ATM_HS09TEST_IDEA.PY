import os



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


if __name__ == "__main__":
    first()
    clear()
    