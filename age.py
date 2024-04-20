drive = input('你有開過車嗎？')
age = input('請問你的年紀')
age = int(age)
if drive == '有':
    if age >= 18:
        print('恭喜你！符合開車年齡')
    else:
        print('在幾年就可考照')
elif drive == '沒有':
    if age >= 18:
        print('抱歉！你沒有符合法定年齡')
    else:
        print('再過幾年就可以考駕照囉！')
else:
    print('需要請你輸入 有還是沒有')