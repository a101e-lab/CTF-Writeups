import hashlib
import itertools
from string import digits, ascii_letters, punctuation
alpha_bet=digits+ascii_letters+punctuation
strlist = itertools.product(alpha_bet, repeat=4)

sha256="5ccd4cda1dc33d20a072cddf2cf921c865b274da912edb7ac3f157404c3fe4e3"
tail="uLBLoFfDko5h5uA9"

xxxx=''

for i in strlist:
    data=i[0]+i[1]+i[2]+i[3]
    data_sha=hashlib.sha256((data+str(tail)).encode()).hexdigest()
    if(data_sha==str(sha256)):
        xxxx=data
        break

print(xxxx)