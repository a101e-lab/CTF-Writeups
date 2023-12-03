import requests

url = "https://hacker-typer.tuctf.com/check_word"  # 替换为您的请求URL

# 初始化word字段的值
word = "rooting"
# # 创建一个CookieJar对象，用于保存cookie
# cookies = requests.cookies.RequestsCookieJar()
# cookies.set("uuid", "534524c4-b7f8-42f9-8f59-f010af3c6246")

# 添加请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://hacker-typer.tuctf.com",
    "Referer": "https://hacker-typer.tuctf.com/",
    "Cookie": "uuid=78d6ec41-5e6b-448e-b823-2ba54ecb54d3",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

# 循环发送POST请求
for _ in range(200):
    payload = "word=" + word
    response = requests.post(url, data=payload, headers=headers)
    # response = requests.post(url, data=data)
    print(response.text)
    # 检查请求是否成功
    if response.status_code != 200:
        print("请求失败:", response.status_code)
        break
    
    try:
        json_data = response.json()
        next_word = json_data.get("next_word")
        
        # 检查是否成功获取到next_word字段
        if next_word is None:
            print("未能获取到next_word字段")
            break
        
        # 更新word字段的值
        word = next_word
        
        # 打印响应结果
        # print(json_data)
    
    except ValueError:
        print("响应内容无法解析为JSON格式")
        break
