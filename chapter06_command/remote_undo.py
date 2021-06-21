import abc


class Command(abc.ABC):
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.level = self.light.getLevel()
        self.light.on()
 
    def undo(self):
        self.light.dim(self.level)


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.level = self.light.getLevel()
        self.light.off()
 
    def undo(self):
        self.light.dim(self.level)


class Light():
    def __init__(self, location:str):
        self.location = location

    def on(self):
        self.level = 100
        print("Light is on")

    def off(self):
        self.level = 0
        print("Light is off")

    def dim(self, level):
        self.level = level
        if level == 0:
            self.off()
        else:
            print(f"Light is dimmed to {self.level}%")
    
    def get_level(self):
        return self.level


