import pyxel

pyxel.init(700,500)

class Ball:
    speed = 5
    def __init__(self):
        self.restart()
   
    def move(self):
        self.x += self.vx * Ball.speed
        self.y += self.vy * Ball.speed

    def restart(self):
        self.x = pyxel.rndi(0, 700)  
        self.y = pyxel.rndi(-500, 0)
        self.vx = pyxel.cos(90)
        self.vy = pyxel.sin(90)

class Apple:
    speed = 5
    def __init__(self):
        self.restart()
   
    def move(self):
        self.x += self.vx * Apple.speed
        self.y += self.vy * Apple.speed

    def restart(self):
        self.x = pyxel.rndi(0, 700)  
        self.y = pyxel.rndi(-500, 0)
        self.vx = pyxel.cos(90)
        self.vy = pyxel.sin(90)

class Kiwi:
    speed = 5
    def __init__(self):
        self.restart()
   
    def move(self):
        self.x += self.vx * Kiwi.speed
        self.y += self.vy * Kiwi.speed

    def restart(self):
        self.x = pyxel.rndi(0, 700)  
        self.y = pyxel.rndi(-500, 0)
        self.vx = pyxel.cos(90)
        self.vy = pyxel.sin(90)

class Orenge:
    speed = 5
    def __init__(self):
        self.restart()
   
    def move(self):
        self.x += self.vx * Orenge.speed
        self.y += self.vy * Orenge.speed

    def restart(self):
        self.x = pyxel.rndi(0, 700)  
        self.y = pyxel.rndi(-500, 0)
        self.vx = pyxel.cos(90)
        self.vy = pyxel.sin(90)


class Star:
    speed = 5
    def __init__(self):
        self.restart()
   
    def move(self):
        self.x += self.vx * Star.speed
        self.y += self.vy * Star.speed

    def restart(self):
        self.x = pyxel.rndi(0, 700)  
        self.y = pyxel.rndi(-500, 0)
        angle = pyxel.rndi(30, 150)   
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)

class Rock:
    speed = 5
    def __init__(self):
        self.restart()
   
    def move(self):
        self.x += self.vx * Rock.speed
        self.y += self.vy * Rock.speed

    def restart(self):
        self.x = pyxel.rndi(0, 700)  
        self.y = pyxel.rndi(-500, 0)  
        self.vx = pyxel.cos(90)
        self.vy = pyxel.sin(90)

class Pad:
    w=20
    h=10
    y = 200
    x = 0



class App:
    def __init__(self):
        self.score = 0
        self.fale = 0
        self.pad = Pad()

        self.ball=1
        self.ball1 = Ball()
        self.ball2 = Ball()
        self.ball3 = Ball()
        self.ball4 = Ball()
        self.ball5 = Ball()
        self.ball6 = Ball()
        self.ball7 = Ball()
        self.balls = [self.ball1, self.ball2, self.ball3, 
        self.ball4, self.ball5, self.ball6, self.ball7]


        self.apple=1
        self.apple1 = Apple()
        self.apple2 = Apple()
        self.apple3 = Apple()
        self.apple4 = Apple()
        self.apple5 = Apple()
        self.apple6 = Apple()
        self.apple7 = Apple()
        self.apples = [self.apple1, self.apple2, self.apple3, 
        self.apple4, self.apple5, self.apple6, self.apple7]


        self.kiwi=1
        self.kiwi1 = Kiwi()
        self.kiwi2 = Kiwi()
        self.kiwi3 = Kiwi()
        self.kiwi4 = Kiwi()
        self.kiwi5 = Kiwi()
        self.kiwi6 = Kiwi()
        self.kiwi7 = Kiwi()
        self.kiwis = [self.kiwi1, self.kiwi2, self.kiwi3, 
        self.kiwi4, self.kiwi5, self.kiwi6, self.kiwi7]


        self.orenge=1
        self.orenge1 = Orenge()
        self.orenge2 = Orenge()
        self.orenge3 = Orenge()
        self.orenge4 = Orenge()
        self.orenge5 = Orenge()
        self.orenge6 = Orenge()
        self.orenge7 = Orenge()
        self.orenges = [self.orenge1, self.orenge2, self.orenge3, 
        self.orenge4, self.orenge5, self.orenge6, self.orenge7]

        self.satr=1
        self.star1 = Star()
        self.stars = [self.star1]


        self.rock=1
        self.rock1 = Rock()
        self.rock2 = Rock()
        self.rock3 = Rock()
        self.rock4 = Rock()
        self.rock5 = Rock()
        self.rock6 = Rock()
        self.rock7 = Rock()
        self.rock8 = Rock()
        self.rock9 = Rock()
        self.rock10 = Rock()
        self.rock11 = Rock()
        self.rock12 = Rock()
        self.rock13 = Rock()
        self.rock14 = Rock()
        self.rock15 = Rock()
        self.rock16 = Rock()
        self.rock17 = Rock()
        self.rock18 = Rock()


        self.rocks = [self.rock1, self.rock2, self.rock3, 
        self.rock4, self.rock5, self.rock6, self.rock7, 
        self.rock8, self.rock9, self.rock10, self.rock11,
        self.rock12, self.rock13, self.rock14, self.rock15,
        self.rock16, self.rock17, self.rock18, ]

        pyxel.load("test.pyxres")
        pyxel.play(2, 6, loop= True)
        self.bgm_delete_flag = True

        pyxel.run(self.update, self.draw)

      


    def update(self):

        for i in self.balls:
            i.move()
            if 390 <= i.y <= 410 and self.pad.x <= i.x <= self.pad.x+100 :
                pyxel.playm(0, loop= False)
                self.score += 1
                i.restart()              
            if i.y >= 500 :
                i.restart()

        for a in self.apples:
            a.move()
            if 390 <= a.y <= 410 and self.pad.x <= a.x <= self.pad.x+100 :
                pyxel.playm(0, loop= False)
                self.score += 1   
                a.restart()  
            if a.y >= 500 :
                a.restart()

        for k in self.kiwis:
            k.move()
            if 390 <= k.y <= 410 and self.pad.x <= k.x <= self.pad.x+100 :
                pyxel.playm(0, loop= False)
                self.score += 1   
                k.restart()  
            if k.y >= 500 :
                k.restart()

        for o in self.orenges:
            o.move()
            if 390 <= o.y <= 410 and self.pad.x <= o.x <= self.pad.x+100 :
                pyxel.playm(0, loop= False)
                self.score += 1
                o.restart() 
            if o.y >= 500 :
                o.restart()


        for s in self.stars:
            s.move()
            if s.x >= 700 or s.x <= 0:
                s.vx = s.vx *-1
            if 390 <= s.y <= 410 and self.pad.x <= s.x <= self.pad.x+100 :
                pyxel.playm(1, loop= False)
                self.score += 5 
                s.restart()   
            if s.y >= 500 :
                s.restart()
                
       
        for r in self.rocks:
            r.move()
            if 390 <= r.y <= 410 and self.pad.x <= r.x <= self.pad.x+85 :
                self.fale +=1                
                r.restart()   
            if r.y >= 500 :
                r.restart()

        if self.score == 20:
            Ball.speed += 0.1
            Apple.speed += 0.1
            Orenge.speed += 0.1
            Kiwi.speed += 0.1
            Rock.speed += 0.1
        if self.score == 40:
            Ball.speed += 0.1
            Apple.speed += 0.1
            Orenge.speed += 0.1
            Kiwi.speed += 0.1
            Rock.speed += 0.1
        if self.score == 60:
            Ball.speed += 0.1
            Apple.speed += 0.1
            Orenge.speed += 0.1
            Kiwi.speed += 0.1
            Rock.speed += 0.1
        if self.score == 80:
            Ball.speed += 0.1
            Apple.speed += 0.1
            Orenge.speed += 0.1
            Kiwi.speed += 0.1
            Rock.speed += 0.1


        if pyxel.btn(pyxel.KEY_LEFT):
            self.pad.x += -10
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.pad.x += 10  




    def draw(self):
        if 0 <= self.score <= 19:
            pyxel.cls(7) 
            pyxel.text(10, 10,'Point : '+ str(self.score), 0)
        if 19 < self.score <= 39:
            pyxel.cls(6) 
            pyxel.text(10, 10,'Point : '+ str(self.score), 0)
        if 39 < self.score <= 59:
            pyxel.cls(5) 
            pyxel.text(10, 10,'Point : '+ str(self.score), 7)
        if 59 < self.score <= 79:
            pyxel.cls(1) 
            pyxel.text(10, 10,'Point : '+ str(self.score), 7)
        if 79 < self.score <= 100:
            pyxel.cls(0) 
            pyxel.text(10, 10,'Point : '+ str(self.score), 7)



        if  self.score >= 100:
            pyxel.cls(10)
            pyxel.blt(310, 230,2,0,24,70,17,5)                      
            for i in self.balls:
                i.x = 0
                i.y = 0

            for a in self.apples:
                a.x = 0
                a.y = 0  

            for s in self.stars:
                s.x = 0
                s.y = 0
           
            for k in self.kiwis:
                k.x = 0
                k.y = 0   
            
            for o in self.orenges:
                o.x = 0
                o.y = 0   
            
            for r in self.rocks:
                r.x = 0
                r.y = 0    

            if self.bgm_delete_flag:
                pyxel.stop(0)
                pyxel.stop(1)
                pyxel.stop(2)
                pyxel.playm(4, loop= False)
                self.bgm_delete_flag = False      
                        
            return


        if  self.fale >= 1:
            pyxel.cls(0)
            pyxel.blt(300, 230,2,0,0,111,17,10)
        
            for i in self.balls:
                i.x = 0
                i.y = 0

            for a in self.apples:
                a.x = 0
                a.y = 0  

            for s in self.stars:
                s.x = 0
                s.y = 0
           
            for k in self.kiwis:
                k.x = 0
                k.y = 0  
                 
            for o in self.orenges:
                o.x = 0
                o.y = 0   
            
            for r in self.rocks:
                r.x = 0
                r.y = 0      

            if self.bgm_delete_flag:
                pyxel.stop(0)
                pyxel.stop(1)
                pyxel.stop(2)
                pyxel.playm(3, loop= False)
                self.bgm_delete_flag = False         

            return


        
        else:
            for i in self.balls:
                pyxel.blt(i.x, i.y,1,0,32,20,18,13)

            for a in self.apples:
                pyxel.blt(a.x,a.y,1,0,0,20,20,13)    

            for s in self.stars:
                pyxel.blt(s.x, s.y,1,32,0,20,18,13)

            for k in self.kiwis:
                pyxel.blt(k.x, k.y,1,0,56,20,18,13)
            
            for o in self.orenges:
                pyxel.blt(o.x, o.y,1,8,77,20,20,13)            
            
            for r in self.rocks:
                pyxel.blt(r.x, r.y,1,28,40,20,18,7)
        

        pyxel.blt(self.pad.x,406, 0, 0, 0,100, 94, 10)    


App()