import pygame

pygame.init()

Screen_Width = 640
Screen_Height = 460
Lower_Margin = 340
Side_Margin = 340


Screen = pygame.display.set_mode((Screen_Width + Side_Margin, Screen_Height + Lower_Margin ))
pygame.display.set_caption("Level Editor")

scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1.5
Screen.fill((255,225,225))


    
    
run = True
while run:
    

    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
       
                
   
            
    pygame.display.update()
pygame.quit()




