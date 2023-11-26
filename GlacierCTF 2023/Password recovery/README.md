# Password recovery

## 题目

Our infra admin "LosCapitan" stores all of his passwords in a self-hosted password manager. Shortly before the CTF, he forgot his password and now he can't access his passwords anymore. The keys to the underlying server are stored in the password manager as well. Luckily, he never changed his password and we still have the old password checker for one of our servers. Can you help us recover his password for the "LosCapitan" user? Wrap the correct password in gctf{}. Flag format is gctf{.*}.

author: Xer0

[app](./files/app)


## 考点

- `rev`


## WriteUp

- 使用`ghidra`调试`app`，查看对应寄存器中的值

## FLAG

```plain

```
