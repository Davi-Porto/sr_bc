# Add RegEx to verify IP and Mask
# from re import *

# Convert  decimal number into a string witch contains 8 bits, eight zeros and one, return it
def dTB(d):
    d = int(d) if type(d)==type("") else d
    if type(d)==type(0):
        aux=d
        bin=[]
        for i in range(7,-1,-1):
            if aux>=2**i:
                bin.append("1")
                aux-=2**i
            else:
                bin.append("0")
        return "".join(bin)

# Convert binary into a decimal one, return it
def bTD(b):
    if type(b)==type("") and len(b)==8:
        d=0
        for i, c in enumerate(b):
            if c=="1":
                d+=2**(7-i)
        return d

# Logic AND between two bits, return 0 or 1 based on result
def andB(a, b):
    return str(int(a) and int(b))

# Join list elements using a separator, return new string
def join(l, sep=""):
    result=""
    l=list(map(lambda n: str(n), l))
    for i, item in enumerate(l):
        result+=item+sep if not i==len(l)-1 else item
    return result


def c32oct(str):
    l=[]
    for v in range(1,5):
        l.append(bTD(str[(v-1)*8:v*8]))
    return join(l, ".")

# Main-line of code
def main():
    try:
        # # Tests (Comment if not testing)
        # ip = [192, 168, 0, 4]
        # mask = [255, 255, 255, 0]
        
        ip = list(map(lambda n: int(n), input("IP (x.x.x.x): ").split(".")))
        mask = list(map(lambda n: int(n), input("Mask (x.x.x.x): ").split(".")))
        
        # Subnet:
        
        # Ip to binary
        # Mask to binary
        # Logical AND with them
        # Subnet to decimal
        
        # IP to binary:
        ipBinary = "".join(list(map(dTB, ip)))
        
        # Mask to binary
        maskBinary = "".join(list(map(dTB, mask)))
        
        # Logical AND with them
        srBin=""
        for i in range(32):
            srBin+=andB(ipBinary[i], maskBinary[i])
        
        # Subnet to decimal
        subnet=c32oct(srBin)
        
        
        # Broadcast:
        
        # Subnet to binary
        # Mask to binary, invert it
        # Logical sum with them chars
        # Broadcast to decimal
        
        # Subnet to binary:
        # Already exists in srBin
        
        # Mask to binary, invert it
        # Just invert it:
        maskBinaryInverted = join(list(map(lambda c: "1" if c=="0" else "0", maskBinary)))
        
        # Logical sum with them chars:
        broadcastBin=""
        for i, c in enumerate(maskBinaryInverted):
            broadcastBin+=str(int(c)+int(srBin[i]))
        
        # Broadcast to decimal
        broadcast = c32oct(broadcastBin)
        
        
        print("Subnet:",subnet)
        print("Broadcast:", broadcast)
    except:
        print("\nAn erro has occurred with this values")

main()