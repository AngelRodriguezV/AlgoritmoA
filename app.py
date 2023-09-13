import pygame as pg
import pygame.gfxdraw as pgfw
import sys

from settings import *

from algoritmoA import AlgoritmoA

from data.myDataTest1 import *

class Motor2D:

    def __init__(self, mapa, inicio, meta) -> None:
        pg.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption("Arbol")

        self.clock = pg.time.Clock()
        self.running = True

        self.mapa = mapa
        self.meta = meta
        self.inicio = inicio
        self.x = 0
        self.y = 0
        self.algoritmo = AlgoritmoA(mapa, inicio, meta)
        self.algoritmo.resolver()
        self.coordenadas = self.algoritmo.resultado()
        self.n = 0
        self.t = 0

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        poss = self.coordenadas[self.n]
        self.x = (poss[1]*100)+55
        self.y = (poss[0]*100)+55
        self.t += 1
        if self.t == 62:
            self.t = 0
            if self.n != len(self.coordenadas)-1:
                self.n += 1
            else:
                self.n = 0


    def render(self):
        self.screen.fill(BG_COLOR)

        for i in range(0,len(self.mapa)):
            for j in range(0,len(self.mapa[i])):
                contorno = pg.Rect((j*100)+5,(i*100)+5,100,100)
                cubo = pg.Rect((j*100)+10,(i*100)+10,90,90)
                pgfw.box(self.screen,contorno,BLACK)
                if self.mapa[i][j] == 0:
                    pgfw.box(self.screen,cubo,WHITE)
        pgfw.filled_circle(self.screen, (self.meta[1]*100)+55, (self.meta[0]*100)+55, 45, RED)
        pgfw.filled_circle(self.screen, self.x, self.y, 45, GREEN)
        
        pg.display.flip()

    def run(self):
        while self.running:
            self.event()
            self.update()
            self.render()
            self.clock.tick(60)
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    app = Motor2D(MAPA, INICIO, META)
    print(app.algoritmo.closedSet)
    print(" ")
    print(app.coordenadas)
    app.run()
