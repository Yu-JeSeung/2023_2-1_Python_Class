#import pygame을 사용해주기 위해서 터미널 -> 새로운 터미널 열기 -> pip install pygame 입력

# pygame 선언
import pygame

#pygame 초기화
#pygame 모듈을 사용해주기 위해선 무조건 초기화를 시켜줘야 된다.
pygame.init()

#pygame을 실행하기 위해서는 무한 반복이 되어야한다.
run = True #while 무한 반복문을 제어하기 위한 변수 지정

while run: 
    for event in pygame.event.get(): # pygame으로 들어오는 이벤트 등을 모두 캐치
        if event.type == pygame.QUIT: # 받아온 이벤트의 타입중 QUIT에 해당되면
            run = False # 무한 반복을 나오기 위해 제어 변수 False 지정

#pygame 종료
pygame.quit()