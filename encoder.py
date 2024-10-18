# Yat Yeung
def encode(pswd):
    encoded_pswd = ""
    for i in range(len(pswd)):
        if(int(pswd[i])>=7):
            encoded_pswd+= str(int(pswd[i])+3)[1]
        else:
            encoded_pswd+= str(int(pswd[i])+3)
    return encoded_pswd
def decode (pswd):
    pass

def main():
    encoded_pswd=""
    while True:
        option=input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option:")
        if(option=="1"):
            encoded_pswd=encode(input("Please enter your password to encode:"))
            print("Your password has been encoded and stored!")
        if(option=="2"):
            decoded_pswd=decode(encoded_pswd)
            print(f"The encoded password is {encoded_pswd}, and the original password is {decoded_pswd} .")
        if(option=="3"):
            break

if __name__ == '__main__':
    main()
