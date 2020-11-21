import random # For generating random numbers
import sys # We will use sys.exit to exit the program
import pygame
from pygame.locals import * # Basic pygame imports

# Global Variables for the game
FPS = 32
SCREENWIDTH = 700
SCREENHEIGHT = 400
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
sonic2={}

def dispobj(pl):
    if pl['level']==0:
        pl['py']=75
        try:
            SCREEN.blit(obj[pl['dis']][pl['img']][pl['point']],(pl['px'],75))
            pl['point']+=1
            
        except IndexError:
            SCREEN.blit(obj[pl['dis']][pl['img']][0],(pl['px'],75))
            pl['point']=1
            
    else:
        try:
            SCREEN.blit(obj[pl['dis']][pl['img']][pl['point']],(pl['px'],275-obj[pl['dis']][pl['img']][pl['point']].get_height()))
            pl['point']+=1
            pl['py']=275-obj[pl['dis']][pl['img']][pl['point']].get_height()
        except IndexError:
            SCREEN.blit(obj[pl['dis']][pl['img']][0],(pl['px'],275-obj[pl['dis']][pl['img']][0].get_height()))
            pl['point']=1
            pl['py']=275-obj[pl['dis']][pl['img']][0].get_height()
        
def takegams(err=0):
    level=random.randrange(0,2)
    d=2
    img=random.randrange(0,5)
    
    objx=SCREENWIDTH+200+err
    return {'dis':d,'img':img,'px':objx,'py':75,'level':level,'point':0,'colu':0}
def takeobject(err=0):
    
    level=random.randrange(0,2)
      #for star,coin 
    if level==0:
        
        d=random.randrange(0,2)
        if d==0:
            img=random.randrange(0,3)
        else:
            img=random.randrange(0,4)
    else:
        d=random.randrange(0,2)
        if d==0:
            img=random.randrange(0,3)
        else:
            img=random.randrange(3,6)
        
    objx=SCREENWIDTH+200+err
    return {'dis':d,'img':img,'px':objx,'py':75,'level':level,'point':0,'colu':0}

def collid (py,r,p,pl,trans):
    if trans==0:
        if (100<(pl['px'])<(100+sonic2[r][p].get_width()))and(pl['py']<py<(pl['py']+obj[pl['dis']][pl['img']][0].get_height())):
            return True
        if ((100<(pl['px'])<(100+sonic2[r][p].get_width()))or (100<(pl['px']+obj[pl['dis']][pl['img']][0].get_width())<(100+sonic2[r][p].get_width())))and (r==0 or r==1 or r==3)and(pl['level']==1):
            return True
    elif trans==1:
        if (100<(pl['px'])<(100+super2[r][p].get_width())) and(pl['py']<=py<=(pl['py']+obj[pl['dis']][pl['img']][0].get_height())):
            return True
        if (100<(pl['px'])<(100+super2[r][p].get_width())) and (pl['py']<=(py+super2[r][p].get_height())<=(pl['py']+obj[pl['dis']][pl['img']][0].get_height())):
            return True
    elif trans==2:
        if (100<(pl['px'])<(100+white2[r][p].get_width())) and(pl['py']<=py<=(pl['py']+obj[pl['dis']][pl['img']][0].get_height())):
            return True
        if (100<(pl['px'])<(100+white2[r][p].get_width())) and (pl['py']<=(py+white2[r][p].get_height())<=(pl['py']+obj[pl['dis']][pl['img']][0].get_height())):
            return True
    if trans==3:
        if (100<(pl['px'])<(100+red2[r][p].get_width()))and(pl['py']<py<(pl['py']+obj[pl['dis']][pl['img']][0].get_height())):
            return True
        if ((100<(pl['px'])<(100+red2[r][p].get_width()))or (100<(pl['px']+obj[pl['dis']][pl['img']][0].get_width())<(100+red2[r][p].get_width())))and (r==0 or r==1 or r==3)and(pl['level']==1):
            return True
    #elif  (pl['level']==1) and ((100+sonic2[r][p].get_width())>(pl['px']+obj[pl['dis']][pl['img']][0].get_width())>100) and (pl['py']<(py+sonic2[r][p].get_height())<=(pl['py']+obj[pl['dis']][pl['img']][0].get_height())):
     #   return True
    return False



def maingame():
    run=False
    #for background
    b1=background
    x=0
    y=0
    #for bar
    bar_p=0
    power=0
    score=0
    term=1
    #for gams
    gams=1
    #for sonic
    trans=0
    transformation=False
    p=-1
    roll=False
    r=0
    n=10
    px=100
    py=275-sonic2[r][p].get_height()
    #super
    down=False
    up=False
    #objects
    p1=takeobject()

    p2=takeobject()
    p2['px']=p1['px']+275
    p3=takeobject()
    p3['px']=p2['px']+275
    p4=takeobject()
    p4['px']=p3['px']+275
    
    while 1:
       
        for i in range(1,n):
            x-=1

            SCREEN.blit(b1,(x,y))
            SCREEN.blit(b1,(x+b1.get_width(),y))
            if x==-b1.get_width():
                x=0        
        for event in pygame.event.get():
            if term==1 and transformation== False:
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                
                elif event.type == KEYDOWN and ( event.key == K_DOWN):
                    if trans==0 or trans==3 :
                        roll=True
                        p=0
                        r=1
                        n=60
                    elif trans==1 or 2 :
                        down=True
                        up=False
                        r=0
                        term=0
                    

                elif event.type == KEYDOWN and (event.key == K_KP_ENTER):#
                    run=True
                    r=0
                elif event.type ==KEYDOWN and (event.key ==K_RIGHT):
                    if trans==0 or trans==3:
                        run=True
                        r=3
                        if trans==0:
                            p=-1
                        else:
                            p=0
                    elif trans==1:
                        r=1
                        p=0
                        n=30
                        term=0
                    elif trans==2:
                        if py==75:
                            r=2
                        else:
                            r=1
                            py=275-white2[r][0].get_height()
                        p=0
                        n=30
                        term=0

                elif event.type == KEYUP and (event.key == K_DOWN):#
                    if trans==0 or trans==3 :
                        roll=False
                        n=15
                        if trans==0:
                            p=15
                        else:
                            p=13
                        
                elif event.type==KEYDOWN and (event.key ==K_UP):
                    if trans==0 or trans==3 :
                        run=False
                        r=2
                        n=25
                        p=0
                        px=100
                        py=275-sonic2[r][p].get_height()
                        term=0
                    elif trans==1 or 2 :
                        up=True
                        down=False
                        term=0
                    
        if p1['px']<=-200:
            err=p1['px']+200
            p1=p2
            p2=p3
            p3=p4
            if (gams%2)==0:
                p4=takegams(err)
                gams+=1
            else:
                p4=takeobject(err)
                gams+=1
        
        p1['px']-=n-5
        p2['px']-=n-5
        p3['px']-=n-5
        p4['px']-=n-5
        
        dispobj(p1)
        dispobj(p2)
        dispobj(p3)
        dispobj(p4)
        
        if trans==0 and transformation==False:   
            if run==True:     #run&roll

                p+=1
                SCREEN.blit(sonic2[r][p],(100,275-sonic2[r][p].get_height()))
                if r==0 and p==21:
                    p=14
                if roll ==True and p==14 :
                    p=11
                if roll==False and p==38 :
                    r=0
                    p=14
                if run==True and p==13 and r==3:
                    n=40
                if run ==True and p==22 and r==3:
                    r=0
                    p=14
                    n=15
                #pygame.display.update()
                pygame.time.delay(80)  
            if r==2:#jump
                try:
                    SCREEN.blit(sonic2[r][p],(px,py))
                except IndexError:
                    SCREEN.blit(sonic2[r][0],(px,py))
                    p=0
                #pygame.display.update()
                pygame.time.delay(80)
                p+=1
                if p<6:
                    py-=33
                else:
                    py+=33
                if p==9:
                    r=0
                    run=True
                    n=15
                    term=1
        elif trans==1 and transformation==False: 
            SCREEN.blit(super2[r][p],(100,py))
            pygame.time.delay(80)
            p+=1 
            if r==0:
                if p>6:
                    p=0
            if down==True and r==0 :
                if (py+super2[r][p].get_height())<275:
                    py+=33
                    p=7
                else:
                    py=275-super2[r][p].get_height()
                    down=False
                    term=1
            if up==True and r==0:
                if py>75:
                    py-=33
                    p=7
                else:
                    py=75
                    up=False
                    term=1
            if r==1:
                if p>8:
                    r=0
                    p=0
                    n=15
                    term=1

        elif trans==2 and transformation==False:        
            SCREEN.blit(white2[r][p],(100,py))
            pygame.time.delay(80)
            p+=1
            if r==0:
                if p>8:
                    p=4
            if down==True and r==0 :
                if (py+white2[r][p].get_height())<275:
                    py+=33
                    p=7
                else:
                    py=275-white2[r][p].get_height()
                    down=False
                    term=1
            if up==True and r==0:
                if py>75:
                    py-=33
                    p=7
                else:
                    py=75
                    up=False
                    term=1
            if r==2 and p>9:
                r=0
                p=2
                n=15
                term=1
            if r==1 :
                if p>11:
                    r=0
                    p=0
                    term=1
                    n=15
                py=275-white2[r][p].get_height()


        elif trans==3 and transformation==False:   
            if run==True:     #run&roll
                SCREEN.blit(red2[r][p],(100,270-sonic2[r][p].get_height()))
                p+=1
                if r==0 and p==8:
                    p=0
                if roll ==True and p==13 :
                    p=11
                    n=60
                if roll==False and p==21 :
                    r=0
                    n=15
                    p=0
                
                if run ==True and p==8 and r==3:
                    r=0
                    p=0
                    n=15
                #pygame.display.update()
                pygame.time.delay(100)  
            if r==2:#jump
                try:
                    SCREEN.blit(red2[r][p],(px,py))
                except IndexError:
                    SCREEN.blit(red2[r][0],(px,py))
                    p=0
                #pygame.display.update()
                pygame.time.delay(80)
                p+=1
                if p<6:
                    py-=33
                else:
                    py+=33
                if 8<p<12:
                    py=275-red2[r][p].get_height()
                if p==12:
                    r=0
                    p=0
                    run=True
                    n=15
                    term=1




        if transformation==True:
            if trans==0:
                try:
                    SCREEN.blit(sonic2[4][p],(100,py))
                    pygame.time.delay(80)
                    p+=1
                except IndexError:
                    p=0
                    trans+=1
                    n=15
                    r=0
                    px=100
                    term=1
                    transformation=False
            elif trans==1:
                try:
                    SCREEN.blit(super2[2][p],(100,py))
                    pygame.time.delay(100)
                    p+=1
                except IndexError:
                    p=0
                    trans+=1
                    n=15
                    term=1
                    transformation=False
            elif trans==2:
                try:
                    SCREEN.blit(white2[3][p],(100,py))
                    pygame.time.delay(80)
                    p+=1
                except IndexError:
                    p=0
                    r=0
                    run=True
                    term=1
                    trans+=1
                    n=15
                    transformation=False


        if bar_p<0:
            bar_p=0
        if bar_p>3:
            bar_p=3
        if power>4:
            power=0
            n=6
            transformation=True
            p=0
            

        SCREEN.blit(bars[0][bar_p],(50,10))
        SCREEN.blit(bars[1][power],(500,20))
        SCREEN.blit(obj[4],(500,50))
        s=str(score)
        n1=len(s)
        i=0
        while n1>0:
            SCREEN.blit(obj[3][int(s[i])],(530+11*i,55))
            n1-=1
            i+=1

        pygame.display.update()
        if p2['colu']==0 and transformation==False:
            if collid(py,r,p,p2,trans)==True:
                if p2['dis']==0:
                    p2['img']=3
                    bar_p-=1
                    score+=1
                    p2['colu']=1
                elif p2['dis']==2:
                    p2['img']=3
                    p2['dis']=0
                    p2['colu']=1
                    power+=1
                else:
                    p2['img']=6
                    bar_p+=1
                    p2['colu']=1
                    
            
            #pygame.time.delay(50)   
        
        

if __name__ == "__main__":
    # This will be the main point from where our game will start
    pygame.init() # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    background=pygame.image.load('backgrounds/sky.jpg').convert_alpha()
    sonic2=[
        [pygame.image.load('sonic/sonic/run/1.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/2.png').convert_alpha(),
        pygame.image.load('sonic/sonic/run/3.png').convert_alpha(),
        pygame.image.load('sonic/sonic/run/4.png').convert_alpha(),
        pygame.image.load('sonic/sonic/run/5.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/6.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/7.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/8.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/9.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/10.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/11.png').convert_alpha(),
        pygame.image.load('sonic/sonic/run/12.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/13.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/14.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/15.png').convert_alpha(),
        pygame.image.load('sonic/sonic/run/16.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/17.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/18.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/19.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/20.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/21.gif').convert_alpha(),
        pygame.image.load('sonic/sonic/run/22.gif').convert_alpha()],
        [pygame.image.load(f'sonic/sonic/roll/{str(i)}.png').convert_alpha() for i in range(1,40)],
        [pygame.image.load(f'sonic/sonic/fly/{str(i)}.png').convert_alpha() for i in range(1,10)],
        [pygame.image.load(f'sonic/sonic/attack/{str(i)}.png').convert_alpha() for i in range(1,24)],
        [pygame.image.load(f'sonic/sonic/tras2/{str(i)}.png').convert_alpha() for i in range(1,23)]
    ]

    super2=[
        [pygame.image.load(f'sonic/super/fly/{str(i)}.png').convert_alpha() for i in range(1,9)],
        [pygame.image.load(f'sonic/super/attack/{str(i)}.png').convert_alpha() for i in range(1,10)],
        [pygame.image.load(f'sonic/super/tras3/{str(i)}.png').convert_alpha() for i in range(1,10)]
    ]

    white2=[
        [pygame.image.load(f'sonic/white/fly/{str(i)}.gif').convert_alpha() for i in range(1,11)],
        [pygame.image.load(f'sonic/white/run/{str(i)}.gif').convert_alpha() for i in range(1,13)],
        [pygame.image.load(f'sonic/white/attack/{str(i)}.gif').convert_alpha() for i in range(1,11)],
        [pygame.image.load(f'sonic/white/trans4/{str(i)}.png').convert_alpha() for i in range(1,4)]

    ]
    
    red2=[
        [pygame.image.load(f'sonic/red/run/{str(i)}.png').convert_alpha() for i in range(1,9)],
        [pygame.image.load(f'sonic/red/roll/{str(i)}.png').convert_alpha() for i in range(1,22)],
        [pygame.image.load(f'sonic/red/fly/{str(i)}.png').convert_alpha() for i in range(1,13)],
        [pygame.image.load(f'sonic/red/attack/{str(i)}.png').convert_alpha() for i in range(1,11)]
    ]
    obj=[
        [[pygame.image.load(f'backgrounds/coin/ring/{str(i)}.png').convert_alpha() for i in range(1,9)],
        [pygame.image.load(f'backgrounds/coin/rcoin/{str(i)}.gif').convert_alpha() for i in range(1,7)],
        [pygame.image.load(f'backgrounds/coin/star/{str(i)}.png').convert_alpha() for i in range(1,7)],
        [pygame.image.load(f'backgrounds/coin/shin/{str(i)}.png').convert_alpha() for i in range(1,7)]
        ],#0
        [
        [pygame.image.load(f'evils/boom/{str(i)}.png').convert_alpha() for i in range(1,7)],
        [pygame.image.load(f'evils/bugfly/{str(i)}.png').convert_alpha() for i in range(1,3)],
        [pygame.image.load(f'evils/bee/{str(i)}.png').convert_alpha() for i in range(1,3)],
        [pygame.image.load(f'evils/bital/{str(i)}.png').convert_alpha() for i in range(1,4)],
        [pygame.image.load(f'evils/ant/{str(i)}.png').convert_alpha() for i in range(1,4)],
        [pygame.image.load(f'evils/scorp/{str(i)}.png').convert_alpha() for i in range(1,4)],
        [pygame.image.load(f'backgrounds/expl/{str(i)}.png').convert_alpha() for i in range(1,13)]
        ],#1
        [
        [pygame.image.load(f'backgrounds/gams/hart/{str(i)}.png').convert_alpha() for i in range(1,13)],
        [pygame.image.load(f'backgrounds/gams/blue/{str(i)}.png').convert_alpha() for i in range(1,16)],
        [pygame.image.load(f'backgrounds/gams/diamond/{str(i)}.png').convert_alpha() for i in range(1,16)],
        [pygame.image.load(f'backgrounds/gams/green/{str(i)}.png').convert_alpha() for i in range(1,16)],
        [pygame.image.load(f'backgrounds/gams/yellow/{str(i)}.png').convert_alpha() for i in range(1,15)]
        ],#2
        [pygame.image.load(f'backgrounds/numbers/{str(i)}.png').convert_alpha() for i in range(0,10)],#3
        pygame.image.load('backgrounds/score.png').convert_alpha() #4

    ]
    bars=[
    
        [pygame.image.load(f'backgrounds/bar/{str(i)}.png').convert_alpha() for i in range(1,5)],
        [pygame.image.load(f'backgrounds/bar2/{str(i)}.png').convert_alpha() for i in range(1,6)]
    ]

    while 1:
        maingame()
    
       