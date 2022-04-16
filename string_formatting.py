def decimalToOctal(decimal):
    
    octal = 0
    i = 1
    while(decimal != 0):
        octal = octal +(decimal%8) * i
        decimal = int(decimal / 8)
        i = i * 10
        
    return octal

def decimalToHexa(decimal):
    
    return hex(decimal).replace("0x", "").upper()

def decimalToBinary(decimal):
    
    return bin(decimal).replace("0b", "")
    

def print_formatted(number):
    
    binLength = len(bin(number)[2:])
    
    # your code goes here
    for i in range(1, number+1):
        print("{} {} {} {}".format(str(i).rjust(binLength), str(decimalToOctal(i)).rjust(binLength), decimalToHexa(i).rjust(binLength), decimalToBinary(i).rjust(binLength)))

