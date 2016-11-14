
import pygame
import time
import random

def start():
  pygame.init() #initislise pygame
  

  width = 800   #window size
  height = 600

  black = (0,0,0)          ##
  white = (255,255,255)    ##define colours

  red = (200,0,0)          ##
  bright_red = (255,0,0)

  green = (0,200,0)
  bright_green = (0,255,0)

  blue = (41,199,194)
  light_blue = (150,233,231)
  
  orange = (238,109,15)

  yellow = (224,214,5)
  bright_yellow = (249,237,11)

  brown = (74,0,0)
  bright_brown = (174,0,0)

  gray = (188,188,188)

  pink = (230,100,230)
  
  block_color = (245,0,0)


  arrow_width = 82       #define object size    
  arrow_height = 82



  gamedisplay = pygame.display.set_mode((width,height)) #define game display
  pygame.display.set_caption('Interstellar')               #game title 
  clock = pygame.time.Clock()                           #define pygame clock

  arrowImg = pygame.image.load('Arrow.png')             #upload the object as img
  rocket1 = pygame.image.load('rocket1.png')
  rocket2 = pygame.image.load('rocket2.png')
  rocket3 = pygame.image.load('rocket3.png')
  rocket4 = pygame.image.load('rocket4.png')
  gameicon = pygame.image.load('icon.png')

  pygame.display.set_icon(gameicon)

  pause = False

  def things_dodged(count):
    font = pygame.font.SysFont('comicsansms', 25)
    text = font.render('Dodged: ' + str(count),True,orange)
    gamedisplay.blit(text,(10,10))

  def player_score(count):
    font = pygame.font.SysFont('comicsansms', 25)
    text = font.render('Socre: ' + str(count),True,pink)
    gamedisplay.blit(text,(10,40))

  def well():
    global dodged
    font = pygame.font.SysFont('comicsansms', 25)
    if dodged > 9 and dodged < 12:
      text = font.render('You dodged 10, keep going! :)',True,orange)
      gamedisplay.blit(text,(200,40))
    elif dodged > 19 and dodged < 23:
      text = font.render('You dodged 20, Excellent!',True,orange)
      gamedisplay.blit(text,(200,40))
    elif dodged > 29 and dodged < 33:
      text = font.render('You dodged 30, WOW! :O',True,orange)
      gamedisplay.blit(text,(200,40))
    elif dodged > 39 and dodged < 43:
      text = font.render('You dodged 40, you got skills!',True,orange)
      gamedisplay.blit(text,(200,40))
    elif dodged > 49 and dodged < 55:
      text = font.render('You dodged 50, i like your Expertise!',True,orange)
      gamedisplay.blit(text,(200,40))
    elif dodged > 58 and dodged < 66:
      text = font.render('You dodged 60, You are awasome!',True,orange)
      gamedisplay.blit(text,(200,40))
    elif dodged > 68 and dodged < 76:
      text = font.render('You are a certified Gamer!',True,orange)
      gamedisplay.blit(text,(200,40))
    elif dodged > 78 and dodged < 87:
      text = font.render('You are a PRO',True,orange)
      gamedisplay.blit(text,(200,40))
    elif dodged > 88 and dodged < 97:
      text = font.render('Take it EASY!',True,orange)
      gamedisplay.blit(text,(200,40))
    elif dodged > 108 and dodged < 118:
      text = font.render('WELL DONE!!!',True,orange)
      gamedisplay.blit(text,(200,40))
    elif dodged > 117 and dodged < 129:
      text = font.render('That\'s the way forward',True,orange)
      gamedisplay.blit(text,(200,40))
    elif dodged > 127 and dodged < 150:
      text = font.render('THIS IS YOUR GAME NOW!',True,orange)
      gamedisplay.blit(text,(200,40))
            
    

    
  def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gamedisplay, color, [thingx, thingy, thingw, thingh])

##  def things(thingx,thingy,thingw,thingh,color):
##    pygame.draw.rect(gamedisplay, color, [thingx, thingy, thingw, thingh])

  def things2(thingx2,thingy2,thingw2,thingh2,color2):
    pygame.draw.rect(gamedisplay, color2, [thingx2, thingy2, thingw2, thingh2])

  def things3(thingx3,thingy3,thingw3,thingh3,color3):
    pygame.draw.rect(gamedisplay, color3, [thingx3, thingy3, thingw3, thingh3])


      
  def arrow(x,y):                                       #object fun, display img on screen
    if vc1 == True:
      gamedisplay.blit(arrowImg,(x,y))
    if vc2 == True:
      gamedisplay.blit(rocket1,(x,y))
    if vc3 == True:
      gamedisplay.blit(rocket2,(x,y))
    if vc4 == True:
      gamedisplay.blit(rocket3,(x,y))
    if vc5 == True:
      gamedisplay.blit(rocket4,(x,y))


  def text_objects(text, font):                         #define text object
    textSurface = font.render(text, True, black)        #font render,text color 
    return textSurface, textSurface.get_rect()          #return text
    
  def crash():     #print message if crash fu
      global dodged,score,green_boxes
      pygame.mixer.music.stop()
      pygame.mixer.music.load("Explosion.mp3")
      pygame.mixer.music.play(1)

      col = loop_background()
      gamedisplay.fill(col)
      
      largetext = pygame.font.SysFont('comicsansms',115)   
      TextSurf, TextRect = text_objects('You Crashed', largetext)
      TextRect.center = (410,100)
      
      gamedisplay.blit(TextSurf, TextRect)

      #score table
      pygame.draw.rect(gamedisplay, black, pygame.Rect(160,180,500,250),1)
      pygame.draw.lines(gamedisplay, black, False, [(160,215),(660,215)],1)#1st row
      pygame.draw.lines(gamedisplay, black, False, [(200,180),(200,429)],1)#1st col
      pygame.draw.lines(gamedisplay, black, False, [(280,180),(280,429)],1)#2nd col
      pygame.draw.lines(gamedisplay, black, False, [(350,180),(350,429)],1)#3rd col
      pygame.draw.lines(gamedisplay, black, False, [(480,180),(480,429)],1)#4th col
      font = pygame.font.SysFont('comicsansms', 18)
      text = font.render('No.',True,black)
      gamedisplay.blit(text,(165,185))
      text = font.render('1.',True,black)
      gamedisplay.blit(text,(165,215))
      text = font.render('Dodged',True,black)
      gamedisplay.blit(text,(205,185))
      text = font.render('Score',True,black)
      gamedisplay.blit(text,(285,185))
      text = font.render('Green boxes',True,black)
      gamedisplay.blit(text,(355,185))
      text = font.render('Overall Score',True,black)
      gamedisplay.blit(text,(485,185))      
      text = font.render(str(dodged),True,black)
      gamedisplay.blit(text,(205,215))
      text = font.render(str(score),True,black)
      gamedisplay.blit(text,(285,215))
      text = font.render(str(green_boxes),True,black)
      gamedisplay.blit(text,(355,215))
      text = font.render(str(format((dodged+score+green_boxes)/3,'.2f')),True,black)
      gamedisplay.blit(text,(485,215))

##      dodged2 = 
##      if dodged != dodged2:
##        dodged2 = dodged
##      else:
##        dodged 
##        
      
      
      while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        
        #borders
        pygame.draw.lines(gamedisplay, black, False, [(160,449),(259,449),(160,500),(259,500)],1)
        pygame.draw.lines(gamedisplay, black, False, [(340,449),(439,449),(340,500),(439,500)],1)
        pygame.draw.lines(gamedisplay, black, False, [(510,449),(609,449),(510,500),(609,500)],1)
      
        button('Try Again',160,450,100,50,green,bright_green, game_loop)
        button('Quit',510,450,100,50,red,bright_red,quitgame)
        button('Menu',340,450,100,50,blue,light_blue,game_into)

        pygame.display.update()
        clock.tick(15)

  def button(msg,x,y,w,h,ic,ac,action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0]  > x and y+h > mouse[1] > y:
      pygame.draw.rect(gamedisplay, ac, (x,y,w,h))
      if click [0] == 1 and action != None:
        action()
    else:
      pygame.draw.rect(gamedisplay, ic, (x,y,w,h))

    smalltext = pygame.font.SysFont('comicsansms',20) 
    textSurf, textRect = text_objects(msg,smalltext)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gamedisplay.blit(textSurf, textRect)


  def game_settings():
      
      while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        #large setting
        gamedisplay.fill(blue)
        largetext = pygame.font.SysFont('comicsansms',115)    
        TextSurf, TextRect = text_objects('Settings', largetext)
        TextRect.center = ((width/2.3),(height/6.7))        
        gamedisplay.blit(TextSurf, TextRect)

        #setting title
        font = pygame.font.SysFont('comicsansms', 20)
        text = font.render('Choose Game Background',True,black)
        gamedisplay.blit(text,((230),200))

        #border
        pygame.draw.lines(gamedisplay, black, False, [(115,269),(595,269),(115,320),(595,320)],1)
        
        
        #background colour buttons
        button('White',115,270,120,50,gray,white,var1)
        if bc_white == True:
          pygame.draw.rect(gamedisplay, black, pygame.Rect(135,278,80,35),2)
        button('Blue',235,270,120,50,blue,light_blue,var2)
        if bc_blue == True:
          pygame.draw.rect(gamedisplay, black, pygame.Rect(255,278,80,35),2)
        button('Yellow',355,270,120,50,yellow,bright_yellow,var3)
        if bc_yellow == True:
          pygame.draw.rect(gamedisplay, black, pygame.Rect(375,278,80,35),2)
        button('Brown',475,270,120,50,brown,bright_brown,var4)
        if bc_brown == True:
          pygame.draw.rect(gamedisplay, black, pygame.Rect(495,278,80,35),2)

        #seting title 2
        font = pygame.font.SysFont('comicsansms', 20)
        text = font.render('Choose your Vehicle',True,black)
        gamedisplay.blit(text,((252),350))
        #rockets
        gamedisplay.blit(arrowImg,(120,412))#180,442
        gamedisplay.blit(rocket1,(205,398))
        gamedisplay.blit(rocket2,(305,418))
        gamedisplay.blit(rocket3,(420,418))
        gamedisplay.blit(rocket4,(520,380))
        #vehicle buttons
        button('',147,520,25,20,blue,blue,veh_cho1)#207,540
        pygame.draw.rect(gamedisplay, black, pygame.Rect(147,516,25,20),2)
        if vc1 == True:
          pygame.draw.rect(gamedisplay, black, pygame.Rect(151,520,17,12),2)
        button('',233,520,25,20,blue,blue,veh_cho2)
        pygame.draw.rect(gamedisplay, black, pygame.Rect(233,516,25,20),2)
        if vc2 == True:
          pygame.draw.rect(gamedisplay, black, pygame.Rect(237,520,17,12),2)
        button('',336,520,25,20,blue,blue,veh_cho3)
        pygame.draw.rect(gamedisplay, black, pygame.Rect(336,516,25,20),2)
        if vc3 == True:
          pygame.draw.rect(gamedisplay, black, pygame.Rect(340,520,17,12),2)
        button('',447,520,25,20,blue,blue,veh_cho4)
        pygame.draw.rect(gamedisplay, black, pygame.Rect(447,516,25,20),2)
        if vc4 == True:
          pygame.draw.rect(gamedisplay, black, pygame.Rect(451,520,17,12),2)
        button('',542,520,25,20,blue,blue,veh_cho5)
        pygame.draw.rect(gamedisplay, black, pygame.Rect(542,516,25,20),2)
        if vc5 == True:
          pygame.draw.rect(gamedisplay, black, pygame.Rect(546,520,17,12),2)
        
        button('Menu',700,0,100,600,green,bright_green, game_into)

        pygame.display.update()
        clock.tick(60)
  #####################################
  #vehicle choice variables (vc - vehicle choice)
  def veh_cho1():
    global vc1,vc2,vc3,vc4,vc5
    if vc2 == True:
      vc2 = False
    if vc3 == True:
      vc3 = False
    if vc4 == True:
      vc4 = False
    if vc5 == True:
      vc5 = False
    vc1 = True
    

  def veh_cho2():
    global vc1,vc2,vc3,vc4,vc5
    if vc1 == True:
      vc1 = False
    if vc3 == True:
      vc3 = False
    if vc4 == True:
      vc4 = False
    if vc5 == True:
      vc5 = False
    vc2 = True

  def veh_cho3():
    global vc1,vc2,vc3,vc4,vc5
    if vc2 == True:
      vc2 = False
    if vc1 == True:
      vc1 = False
    if vc4 == True:
      vc4 = False
    if vc5 == True:
      vc5 = False
    vc3 = True

  def veh_cho4():
    global vc1,vc2,vc3,vc4,vc5
    if vc2 == True:
      vc2 = False
    if vc3 == True:
      vc3 = False
    if vc1 == True:
      vc1 = False
    if vc5 == True:
      vc5 = False
    vc4 = True

  def veh_cho5():
    global vc1,vc2,vc3,vc4,vc5
    if vc2 == True:
      vc2 = False
    if vc3 == True:
      vc3 = False
    if vc4 == True:
      vc4 = False
    if vc1 == True:
      vc1 = False
    vc5 = True
  ###################################
  #background color management
  global bc_white,bc_blue,bc_yellow,bc_brown
  bc_white = True
  bc_blue = False
  bc_yellow = False
  bc_brown = False

  #vehicle choice variables
  global vc1,vc2,vc3,vc4,vc5
  vc1 = True
  vc2 = False
  vc3 = False
  vc4 = False
  vc5 = False
  
  def var1():
    global bc_white,bc_blue,bc_yellow,bc_brown
    if bc_blue == True:
      bc_blue = False
    if bc_yellow == True:
      bc_yellow = False
    if bc_brown == True:
      bc_brown = False
    bc_white = True
    pygame.draw.rect(gamedisplay, black, pygame.Rect(130,273,90,45),2)
    print(bc_white)

    

  def var2():
    global bc_white,bc_blue,bc_yellow,bc_brown
    if bc_white == True:
      bc_white = False
    if bc_yellow == True:
      bc_yellow = False
    if bc_brown == True:
      bc_brown = False
    bc_blue = True
    pygame.draw.rect(gamedisplay, black, pygame.Rect(250,273,90,45),2)
    print(bc_blue)

  def var3():
    global bc_white,bc_blue,bc_yellow,bc_brown
    if bc_blue == True:
      bc_blue = False
    if bc_white == True:
      bc_white = False
    if bc_brown == True:
      bc_brown = False
    bc_yellow = True
    pygame.draw.rect(gamedisplay, black, pygame.Rect(370,273,90,45),2)
    print(bc_yellow)

  def var4():
    global bc_white,bc_blue,bc_yellow,bc_brown
    if bc_blue == True:
      bc_blue = False
    if bc_yellow == True:
      bc_yellow = False
    if bc_white == True:
      bc_white = False
    bc_brown = True
    pygame.draw.rect(gamedisplay, black, pygame.Rect(490,273,90,45),2)
    print(bc_brown)
    
  def loop_background():
    if bc_brown == True:
      return brown
    if bc_blue == True:
      return blue
    if bc_yellow == True:
      return yellow
    if bc_white == True:
      return white

  ##################################
  def game_instructions():
      while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        gamedisplay.fill(yellow)  
        font = pygame.font.SysFont('comicsansms', 60)
        text = font.render('Instructions',True,black)
        gamedisplay.blit(text,(220,60))
        font = pygame.font.SysFont('comicsansms', 18)
        text = font.render('1. Avoid left & right edges of the window',True,black)
        gamedisplay.blit(text,(30,140))
        text = font.render('2. Avoid red blocks',True,black)
        gamedisplay.blit(text,(30,160))
        text = font.render('3. Eat green blocks',True,black)
        gamedisplay.blit(text,(30,180))
        text = font.render('- Earn 2 points for dodging each red block',True,black)
        gamedisplay.blit(text,(30,220))
        text = font.render('- 3 points for eating green blocks',True,black)
        gamedisplay.blit(text,(30,240))
        text = font.render('- Go in the middle of the red box to save yourself!',True,black)
        gamedisplay.blit(text,(30,260))
        text = font.render('- If you go in the middle of green box, you miss out 3 points',True,black)
        gamedisplay.blit(text,(30,280))
        
        text = font.render('- Good Luck!',True,black)
        gamedisplay.blit(text,(30,320))

        button('Menu',700,0,100,600,green,bright_green, game_into)
          
        pygame.display.update()
        clock.tick(15)
      

  def quitgame():
    pygame.quit()
    quit()

  def unpause():
    pygame.mixer.music.unpause()
    global pause
    pause = False

  def paused():
    pygame.mixer.music.pause()
    global bc_blue, bc_yellow, bc_brown
    global pause
    largetext = pygame.font.SysFont('comicsansms',115)    
    TextSurf, TextRect = text_objects('Paused', largetext)
    TextRect.center = ((width/2),(height/2))        
    gamedisplay.blit(TextSurf, TextRect)

    while pause:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()

      
      
      #if bc_blue == True:
        #bc_blue = False
      #if bc_yellow == True:
        #bc_yellow = False
      #if bc_brown == True:
        #bc_brown = False

      #borders
      pygame.draw.lines(gamedisplay, black, False, [(150,449),(250,449),(150,500),(250,500)],1)
      pygame.draw.lines(gamedisplay, black, False, [(340,449),(440,449),(340,500),(440,500)],1)
      pygame.draw.lines(gamedisplay, black, False, [(550,449),(650,449),(550,500),(650,500)],1)
      
      button('Continue',150,450,100,50,green,bright_green, unpause)
      button('Quit',550,450,100,50,red,bright_red,quitgame)
      button('Menu',340,450,100,50,blue,light_blue, game_into)

      pygame.display.update()
      clock.tick(15)

  def boxes_collected_msg():
      global dodged
      if dodged > 0:
        font = pygame.font.SysFont('comicsansms', 20)
        text = font.render('3 Points Earned',True,black)
        gamedisplay.blit(text,(400,100))

      
  def game_into():
    
    pygame.mixer.music.stop()
    intro = True
    while intro:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()

      
      gamedisplay.fill(white)
      button('Start',170,0,100,600,green,bright_green, game_loop)
      button('Quit',500,0,100,600,red,bright_red,quitgame)
      button('Instructions',270,0,130,600,yellow,bright_yellow,game_instructions)
      button('Settings',400,0,100,600,blue,light_blue,game_settings) 
      largetext = pygame.font.SysFont('comicsansms',115)    
      TextSurf, TextRect = text_objects('Interstellar', largetext)
      TextRect.center = ((width/2),(height/5))        
      gamedisplay.blit(TextSurf, TextRect)

      
         
      
      
      pygame.display.update()
      clock.tick(15)
    
  def game_loop():
    pygame.mixer.music.load("Space.mp3")
    pygame.mixer.music.play(-1)

    global pause
    global block_color
    
    x = (width * 0.45)
    y = (height * 0.86)


    x_change = 0               #how much the object will move
   
    thing_startx = random.randrange(0,width)
    thing_starty = -600
    thing_speed = 2.5
    thing_width = 60
    thing_height = 60

    thing_startx2 = random.randrange(0,width)
    thing_starty2 = -1200
    thing_speed2 = 2.5
    thing_width2 = 40
    thing_height2 = 40

    thing_startx3 = random.randrange(0,width)
    thing_starty3 = -4000
    thing_speed3 = 2.5
    thing_width3 = 60
    thing_height3 = 60

    global dodged,score,green_boxes
    dodged = 0
    score = 0
    green_boxes = 0
    
    gameExit = False        #define gameexit
    while not gameExit:     #loop
     
      for event in pygame.event.get():          #get the actions from user
        if event.type == pygame.QUIT:           #and if user quits, the window will shut
          pygame.quit()
          quit()
            
        if event.type == pygame.KEYDOWN:       #what happens when keydown
          if event.key == pygame.K_LEFT:
            x_change = -7
        
          elif event.key == pygame.K_RIGHT:
            x_change = 7

          if event.key == pygame.K_p:
            pause = True
            print('Letter P pressed')
            paused()

        if event.type == pygame.KEYUP:            #or when keyup
          if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0


        

      x += x_change                           #update x_change

      col = loop_background()
      gamedisplay.fill(col)                   #fill background color
        
      player_score(score)
      
      things(thing_startx, thing_starty, thing_width, thing_height, red)
      things2(thing_startx2, thing_starty2, thing_width2, thing_height2, green)
      
      
      thing_starty += thing_speed
      thing_starty2 += thing_speed2
      
      if vc1 == True:
        arrow(x,y)                                #call fun of object with x,y
      elif vc2 == True:
        arrow(x,y-18)
      elif vc3 == True:
        arrow(x,y)
      elif vc4 == True:
        arrow(x,y)
      elif vc5 == True:
        arrow(x,y-34)
      things_dodged(dodged)

      font = pygame.font.SysFont('comicsansms', 15)
      text = font.render('P - Pause',True,black)
      gamedisplay.blit(text,(12,75))


      

      if (x-20) > width - arrow_width  or (x+20) < 0:     #if object hits edge, you crash
        crash()                   #and call crash
        

      if thing_starty > height:
        thing_starty = 0 - thing_height
        thing_startx = random.randrange(0,width)
        dodged += 1
        score += 2
        thing_speed += 0.2

      if thing_starty2 > height:
        thing_starty2 = 0 - thing_height2 + 20
        thing_startx2 = random.randrange(0,width)
        
        thing_speed2 += 0.1


      if y < thing_starty2+thing_height2:

        if (x-5) > thing_startx2 and (x+5) < thing_startx2+thing_width2 or (x-5) + arrow_width > thing_startx2 and (x+5)+arrow_width < thing_startx2+thing_width2:
          score += 3
          thing_starty2 -=  height
          thing_startx2 = random.randrange(0,width)
          green_boxes += 1
      
        
      if y < thing_starty+thing_height:
        if (x-20) > thing_startx and (x+20) < thing_startx+thing_width or (x-20) + arrow_width > thing_startx and (x+20)+arrow_width < thing_startx+thing_width:
                                      
                                      crash()

      
      things3(thing_startx3, thing_starty3, thing_width3, thing_height3, red)
      thing_starty3 += thing_speed3
        
      if thing_starty3 > height:
        thing_starty3 = 0 - thing_height3
        thing_startx3 = random.randrange(0,width)
        dodged += 1
        score += 2
        thing_speed3 += 0.3
          
      if y < thing_starty3 + thing_height3:
        if (x-20) > thing_startx3 and (x+20) < thing_startx3+thing_width3 or (x-20) + arrow_width > thing_startx3 and (x+20)+arrow_width < thing_startx3+thing_width3:
          crash()
      
      if dodged > 9:
        well()
        
              
         

      
      pygame.display.update()                   #show everything on display
      clock.tick(60)                            #60 fps
  game_into()
  game_loop()                                   #call game_loop
  pygame.quit()
  quit()                                          #quit

start()

