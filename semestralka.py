# No libraries were used

# InputData reads binary input from the user.
def InputData():
    data = input()
    s = {'0','1'}
    d = set(data)

    if s == d or d == {'0'} or d == {'1'}:
        return data
    else:
        print("Input must be a binary value...")
        InputData()

# Reads the degree of the generating polynomial from user
def inputDegree():
    while True:
        degree = input()
        if (degree.isnumeric()) and (int(degree) > 0):
            return degree
        else:
            print("Only values between <1,100> are accepted.")

# Binary XOR of two binary numbers represented as string
def xor(a, b):
    ans = []
 
    for i in range(1, len(b)):
        if a[i] == b[i]:
            ans.append('0')
        else:
            ans.append('1')
 
    return ''.join(ans)

# Binary division of number divideMe by the divider
def division(divideMe, divider):

    if len(divideMe) >= len(divider):
        divLen = len(divider)

        tmp = divideMe[0 : divLen]
        while divLen < len(divideMe):
            if tmp[0] == '1':
                tmp = xor(divider, tmp) + divideMe[divLen]
    
            else: 
                tmp = xor('0'*divLen, tmp) + divideMe[divLen]
    
            divLen += 1
        
        if tmp[0] == '1':
            tmp = xor(divider, tmp)
        else:
            tmp = xor('0'*divLen, tmp)

        remainder = tmp
        return remainder
    else:
        return divideMe

# CRC Encoding 
def encode(data, key):
    keyLen = len(key)
    dataAppended = data + '0'*(keyLen-1)
    remainder = division(dataAppended,key)
    codeword = data + remainder
    return codeword

# CRC Decoding
def decode(data,key):
    remainder = division(data,key)
    return remainder

# Checking for errors in data
def dataOkay(data):
    d = set(data)

    if d == {'0'}:
        return True
    else:
        return False

# Prints data as a polynomial
def printData(data):
    prevExists = False

    for i in range(len(data)):
        if data[i] == '1' and prevExists == False:
            if i == (len(data) - 1):
                print("1")
            print("x^%d" % ( (len(data) - 1) - i), end='')
            prevExists = True

        elif i == (len(data) - 1) and data[i] == '1':
            print(" + 1")

        elif data[i] == '1':
            print(" + x^%d" % ( (len(data) - 1) - i), end='')
            prevExists = True

# Finds position of the error
def findError(data, remainder, key):
    degree = len(data)

    for i in range((degree), 0, -1):
        position = '1'
        position = position + '0'*(degree-i)
        if len(position) < (len(key) - 1):
            position = ((len(key) - 1) - len(position))*'0' + position

        if division(position,key) == remainder:
            return (i)

    return False

# Implementation of product() method from itertools. Generates all permutations of given length
def product(*args, repeat = 1):

    pools = [list(pool) for pool in args] * repeat
    result = [[]]

    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield list(prod) 

# Creates all polynomials of a given degree, returns them as a list of lists
def gpCandidatesList(degree):

    gp_list = list(product('01', repeat = int(degree)))

    for gp in range(len(gp_list)):
        gp_list[gp].insert(0,'1')
        gp_list[gp] = ''.join(gp_list[gp])

    return gp_list

# Returns all possible generating polynomials of a given degree from gpCandidatesList
def choose_gp(gen_pol_candidates, dataLen, degree):
    gen_pols = []
    divideMe = "1" + (dataLen + int(degree) - 1)*"0" + "1"

    for gp in range(len(gen_pol_candidates)):
        remainder = division(divideMe,gen_pol_candidates[gp])
        if remainder == int(degree)*"0":
            gen_pols.append(gen_pol_candidates[gp])

    return gen_pols

# Corrects error in binary data at a given index
def dataCorrection(data, errorIndex):
    correctedData = data
    if correctedData[errorIndex] == '0':
        correctedData = correctedData[:errorIndex] + '1' + correctedData[errorIndex + 1:]
    else:
        correctedData = correctedData[:errorIndex] + '0' + correctedData[errorIndex + 1:]

    return correctedData

#---------LOADING DATA FROM USER------------------
print("Enter binary data to encrypt: ", end='')
dataToEncrypt = InputData()

print("Enter the degree of the generating polynomial: ", end='')
degree = inputDegree()
#---------CREATE GENERATING POLYNOMIALS-----------
gen_pol_candidates = gpCandidatesList(degree)
gen_pols = choose_gp(gen_pol_candidates, len(dataToEncrypt), degree)

print("Generating polynomials of %d. degree: " %int(degree))
for gp in range(len(gen_pols)):
    print("%d. " %gp, end='')
    printData(gen_pols[gp])

#---------CHOOSE ONE GENERATING POLYNOMIAL--------
print("Choose one by entering its sequence number <0,%d>: " %( len(gen_pols) - 1 ), end='')
choice = int(input())
key = gen_pols[choice]

#---------ENCODING DATA---------------------------
encodedData = encode(dataToEncrypt, key)
print("Encoded data: ", encodedData)
print("Encoded data as a polynomial: ", end='')
printData(encodedData)

#---------RECEIVED DATA FROM USER-----------------
print("")
print("Enter received data in binary:", end='')
receivedData = InputData()
print("The received data as a polynomial: ")
printData(receivedData)

#---------CHECKING FOR ERRORS AND CORRECTION------
remainder = decode(receivedData, key)
if dataOkay(remainder) == True:
    print("")
    print("Data has been received without any errors.")
else:
    print("")
    print("Oops, there was an error in the data!")

if findError(receivedData, remainder, key) != False:

    errorIndex = findError(receivedData, remainder, key)
    print("The error was found at digit number(from the left): ", errorIndex)

    correctedData = dataCorrection(receivedData, errorIndex-1)
    print("Corrected data: ", correctedData)
    print("Corrected data as a polynomial: ", end='')
    printData(correctedData)

else:
    print("Multiple errors or input code was not a hamming code.")
