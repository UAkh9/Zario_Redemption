import pygame
import sys

pygame.init()
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image test")

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


BACKGROUND = pygame.image.load("assets/cloudbackground.png")
SCREEN.blit(BACKGROUND, (0, 0))

pygame.display.update()
CLOCK.tick(60)

{
    "id":0,
    "length":60,
    "level":{
        "objects": {
                "bush":[
                    [2,12],
                    [17,12],
                    [24,12],
                    [34,12],
                    [40,12],
                    [44,12]
                ],
                "sky":[
                    [48,13],
                    [49,13],
                    [48,14],
                    [49,14]
                ],
                "cloud":[
                    [5,5],
                    [13,3],
                    [26,5],
                    [32,3],
                    [42,6],
                    [55,4]
                ],
                "pipe":[
                    [8,10,4],
                    [12,12,4],
                    [22,12,4],
                    [29,9,6]
                ],
                "ground":[
                    [40,9],
                    [41,9],
                    [42,9],
                    [43,9],
                    [44,9],
                    [45,9],
                    [45,9],
                    [46,9],
                    [47,9],
                    [50,9],
                    [51,9],
                    [52,9],
                    [53,9],
                    [54,9],
                    [55,9],
                    [54,8],
                    [55,8],
                    [56,8],
                    [57,8],
                    [58,8],
                    [59,8]
                ]
            },
        "layers": {
                "sky":{
                    "x":[0,60],
                    "y":[0,13]
                },
                "ground":{
                    "x":[0,60],
                    "y":[14,16]
                }
        }
        
    }

}

