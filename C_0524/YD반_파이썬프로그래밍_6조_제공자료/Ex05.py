
import pygame
import os

pygame.init()

#프레임 제목 부분 설정
pygame.display.set_caption("Hello, Screen!")

#pygame 프레임 크기 지정
screen_width = 1000 #프레임 가로 길이
screen_height = 600 #프레임 세로 길이
screen = pygame.display.set_mode((screen_width, screen_height))
#괄호 안에 소괄호가 또 있는 이유는 튜플 형식으로 변하지 않게 하기 위해서 사용된 것이다

#이미지 로드
dino = [pygame.image.load(os.path.join("Assets/Dino", f"DinoRun{i }.png")) for i in range (1, 3)]
coin = [pygame.image.load(os.path.join("Assets/Coin", f"Coin{i}.png")) for i in range(1,10)]
cactus = pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png"))

#pygame을 실행하기 위해서는 무한 반복이 되어야한다.
run = True #while 무한 반복문을 제어하기 위한 변수 지정

clock = pygame.time.Clock()
index = 0 
coinIndex = -1
coinIndexCounter = 0
dino_img = dino[0]


cactus_x = 1000 #장애물 선인장 x값 위치 지정
move = 10 #선인장이 이동하는 거리 지정


while run: 
    clock.tick(60) # 초당 60프레임 지정
    
    screen.fill((255,255,255))
    
    if index >= 9:
        index = 0
        
    if coinIndexCounter > 6 :
        coinIndexCounter = 0
        coinIndex += 1
    
    if coinIndex >= 9 :
        coinIndex = 0

    if cactus_x < -50:
        cactus_x = 1000
        
    

    for event in pygame.event.get(): #pygame으로 들어오는 이벤트 등을 모두 캐치
        if event.type == pygame.QUIT: #받아온 이벤트의 타입 중 QUIT에 해당되면
            run = False #무한 반복을 나오기 위해 제어 변수 False 지정
    
    dino_rect = dino_img.get_rect()
    dino_rect.x = 50
    dino_rect.y = 400

    cactus_rect = cactus.get_rect()
    cactus_rect.x = cactus_x
    cactus_rect.y = 400

    #충돌 검사
    if dino_rect.colliderect(cactus_rect):
            print('충돌')
            pygame.time.delay(2000) #2초 대기
            run = False
    

    #이미지 출력
    screen.blit(dino[index // 5], dino_rect)
    screen.blit(coin[coinIndex], (250, 250))
    screen.blit(cactus, cactus_rect)

    index += 1
    coinIndexCounter += 1
    cactus_x -= move

    # 디스플레이 업데이트 -> 이부분을 해주어야 최종적으로 이미지가 보여진다.
    pygame.display.update()
    


#pygame 종료
pygame.quit()