def encode(pswd):
    encoded_pswd = ""
    for i in range(len(pswd)):
        if(int(pswd[i])>=7):
            encoded_pswd+= str(int(pswd[i])+3)[1]
        else:
            encoded_pswd+= str(int(pswd[i])+3)
    return encoded_pswd

def main():
    pswd = "00009962"
    print(encode(pswd))
if __name__ == '__main__':
    main()
