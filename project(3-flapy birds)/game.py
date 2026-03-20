import pygame as pg
import sys,time
from bird import bird
from pipe import Pipe
pg.init()

class Game:
    def __init__(self):
        self.width = 600
        self.height =661
        self.scale_factor= 1.5
        self.win=pg.display.set_mode((self.width,self.height))
        self.clock=pg.time.Clock()
        self.move_speed=270
        self.start_monitaring=False
        self.score=0
        self.font=pg.font.Font("assets/font.ttf",24)
        self.score_text=self.font.render("Score:= 0",True,(243,243,243))
        self.score_text_rect=self.score_text.get_rect(center=(100,30))

        self.restart_text=self.font.render("Restart",True,(243,243,243))
        self.restart_text_rect=self.score_text.get_rect(center=(350,500))


        self.bird=bird(self.scale_factor)

        self.is_enter_pressed=False
        self.is_game_started= True
        self.pipes=[]
        self.pipe_generate_counter=70
        self.setupBgAndGround()

        self.gameLoop()
    
    def gameLoop(self):

        last_time=time.time()

        while True:
            new_time=time.time()
            dt=new_time - last_time
            last_time=new_time
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type==pg.KEYDOWN and self.is_game_started:
                     if event.key==pg.K_RETURN:

                       self.is_enter_pressed=True
                       self.bird.update_on=True

                if event.type==pg.MOUSEBUTTONDOWN:
                    self.bird.flap(dt)

                if event.type==pg.MOUSEBUTTONUP:
                    if self.restart_text_rect.collidepoint(pg.mouse.get_pos()):
                        self.restartGame()
                        

                
               

            self.update_everything(dt)
            self.checkCollisions()
            self.checkScore()
            self.draweverything()

            pg.display.update()
            self.clock.tick(60)

    def restartGame(self):
        self.score=0
    
        self.score_text=self.font.render("Score: 0",True,(243,243,243))
        self.is_enter_pressed=False
        self.is_game_started=True
        self.bird.resetpositon()
        self.pipes.clear()
        self.pipe_generate_counter=70
        
    
    def checkScore(self):
        if len(self.pipes)>0:
            if (self.bird.rect.left > self.pipes[0].rect_down.left and self.bird.rect.right < self.pipes[0].rect_down.right and not self.start_monitaring):

                 self.start_monitaring=True


            if self.bird.rect.left > self.pipes[0].rect_down.right and self.start_monitaring:
                self.start_monitaring=False
                self.score+=1
                self.score_text=self.font.render(f"Score: { self.score} ",True,(243,243,243))

    def checkCollisions(self):
        if len(self.pipes):
            if self.bird.rect.bottom>461:
                
                self.bird.update_on=False
                self.is_enter_pressed=False
                self.is_game_started=False
                
            if(self.bird.rect.colliderect(self.pipes[0].rect_down) or self.bird.rect.colliderect(self.pipes[0].rect_up)):
                self.is_enter_pressed=False

                self.is_game_started=False



    def update_everything(self,dt):
         if self.is_enter_pressed:
              self.ground1_img_rect.x -= int(self.move_speed*dt)
              self.ground2_img_rect.x -= int(self.move_speed*dt)

              if self.ground1_img_rect.right<0:
                  self.ground1_img_rect.x=self.ground2_img_rect.right
              if self.ground2_img_rect.right<0:
                  self.ground2_img_rect.x=self.ground1_img_rect.right

              if self.pipe_generate_counter>70:
                  self.pipes.append(Pipe(self.scale_factor,self.move_speed))
                  self.pipe_generate_counter=0
                #   print("pipe created")
              self.pipe_generate_counter+=1

              for pipe in self.pipes:
                  pipe.update(dt)

              if len(self.pipes)!=0:
                  if self.pipes[0].rect_up.right<0:
                      self.pipes.pop(0)
                    #   print("pipe removed")
              

         


         self.bird.update(dt)

              
    def draweverything(self):
            
            self.win.blit(self.bg_img,(0,-250))
            for pipe in self.pipes:
                pipe.drawPipe(self.win)
            self.win.blit(self.ground1_img,self.ground1_img_rect)
            self.win.blit(self.ground2_img,self.ground2_img_rect)
            self.win.blit(self.bird.image,self.bird.rect)
            self.win.blit(self.score_text,self.score_text_rect)
            if not self.is_game_started:
                 self.win.blit(self.restart_text,self.restart_text_rect)

            

    def setupBgAndGround(self):
       
        self.bg_img=pg.transform.scale( pg.image.load("assets/bg.png").convert(),(600,911))
        self.ground1_img=pg.transform.scale( pg.image.load("assets/ground.png").convert(),(600,911))
        self.ground2_img=pg.transform.scale( pg.image.load("assets/ground.png").convert(),(600,911))


        self.ground1_img_rect=self.ground1_img.get_rect()
        self.ground2_img_rect=self.ground2_img.get_rect()

        self.ground1_img_rect.x=0
        self.ground2_img_rect.x=self.ground1_img_rect.right
        self.ground1_img_rect.y=461
        self.ground2_img_rect.y=461
   

game=Game()
