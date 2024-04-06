# Get Subnet and Broadcast

## Resume

With IP and MASK, return Subnet and Broadcast.

## Language
1. Python (v3.12.0)

## Logic

* ### Subnet
  
  1 - Convert each octet in IP to binary; <br>
  2 - Convert each octet in MASK to binary; <br>
  3 - Logical AND with them, each bit; <br>
  4 - Convert to decimal, return is the Subnet.

* ### Broadcast

  1 - Convert Subnet to binary; <br>
  2 - Convert MASK to binary; <br>
  3 - Invert each char in binary mask, where is 0 change to 1 and vice-versa; <br>
  4 - Sum between each char of them; <br>
  5 - Convert to decimal, return is the Broadcast.
