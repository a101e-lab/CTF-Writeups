import json
from collections import defaultdict

# 创建一个默认值为0的字典
phrase_count = defaultdict(int)

# 打开log文件进行读取
with open('lost_map.log', 'r') as file:
    # 逐行读取log文件
    for line in file:
        # 去除每行的首尾空格
        phrase = line.strip()
        # 检查短语是否已经在字典中
        if phrase in phrase_count:
            # 短语已经在字典中，将其对应的值加1
            phrase_count[phrase] += 1
        else:
            # 短语不在字典中，将其添加到字典并设置初始值为1
            phrase_count[phrase] = 1

# 将字典转换为JSON格式的字符串
json_data = json.dumps(phrase_count, indent=4)

# 将JSON字符串写入到文件中
with open('result.json', 'w') as file:
    file.write(json_data)
