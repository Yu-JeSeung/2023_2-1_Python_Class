import random

taro= ['자유', '시작', '갈등', '풍요', '성공', '자립', '연예', '전진',
        '극복', '회피', '선택', '안정', '희생', '불행', '인내', '유혹',
        '파괴', '균형', '불안', '행복', '결단', '성취']

num=len(taro)

for k in range(5):
    tnum=random.randrange(0,num)
    print('뽑은 카드는 %s\n'%taro[tnum])