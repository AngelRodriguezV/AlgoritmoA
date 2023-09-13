import numpy as np

class AlgoritmoA:

    def __init__(self, mapa, inicio, meta) -> None:
        self.openSet = [] # Almacena las casillas por evaluar
        self.closedSet = [] # Almacena las casillas evaluadas
        self.mapa = mapa
        self.inicio = inicio
        self.meta = meta
        self.peso = 0

    def heuristica(self, p1, p2):
        return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
    
    def isEmptyClosedSet(self, poss):
        if len(self.closedSet) == 0:
            return False
        for l in self.closedSet:
            if l[0] == poss[0] and l[1] == poss[1]:
                return True
        return False

    def isEmptyOpenSet(self, poss):
        if len(self.openSet) == 0:
            return False
        for l in self.openSet:
            if l[0] == poss[0] and l[1] == poss[1]:
                return True
        return False

    def addOpenSet(self, poss, peso, poss_init=(0,0)):
        aux = np.zeros(7, dtype='uint8')
        aux[0] = poss[0]
        aux[1] = poss[1]
        aux[2] = peso
        aux[3] = self.heuristica(poss, self.meta)
        aux[4] = peso + aux[3]
        aux[5] = poss_init[0]
        aux[6] = poss_init[1]
        self.openSet.append(aux)
    
    def addClosedSet(self):
        pass

    def evaluarCasillas(self, data):
        listPosition = []
        if (data[0] - 1) >= 0:
            listPosition.append((data[0] - 1, data[1]))
        if (data[0] + 1) < len(self.mapa):
            listPosition.append((data[0] + 1, data[1]))
        if (data[1] - 1) >= 0:
            listPosition.append((data[0], data[1] - 1))
        if (data[1] + 1) < len(self.mapa[0]):
            listPosition.append((data[0], data[1] + 1))
        for position in listPosition:
            if self.mapa[position[0]][position[1]] != 1:
                if (not self.isEmptyOpenSet(position)) and (not self.isEmptyClosedSet(position)):
                    self.addOpenSet(poss=position, peso=data[2]+1, poss_init=(data[0],data[1]))


    def resolver(self): 
        # Agregar inicio a openset
        self.addOpenSet(poss=self.inicio, peso=0)
        # Bucle para repetir los pasos
        while True:
            # Tomar la casilla con menor costo total
            self.openSet = sorted(self.openSet, key=lambda tupla: tupla[4])
            casilla = self.openSet.pop(0)
            # Verificar que la casilla seleccionada sea diferente de la meta
            if self.heuristica((casilla[0],casilla[1]), self.meta) != 0:
                # Evaluar las casillas vecinas
                self.evaluarCasillas(casilla)
            # Verificar si el costo es menor al anterior elemento  agregado a closedSet
            if len(self.closedSet) != 0:
                last = self.closedSet[-1]
                if casilla[4] < last[4]:
                    casilla[5] = last[0]
                    casilla[6] = last[1]
            # Pasar a closedSet la casilla evaluada
            self.closedSet.append(casilla)
            # Para si la heuristica es 0
            if self.heuristica((casilla[0],casilla[1]), self.meta) == 0:
                return

    def resultado(self):
        listResult = []
        hijo = self.closedSet[-1]
        listResult.append((hijo[0],hijo[1]))
        terminar = True
        while terminar:
            if hijo[0] == self.inicio[0] and hijo[1] == self.inicio[1]:
                terminar = False
            else:
                for padre in self.closedSet:
                    if padre[0] == hijo[5] and padre[1] == hijo[6]:
                        listResult.append((padre[0],padre[1]))
                        hijo = padre
                        break
        listOrd = listResult[::-1]
        return listOrd
