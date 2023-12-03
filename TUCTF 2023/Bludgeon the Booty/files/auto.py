
testdict=[]

# 百位
for k in range(11):
    # 十位
    for j in range(11):
        # 个位
        for i in range(11):
            testdict.append('send "1\\r"\n')
            testdict.append('send "3\\r"\n')
            testdict.append('send "+\\r"\n')
        testdict.append('send "1\\r"\n')
        testdict.append('send "2\\r"\n')
        testdict.append('send "+\\r"\n')
    testdict.append('send "1\\r"\n')
    testdict.append('send "1\\r"\n')
    testdict.append('send "+\\r"\n')


with open("auto.exp", "w",encoding="utf8") as file:
    file.write('#!/usr/bin/expect -f\n')
    file.write('spawn nc chal.tuctf.com 30002\n')
    file.writelines(testdict)
    file.write('send "exit\\r"\n')
    file.write('expect eof\n')
