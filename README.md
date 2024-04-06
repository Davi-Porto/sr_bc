# Get Subnet and Broadcast

## Resume

Return the Subnet and Broadcast based at IP and MASK.

## Language
1. Python. (v3.12.0)

## Logic

* ## Subnet
  1 - Convert each octet in IP to binary; <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Sem título](https://github.com/Davi-Porto/sr_bc/assets/135801787/7420df54-644a-4340-b9a1-1af7da5c2a12)<br><br>
  2 - Convert each octet in MASK to binary;  <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Sem título1](https://github.com/Davi-Porto/sr_bc/assets/135801787/e2f6aa2b-916c-4939-b870-a4fcbd86e48c)<br><br>
  3 - Logical AND with them, each bit; <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Sem título2](https://github.com/Davi-Porto/sr_bc/assets/135801787/77c684bc-622e-4af5-897f-3368bad3b506)<br><br>
  4 - Convert to decimal, return is the Subnet. <br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Sem título3](https://github.com/Davi-Porto/sr_bc/assets/135801787/415bd70a-b2e3-4e4a-86b8-65d0ba8b7eb3) <br>
 
* ## Broadcast
  1 - Convert Subnet to binary; <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/Davi-Porto/sr_bc/assets/135801787/ffe5f3f5-22ea-4d77-a4ca-0d3f1a579609)<br><br>
  2 - Convert MASK to binary; <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Sem título1](https://github.com/Davi-Porto/sr_bc/assets/135801787/e2f6aa2b-916c-4939-b870-a4fcbd86e48c)<br><br>
  3 - Invert each char in binary mask, where is 0 change to 1 and vice-versa; <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/Davi-Porto/sr_bc/assets/135801787/3be881a0-8800-419a-aea4-7b61dafde554)<br><br>
  4 - Sum between each char of them; <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/Davi-Porto/sr_bc/assets/135801787/10baf0d5-4152-4e6a-9bb4-2bd5a55d7ec8)<br><br>
  5 - Convert to decimal, return is the Broadcast.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![image](https://github.com/Davi-Porto/sr_bc/assets/135801787/0d31b2c4-b7f7-4c9f-9ebe-691ee56dd08a)<br>
