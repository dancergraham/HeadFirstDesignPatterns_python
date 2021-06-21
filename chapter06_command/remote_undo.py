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
