#uso de clase y superlclase
class Car:
    def __init__(self,model,color):
        self.model=model
        self.color=color

    def printDetails(self):
        print(self.model)
        print(self.color)


class SedanEngine:
    def start(self):
        print("Car has started")
    def stop(self):
        print("Car has stopped")
    # write your class definition


class Sedan(Car):
    def __init__(self,model,color):
        super().__init__(model,color)
        self.engine=SedanEngine()
    
    def setStart(self):
        self.engine.start()
    
    def setStop(self):
        self.engine.stop()

carroNuevo=Sedan("vocho","rojo")
carroNuevo.printDetails()
carroNuevo.setStart()
carroNuevo.setStop()
