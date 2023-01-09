class Amplifier:
    def __init__(self, description):
        self.description = description
        self.tuner = None
        self.player = None

    def __str__(self):
        return self.description

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def set_stereo_sound(self):
        print(f"{self.description} stereo mode on")

    def set_surround_sound(self):
        print(f"{self.description} surround sound on (5 speakers, 1 subwoofer)")

    def set_volume(self, level):
        print(f"{self.description} setting volume to {level}")

    def set_tuner(self, tuner):
        print(f"{self.description} setting tuner to {tuner}")
        self.tuner = tuner

    def set_streaming_player(self, player):
        print(f"{self.description} setting Streaming player to {player}")
        self.player = player


class Tuner:
    def __init__(self, description, amplifier):
        self.description = description
        self.amplifier = amplifier
        self.frequency = None

    def __str__(self):
        return self.description

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def set_frequency(self, frequency):
        print(f"{self.description} setting frequency to {frequency}")
        self.tuner = frequency

    def set_am(self):
        print(f"{self.description} setting AM mode")

    def set_fm(self):
        print(f"{self.description} setting FM mode")


class HomeTheaterFacade:

    def __init__(self, amp, tuner,
                 # player,
                 # projector,
                 # screen,
                 # lights,
                 # popper
                 ):
        self.amp = amp
        self.tuner = tuner
        # self.player = player
        # self.projector = projector
        # self.screen = screen
        # self.lights = lights
        # self.popper = popper

    def watchMovie(self, movie):
        print("Get ready to watch a movie...")
        # self.popper.on()
        # self.popper.pop()
        # self.lights.dim(10)
        # self.screen.down()
        # self.projector.on()
        # self.projector.wideScreenMode()
        self.amp.on()
        # self.amp.set_streaming_player(self.player)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        # self.player.on()
        # self.player.play(movie)

    def endMovie(self):
        print("Shutting movie theater down...")
        # self.popper.off()
        # self.lights.on()
        # self.screen.up()
        # self.projector.off()
        self.amp.off()
        # self.player.stop()
        # self.player.off()

    def listenToRadio(self, frequency):
        print("Tuning in the airwaves...")
        self.tuner.on()
        self.tuner.setFrequency(frequency)
        self.amp.on()
        self.amp.setVolume(5)
        self.amp.setTuner(self.tuner)

    def endRadio(self):
        print("Shutting down the tuner...")
        self.tuner.off()
        self.amp.off()


def theatre_test_drive():
    amp = Amplifier("Amplifier")
    tuner = Tuner("AM/FM Tuner", amp)
    # player = StreamingPlayer("Streaming Player", amp)
    # cd = CdPlayer("CD Player", amp)
    # projector = Projector("Projector", player)
    # lights = TheaterLights("Theater Ceiling Lights")
    # screen = Screen("Theater Screen")
    # popper = PopcornPopper("Popcorn Popper")

    homeTheater = HomeTheaterFacade(amp, tuner,
                                    # player,
                                    # projector,
                                    # screen,
                                    # lights,
                                    # popper
                                    )

    homeTheater.watchMovie("Raiders of the Lost Ark")
    homeTheater.endMovie()


if __name__ == '__main__':
    theatre_test_drive()
