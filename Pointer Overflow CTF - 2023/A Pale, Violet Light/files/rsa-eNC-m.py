import libnum
from Crypto.Util.number import long_to_bytes
 
c_origin ="933969 15848125 24252056 5387227 5511551 10881790 3267174 14500698 28242580 933969 32093017 18035208 2594090 2594090 9122397 21290815 15930721 4502231 5173234 21290815 23241728 2594090 21290815 18035208 10891227 15930721 202434 202434 21290815 5511551 202434 4502231 5173234 25243036"

c_list=c_origin.split(" ")
n = 34034827

e = 5039

q = 5807
p = 5861
 
d = libnum.invmod(e, (p - 1) * (q - 1))
res=""
for i in range(len(c_list)):
    c=int(c_list[i])
    m = pow(c, d, n)   # m 的十进制形式
    string = chr(m)  # m明文
    res+=string
    print(res)