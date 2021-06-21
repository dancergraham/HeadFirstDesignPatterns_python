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
        self.level = self.light.get_level()
        self.light.on()
 
    def undo(self):
        self.light.dim(self.level)


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.level = self.light.get_level()
        self.light.off()
 
    def undo(self):
        self.light.dim(self.level)


class Light():
    def __init__(self, location:str):
        self.location = location
        self.level = 0

    def on(self):
        self.level = 100
        print("Light is on")

    def off(self):
        self.level = 0
        print("Light is off")

    def dim(self, level):
        self.level = level
        if self.level == 0:
            self.off()
        else:
            print(f"Light is dimmed to {self.level}%")
    
    def get_level(self):
        return self.level


class RemoteControlWithUndo():
    """The Invoker"""

    def __init__(self) -> None:
        self.on_commands = [NoCommand() for _ in range(7)]
        self.off_commands = [NoCommand() for _ in range(7)]
        self.undo_command = NoCommand()

    def set_command(self, i, on_command, off_command):
        self.on_commands[i] = on_command
        self.off_commands[i] = off_command

    def on_button_was_pushed(self, i):
        self.on_commands[i].execute()
        self.undo_command = self.on_commands[i]

    def off_button_was_pushed(self, i):
        self.off_commands[i].execute()
        self.undo_command = self.off_commands[i]

    def undo_button_was_pushed(self):
        self.undo_command.undo()

    def __str__(self) -> str:
        buffer = []
        buffer.append("\n------ Remote Control -------\n")
        for i, (on_command, off_command) in enumerate(zip(self.on_commands, self.off_commands)):
            buffer.append(f"[slot {i}] {on_command.__class__.__name__}" +
				f"    {off_command.__class__.__name__}\n")
		
        buffer.append(f"[undo] {self.undo_command.__class__.__name__}\n")
        return "".join(buffer)


def remote_loader():
    remoteControl =  RemoteControlWithUndo()
    living_room_light =  Light("Living Room")
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    remoteControl.set_command(0, living_room_light_on, living_room_light_off)

    remoteControl.on_button_was_pushed(0)
    remoteControl.off_button_was_pushed(0)
    print(remoteControl)
    remoteControl.undo_button_was_pushed()
    remoteControl.off_button_was_pushed(0)
    remoteControl.on_button_was_pushed(0)
    print(remoteControl)
    remoteControl.undo_button_was_pushed()

if __name__ == '__main__':
    remote_loader()