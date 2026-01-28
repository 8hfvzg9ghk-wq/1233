import re

with open(r'c:\Users\AVWIN-NPD\Documents\trae_projects\1233\alarm.html', 'r', encoding='utf-8') as f:
    content = f.read()
    matches = re.findall(r"Audio\(['\"]([^'\"]+)['\"]\)", content)
    print('音频文件引用:')
    for m in matches:
        print(f'  - {m}')
