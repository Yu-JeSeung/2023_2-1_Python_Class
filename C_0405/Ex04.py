menu = ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거')
price = (4000, 4500, 5000, 7000)

# 다음과 같이 출력하는 코드를 작성한다
# 1 : 기본햄버거 : 4000
# 2 : 치즈햄버거 : 4500
# 3 : 불고기버거 : 5000
# 4 : 와퍼킹버거 : 7000

for i in range(4):
    print(i+1,':',menu[i],':',price[i])

# 새우버거 5500원을 추가하고(변경이 있다면 리스트로 변경해야한다)
# 다음과 같이 출력하는 코드를 작성한다
# 메뉴: ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거', '새우버거')
# 가격: (4000, 4500, 5000, 7000, 5500)

lmenu = list(menu)
lprice = list(price)
lmenu.append('새우버거')
lprice.append(5500)

menu = tuple(lmenu)
price = tuple(lprice)

print('메뉴 :',menu)
print('가격 :',price)