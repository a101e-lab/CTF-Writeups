# 010101

## 题目


[1703213552288727081a42a07511eea54300163e0447d0.zip](./files/1703213552288727081a42a07511eea54300163e0447d0.zip)

## 考点

- `crypto`
- `SHA256`
- `RSA`

## WriteUp

- 分析代码逻辑：
  - `proof`：
    - 随机生成一个字符串`random_str`
    - 计算字符串的哈希值`str_sha256`
    - 给出`random_str[4:]`和`str_sha256`，让用户计算`random_str[:4]`
    - 如果用户给定的`random_str[:4]`和`random_str[4:]`的哈希值相同，则验证通过
  - getPQN：
    - 随机生成两个大素数`p`和`q`，满足以下要求：`p.bit_length() == 2048 and q.bit_length() == 2048 and (p*q).bit_length() == 4096`
    - `return p, q, n`
  - `encrypt`：
    - 通过`getPQN`生成`p`和`q`和`n`
    - 计算密文`c = pow(m, e, n)`
    - 对`p`进行变换：前1024位随机挑选一个1变成0，后1024位随机挑选一位变成1，得到`fake_p`
    - `return n, fake_p, c`
  - `handle`：   
    - 通过`proof`函数判断用户输入的`XXXX`和`random_str[4:]`的哈希值是否相同         
    - 相同的话，通过`encrypt`函数对`flag`进行加密，返回`n, fake_p, c`  
- 解题步骤：
  - `nc`连入服务器，获取`random_str[4:]`和`str_sha256`
  - 通过`getXXXX.py`爆破`random_str[:4]`，并将结果发送给服务器，获得`n，fake_p，c`
  - 基于`encrypt`函数，编写[`decrypt.py`](./files/decrypt.py)脚本，破解`p`，解密得到`flag`

## FLAG

```plain
D0g3{sYuWzkFk12A1gcWxG9pymFcjJL7CqN4Cq8PAIACObJ}
```
