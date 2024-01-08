import pyxel

pyxel.init(700,500)

class Grape:
    speed = 4.5
    def __init__(self):
        self.restart()
   
    def move(self):
        self.x += self.vx * Grape.speed
        self.y += self.vy * Grape.speed

    def restart(self):
        self.x = pyxel.rndi(0, 700)  
        self.y = pyxel.rndi(-500, 0)
        self.vx = pyxel.cos(90)
        self.vy = pyxel.sin(90)

class Apple:
    speed = 4
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
    speed = 6
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
    speed = 5.5
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
        self.rock_count = 1

        self.score = 0
        self.fale = 0
        self.pad = Pad()

        self.grape=1
        self.grape1 = Grape()
        self.grape2 = Grape()
        self.grape3 = Grape()
        self.grape4 = Grape()
        self.grape5 = Grape()
        self.grape6 = Grape()
        self.grape7 = Grape()
        self.grapes = [self.grape1, self.grape2, self.grape3, 
        self.grape4, self.grape5, self.grape6, self.grape7]


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

        self.rocks = [self.rock1, self.rock2, self.rock3, 
        self.rock4, self.rock5, self.rock6, self.rock7, 
        self.rock8]


        pyxel.load("test.pyxres")
        pyxel.play(2, 6, loop= True)
        self.bgm_delete_flag = True

        pyxel.run(self.update, self.draw)

      


    def update(self):
        if self.score % 40 == 0 and self.score != 0:
            self.add_rock()

        if self.score == 20:
            Rock.speed == 0.05
        if self.score == 40:
            Rock.speed += 0.05
        if self.score == 60:
            Rock.speed += 0.05
        if self.score == 80:
            Rock.speed += 0.05


        for g in self.grapes:
            g.move()
            if 390 <= g.y <= 410 and self.pad.x <= g.x <= self.pad.x+100 :
                pyxel.playm(0, loop= False)
                self.score += 1
                g.restart()    
                if self.score % 10 == 0:
                    Grape.speed += 1          
            if g.y >= 500 :
                g.restart()

        for a in self.apples:
            a.move()
            if 390 <= a.y <= 410 and self.pad.x <= a.x <= self.pad.x+100 :
                pyxel.playm(0, loop= False)
                self.score += 1   
                a.restart()  
                if self.score % 10 == 0:
                    Apple.speed += 1   
            if a.y >= 500 :
                a.restart()

        for k in self.kiwis:
            k.move()
            if 390 <= k.y <= 410 and self.pad.x <= k.x <= self.pad.x+100 :
                pyxel.playm(0, loop= False)
                self.score += 1   
                k.restart()  
                if self.score % 10 == 0:
                    Kiwi.speed += 1    
            if k.y >= 500 :
                k.restart()

        for o in self.orenges:
            o.move()
            if 390 <= o.y <= 410 and self.pad.x <= o.x <= self.pad.x+100 :
                pyxel.playm(0, loop= False)
                self.score += 1
                o.restart() 
                if self.score % 10 == 0:
                    Orenge.speed += 1    
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
            if self.score % 20 == 0:
                self.rock += 10              

        if pyxel.btn(pyxel.KEY_LEFT):
            self.pad.x += -10
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.pad.x += 10  

    def add_rock(self):
            new_rock = Rock()
            self.rocks.append(new_rock)
            self.rock_count += 1





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
            for g in self.grapes:
                g.x = 0
                g.y = 0

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
        
            for g in self.grapes:
                g.x = 0
                g.y = 0

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
            for g in self.grapes:
                pyxel.blt(g.x, g.y,1,0,32,20,18,13)
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
            for r in self.rocks[:self.rock_count]:
                pyxel.blt(r.x, r.y, 1, 28, 40, 20, 18, 7)
        

        pyxel.blt(self.pad.x,406, 0, 0, 0,100, 94, 10)    


App()