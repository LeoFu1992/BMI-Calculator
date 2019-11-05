w = input('請輸入體重:')
h = input('請輸入身高:')
w = int(w)
h = float(h)
b = w / h ** 2
if b < 18.5:
    print('你的BMI為', b, '體重過輕')
elif b >= 18.5 and b < 24:
    print('你的BMI為', b, '正常')
elif b >= 27 and b < 30:
    print('你的BMI為', b, '輕度肥胖')
elif b >= 30 and b < 35:
    print('你的BMI為', b, '中度肥胖')
elif b > 35:
    print('你的BMI為', b, '重度肥胖')