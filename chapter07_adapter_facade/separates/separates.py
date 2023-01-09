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
        self.frequency = frequency

    def set_am(self):
        print(f"{self.description} setting AM mode")

    def set_fm(self):
        print(f"{self.description} setting FM mode")
