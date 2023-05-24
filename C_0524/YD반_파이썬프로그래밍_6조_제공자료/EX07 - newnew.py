import pygame
import os

pygame.init()

### 사용할 이미지 파일 불러오기
coin = [pygame.image.load(os.path.join("Assets/Coin", f"Coin{i}.png")) for i in range(1,10)]
dino = [pygame.image.load(os.path.join("Assets/Dino", f"DinoRun{i}.png")) for i in range (1, 3)]

# &1-1
cactus = pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png"))

### Display 설정
pygame.display.set_caption("Hello, Screen!") 

screen_width = 1000 ## 디스플레이 가로 길이
screen_height = 600 ## 디스플레이 세로 길이
screen = pygame.display.set_mode((screen_width, screen_height))


### 사용 변수 선언 및 초기값 설정
run = True
index =0

clock=pygame.time.Clock()

coinIndex =0
coinIndexCounter =0
dino_img = dino[0]

cactus_x = 1000 #장애물 선인장 x값 위치 지정

# &1-2
move =10 #선인장이 이동하는 거리 지정
# *1-1
Power =55
# ~1-1
time = 0.01

input_key = 0

# ~1-2
font =pygame.font.Font('freesansbold.ttf', 20)


# &1-3
dino_rect = dino_img.get_rect()
dino_rect.x = 50
dino_rect.y = 400
cactus_rect = cactus.get_rect()
cactus_rect.x = cactus_x
cactus_rect.y = 400

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
    
    # &1-4
    cactus_rect.x = cactus_x

    for event in pygame.event.get(): #pygame으로 들어오는 이벤트 등을 모두 캐치
        if event.type == pygame.QUIT: #받아온 이벤트의 타입 중 QUIT에 해당되면
            run = False #무한 반복을 나오기 위해 제어 변수 False 지정
        # *1-2
        if event.type ==pygame.KEYDOWN :
            if event.key ==pygame.K_RIGHT :
                cactus_x += Power
                input_key += 1
    # ~1-3
    Timetext =font.render("Time Score : "+ str(round(time, 2)), True , (0, 0, 0))
    TimetextRect = Timetext.get_rect()
    TimetextRect.center = (300, 40)
    screen.blit(Timetext, TimetextRect)
    
    Inputtext =font.render("Input_key : "+ str(input_key), False , (0, 0, 0))
    InputtextRect = Inputtext.get_rect(center = (700, 40))
    screen.blit(Inputtext, InputtextRect)
    
    
    Resulttext =font.render("Input Per Second : "+ str(round((input_key / time),2)), False , (0, 0, 0))
    ResulttextRect = Resulttext.get_rect(center = (500, 400))
    screen.blit(Resulttext, ResulttextRect)
    
    # &1-5
    if dino_rect.colliderect(cactus_rect ):
        print('충돌')
        print(input_key / (time))
        pygame.time.delay(2000) #2초 대기
        run = False
    

    # &1-6
    screen.blit(dino[index // 5], dino_rect)
    screen.blit(coin[coinIndex], (250 , 250))
    screen.blit(cactus, cactus_rect)


    index += 1
    coinIndexCounter += 1
    
    # &1-7
    cactus_x -= move

    # ~1-4
    time += 1 / 60

    # 디스플레이 업데이트 -> 이부분을 해주어야 최종적으로 이미지가 보여진다.
    pygame.display.update()
    


#pygame 종료
pygame.quit()
