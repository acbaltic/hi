'''
name = input('請輸入名字：')
print('嗨', name)
'''

# 打開檔案並讀取
# \n 及 print本身的換行符號，故會產生空行
# .strip()將字串後的換行符號及空格清除掉
data = []
with open('E:/OneDrive/ConceptDraw Office/資通程式/Python/pythonData/movies.csv', 'r') as f:
    for line in f:
        data.append(line.strip())
print(len(data))
print(data[0])
print(data)