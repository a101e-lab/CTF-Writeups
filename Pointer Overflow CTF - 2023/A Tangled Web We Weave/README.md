# A Tangled Web We Weave

> reverse

## 题目描述

The flag has been hidden in these assembly instructions, except I forgot how to decode it... If you figure it out you get the flag.

## 解题思路

题目文件是一段汇编文本，大致逻辑是把一段加密的字符串逐个与某个数字异或得到原文，但是这个数字未给出。直接暴力破解即可

## exp

```python
encoded_message = [
    0x0F, 0x10, 0x1C, 0x0B, 0x19, 0x04, 0x0A, 0x08,
    0x0C, 0x0F, 0x20, 0x14, 0x4E, 0x11, 0x46, 0x20,
    0x14, 0x4F, 0x11, 0x46, 0x20, 0x46, 0x4F, 0x48,
    0x20, 0x11, 0x4F, 0x48, 0x17, 0x4E, 0x11, 0x46,
    0x20, 0x4F, 0x11, 0x20, 0x12, 0x4C, 0x02
]

for xor_key in range(0, 255):
    # 对编码的消息进行解码
    decoded_message = [byte ^ xor_key for byte in encoded_message]
    # 将解码后的消息转换成字符串
    decoded_string = ''.join([chr(byte) for byte in decoded_message])
    # 如果字符串每一位都是可打印字符，那么就打印出来
    if all([ord(char) >= 32 and ord(char) <= 126 for char in decoded_string]):
        print(decoded_string)
```

## flag

`poctf{uwsp_k1n9_k0n9_907_n07h1n9_0n_m3}`