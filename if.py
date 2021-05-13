'''
rain = input('請問今天有沒有下雨： ')
if rain == '有':
    print('撐傘出門')
    print('買一包洋芋片')
    print('在家看電影')
'''

# 型別轉換 (Casting)----------------------------------------------------------------------
'''
age = input('請輸入年齡： ')
age = int(age)  # 將字串轉型為整數
if age >= 20:
    print('你可以投票')
'''

# 攝氏溫度轉換為華氏溫度
'''
c = input('請輸入攝氏溫度： ')
c = float(c)
f = c * 9 / 5 + 32
print('華氏溫度為： ', f)
'''

# Else (if架構延伸)
'''
age = input('請輸入年齡： ')
age = int(age)  # 將字串轉型為整數
if age >= 20:
    print('你可以投票')
else:
    print('你還不能投票喔')

'''

# Elif (if架構延伸)
'''
age = input('請輸入年齡： ')
age = int(age)  # 將字串轉型為整數
if age < 13:
    print('國小')
elif age >= 13 and age < 18:
    print('國高中')
elif age >= 18 and age < 22:
    print('大學')
else:
    print('社會')
'''
