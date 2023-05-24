#import pygame을 사용해주기 위해서 터미널 -> 새로운 터미널 열기 -> pip install pygame 입력

# pygame 선언
import pygame
import sys

#pygame 초기화
#pygame 모듈을 사용해주기 위해선 무조건 초기화를 시켜줘야 된다.
pygame.init()

#프레임 제목 부분 설정
pygame.display.set_caption("Hello, Screen!")

#pygame 프레임 크기 지정
screen_width = 1000 #프레임 가로 길이
screen_height = 600 #프레임 세로 길이
SCREEN = pygame.display.set_mode((screen_width, screen_height))
#괄호 안에 소괄호가 또 있는 이유는 튜플 형식으로 변하지 않게 하기 위해서 사용된 것이다

#pygame을 실행하기 위해서는 무한 반복이 되어야한다.
run = True #while 무한 반복문을 제어하기 위한 변수 지정


while run: 

    
    for event in pygame.event.get(): #pygame으로 들어오는 이벤트 등을 모두 캐치
        if event.type == pygame.QUIT: #받아온 이벤트의 타입중 QUIT에 해당되면
            run = False #무한 반복을 나오기 위해 제어 변수 False 지정
            pygame.quit()
            sys.exit()

    SCREEN.fill((255,255,255))
    pygame.display.update()
    
