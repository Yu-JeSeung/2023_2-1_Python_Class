mdic_list = {'기본햄버거':4000, '치즈햄버거':4500, '불고기버거':5000, '와퍼킹버거':7000}

# 1)  [4]의 menu를 키로 하고 price를 값으로 하여 mdict_list를 만들어 출력해 보자
print(mdic_list)

# 2) 새우버거, 5500원 추가 mdict_list에 추가하고 출력한다
mdic_list['새우버거']=5500
print(mdic_list)

# 3) 기본햄버거 삭제하고 나이스버거 2000원 추가하고 출력한다
del(mdic_list['기본햄버거'])
mdic_list['나이스버거']=2000
print(mdic_list)

# 4) for ~ in ~~을 이용하여 다음과 같이 출력되도록 코딩하고 확인하시오

# 치즈햄버거 : 4500
# 불고기버거 : 5500
# 와퍼킹버거 : 7000
# 새우버거 : 5500
# 나이스버거 : 2000
for key,value in mdic_list.items():
    print(key,':',value)