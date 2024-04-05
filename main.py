# Add RegEx to verify IP and Mask
# from re import *

err=False

# Convert  decimal number into a string witch contains 8 bits, eight zeros and one, return it
def dTB(d):
    d = int(d) if type(d)==type("") else d
    if type(d)==type(0):
        bits=[128,64,32,16,8,4,2,1]
        aux=d
        bin=["0","0","0","0","0","0","0","0"]
        for i, bit in enumerate(bits):
            if aux>=bit:
                bin[i]="1"
                aux-=bit
            else:
                bin[i]="0"
        return "".join(bin)

# Convert binary into a decimal one, return it
def bTD(b):
    if type(b)==type("") and len(b)==8:
        bits=[128,64,32,16,8,4,2,1]
        d=0
        for i, c in enumerate(b):
            if c=="1":
                d+=bits[i]
        return d

try:
    ip = list(map(lambda n: int(n), input("IP (x.x.x.x): ").split(".")))
except:
    print("Ocorreu algum erro com endereço ip inserido")
    err=True


try:
    mask = list(map(lambda n: int(n), input("Mask (x.x.x.x): ").split(".")))
except:
    print("Ocorreu algum erro com a máscara de ip inserida")
    err=True


if not err:
    print("Prosseguir")