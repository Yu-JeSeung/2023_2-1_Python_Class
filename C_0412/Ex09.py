upp, low, dig, pct = 0, 0, 0, 0
pswd = input('암호 입력: ')
if pswd.isalnum()==False : pct=1 #특수문자있으면pct=1
for k in pswd: 
    if pswd.isupper() : upp = 1 
    elif pswd.islower(): low = 1
    elif pswd.isdigit(): dig = 1


if low + upp + dig + pct >= 3 : print('사용 가능')
else : print('!!불가능한 암호!!')