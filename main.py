import pygame
import sys
import time
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((640,640))
pygame.display.set_caption("Game Caro")
font_intro=pygame.font.Font("Arial.ttf",50)

text_introduce="<PLAY GAME>"
background_1=pygame.image.load("background_1.jpg")
background_1=pygame.transform.scale(background_1,(640,640))

background_2=pygame.image.load("background_2.jpg")
background_2=pygame.transform.scale(background_2,(640,640))

background_o=pygame.image.load("image_o.png")
background_o=pygame.transform.scale(background_o,(130,130))

background_x=pygame.image.load("image_x.png")
background_x=pygame.transform.scale(background_x,(130,130))

background_winner=pygame.image.load("image_winner.png")
background_winner=pygame.transform.scale(background_winner,(640,640))

color_clicked=(255,48,48)
step_1=True
step_2=False

fist=True
second=False

o1=False
party_o1=""
o2=False
party_o2=""
o3=False
party_o3=""
o4=False
party_o4=""
o5=False
party_o5=""
o6=False
party_o6=""
o7=False
party_o7=""
o8=False
party_o8=""
o9=False
party_o9=""
font=pygame.font.Font("Arial.ttf",30)
text="Click vào ô để chọn"
instruction=font.render(text,True,(0,0,0))
text_o="Đây là lượt của O:"
text_o=font.render(text_o,True,(0,0,0))
text_x="Đây là lượt của X:"
text_x=font.render(text_x,True,(0,0,0))
running=True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            position_mouse=event.pos
            mouse_x=position_mouse[0]
            mouse_y=position_mouse[1]
            if mouse_x>=170 and mouse_x <=500 and mouse_y>=550 and mouse_y<=600 and step_1:
                color_clicked=(0,229,238)
                step_2=True
                step_1=False
            if mouse_x>=100 and mouse_x<=230 and mouse_y>=110 and mouse_y<=240 and step_2 and o1==False:
                if fist:
                    party_o1="first"
                    fist=False
                    second=True
                    o1=True
                elif second:
                    party_o1="second"
                    fist=True
                    second=False
                    o1=True
            elif mouse_x>=240 and mouse_x<=390 and mouse_y>=100 and mouse_y<=250 and step_2 and o2==False:
                if fist:
                    party_o2="first"
                    fist=False
                    second=True
                    o2=True
                    
                elif second:
                    party_o2="second"
                    fist=True
                    second=False
                    o2=True
                    
            elif mouse_x>=390 and mouse_x<=540 and mouse_y>=100 and mouse_y<=250 and step_2 and o3==False:
                if fist:
                    party_o3="first"
                    fist=False
                    second=True
                    o3=True
                    
                elif second:
                    party_o3="second"
                    fist=True
                    second=False
                    o3=True
                    
            #day 2
            elif mouse_x>=100 and mouse_x<=230 and mouse_y>=260 and mouse_y<=390 and step_2 and o4==False:
                if fist:
                    party_o4="first"
                    fist=False
                    second=True
                    o4=True
                   
                elif second:
                    party_o4="second"
                    fist=True
                    second=False
                    o4=True
                    
            elif mouse_x>=240 and mouse_x<=390 and mouse_y>=260 and mouse_y<=390 and step_2 and o5==False:
                if fist:
                    party_o5="first"
                    fist=False
                    second=True
                    o5=True
                    
                elif second:
                    party_o5="second"
                    fist=True
                    second=False
                    o5=True
                    
            elif mouse_x>=390 and mouse_x<=540 and mouse_y>=260 and mouse_y<=390 and step_2 and o6==False:
                if fist:
                    party_o6="first"
                    fist=False
                    second=True
                    o6=True
                    
                elif second:
                    party_o6="second"
                    fist=True
                    second=False
                    o6=True
                     
            #dong 3
            elif mouse_x>=100 and mouse_x<=230 and mouse_y>=400 and mouse_y<=550 and step_2 and o7==False:
                if fist:
                    party_o7="first"
                    fist=False
                    second=True
                    o7=True
                    
                elif second:
                    party_o7="second"
                    fist=True
                    second=False
                    o7=True
                    
            elif mouse_x>=240 and mouse_x<=390 and mouse_y>=400 and mouse_y<=550 and step_2 and o8==False:
                if fist:
                    party_o8="first"
                    fist=False
                    second=True
                    o8=True
                    
                elif second:
                    party_o8="second"
                    fist=True
                    second=False
                    o8=True
            elif mouse_x>=390 and mouse_x<=540 and mouse_y>=400 and mouse_y<=550 and step_2 and o9==False:
                if fist:
                    party_o9="first"
                    fist=False
                    second=True
                    o9=True
                elif second:
                    party_o9="second"
                    fist=True
                    second=False
                    o9=True
            
                 
    if step_1:
      introduce=font_intro.render(text_introduce,True,color_clicked)
      screen.blit(background_1,(0,0))
      screen.blit(introduce,(170,550))
    elif step_2:
        screen.blit(background_2,(0,0))
        
        screen.blit(instruction,(100,0))
        
        if fist:
            screen.blit(text_x,(100,600))
        elif second:
            screen.blit(text_o,(100,600))
            
        pygame.draw.rect(screen,(28,28,28),(90,100,150,150),2)
        pygame.draw.rect(screen,(28,28,28),(240,100,150,150),2)
        pygame.draw.rect(screen,(28,28,28),(390,100,150,150),2)
        
        #screen.blit(background_o,(100,260))
        #screen.blit(background_x,(100,260))
        
        pygame.draw.rect(screen,(28,28,28),(90,250,150,150),2)
        pygame.draw.rect(screen,(28,28,28),(240,250,150,150),2)
        pygame.draw.rect(screen,(28,28,28),(390,250,150,150),2)
        
        pygame.draw.rect(screen,(28,28,28),(90,400,150,150),2)
        pygame.draw.rect(screen,(28,28,28),(240,400,150,150),2)
        pygame.draw.rect(screen,(28,28,28),(390,400,150,150),2)
        
        if o1==True and party_o1=="first":
             screen.blit(background_x,(100,110))
        elif o1==True and party_o1=="second":
             screen.blit(background_o,(100,110))
             
        if o2==True and party_o2=="first":
             screen.blit(background_x,(250,110))
        elif o1==True and party_o2=="second":
             screen.blit(background_o,(250,110))
             
        if o3==True and party_o3=="first":
             screen.blit(background_x,(400,110))
        elif o3==True and party_o3=="second":
            screen.blit(background_o,(400,110))
            
        if o4==True and party_o4=="first":
             screen.blit(background_x,(100,250))
        elif o4==True and party_o4=="second":
            screen.blit(background_o,(100,250))
            
        if o5==True and party_o5=="first":
             screen.blit(background_x,(250,250))
        elif o5==True and party_o5=="second":
            screen.blit(background_o,(250,250))
        
        if o6==True and party_o6=="first":
             screen.blit(background_x,(400,250))
        elif o6==True and party_o6=="second":
            screen.blit(background_o,(400,250))
        
        if o7==True and party_o7=="first":
             screen.blit(background_x,(100,410))
        elif o7==True and party_o7=="second":
            screen.blit(background_o,(100,410))
        
        if o8==True and party_o8=="first":
             screen.blit(background_x,(250,410))
        elif o8==True and party_o8=="second":
            screen.blit(background_o,(250,410))
             
        if o9==True and party_o9=="first":
             screen.blit(background_x,(400,410))
        elif o9==True and party_o9=="second":
            screen.blit(background_o,(400,410))
            
        #check
        if o1 and o2 and o3 and o4 and o5 and o6 and o7 and o8 and o9:
           
            screen.blit(background_winner,(0,0))
        elif party_o1=="first" and party_o2=="first" and party_o3=="first":
            screen.blit(background_winner,(0,0))
        elif party_o4=="first" and party_o5=="first" and party_o6=="first":
            screen.blit(background_winner,(0,0))
        elif party_o7=="first" and party_o8=="first" and party_o9=="first":
            screen.blit(background_winner,(0,0))
        elif party_o1=="first" and party_o5=="first" and party_o9=="first":
            screen.blit(background_winner,(0,0))
        elif party_o7=="first" and party_o5=="first" and party_o3=="first":
            screen.blit(background_winner,(0,0))
        elif party_o1=="first" and party_o4=="first" and party_o7=="first":
            screen.blit(background_winner,(0,0))
        elif party_o2=="first" and party_o5=="first" and party_o8=="first":
            screen.blit(background_winner,(0,0))
        elif party_o3=="first" and party_o6=="first" and party_o9=="first":
            screen.blit(background_winner,(0,0))
        
        elif party_o1=="second" and party_o2=="second" and party_o3=="second":
            screen.blit(background_winner,(0,0))
        elif party_o4=="second" and party_o5=="second" and party_o6=="second":
           screen.blit(background_winner,(0,0))
        elif party_o7=="second" and party_o8=="second" and party_o9=="second":
            screen.blit(background_winner,(0,0))
        elif party_o1=="second" and party_o5=="second" and party_o9=="second":
           screen.blit(background_winner,(0,0))
        elif party_o7=="second" and party_o5=="second" and party_o3=="second":
            screen.blit(background_winner,(0,0))
        elif party_o1=="second" and party_o4=="second" and party_o7=="second":
            screen.blit(background_winner,(0,0))
        elif party_o2=="second" and party_o5=="second" and party_o8=="second":
            screen.blit(background_winner,(0,0))
        elif party_o3=="second" and party_o6=="second" and party_o9=="second":
            screen.blit(background_winner,(0,0))
    pygame.display.update()