import pygame

# pygame 초기화
pygame.init()

# 화면 사이즈
size = [400,600]
screen = pygame.display.set_mode(size)

#게임 타이틀 이름 설정
pygame.display.set_caption("TestGame")

#fps 변수 설정
clock=pygame.time.Clock() 

# 배경 이미지 넣기
background=pygame.image.load("./학생발표/7조수업자료/background.png")

# 플래이어 이미지
character=pygame.image.load("./학생발표/7조수업자료/Character.png")

# 플래이어가 그려질 화면 좌표 
character_x=150
character_y=300
# 플래이어가 움직일 속도 
character_speed=4

sb = True
# 메인 이벤트
while  sb:
    clock.tick(60) #fps 설정 -> ()안은 1초당 몇번 반복될지

    # x 버튼을 누르면 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
 	        sb = False
    #방향키가 눌려지면, character_x나 character_y 값을 변경하여 이동시킨다
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT]:
          character_x -= character_speed
    elif keys[pygame.K_RIGHT]:
          character_x+=character_speed
    
    if keys[pygame.K_UP]:
          character_y-=character_speed
    elif[pygame.K_DOWN]:
          character_y+=character_speed

	#플레이어가 벽에 닿으면 게임종료
    if character_x+65<0 or character_x>size[0]- 65 or character_y+70<0 or character_y>size[1]-70:
         sb=False
    
    #이미지 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x,character_y))

    #화면 지속적으로 그리기
    pygame.display.update()
    

#게임 종료
pygame.display.quit()
pygame.quit()



