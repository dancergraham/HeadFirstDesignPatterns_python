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
        print(f"{self.description} setting frequency to frequency")
        self.frequency = frequency

    def set_am(self):
        print(f"{self.description} setting AM mode")

    def set_fm(self):
        print(f"{self.description} setting FM mode")


class StreamingPlayer:
    def __init__(self, description, amplifier):
        self.description = description
        self.amplifier = amplifier
        self.current_chapter = 0
        self.movie = None

    def __str__(self):
        return self.description

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def play(self, arg):
        if isinstance(arg, str):
            self.movie = arg
            self.current_chapter = 0
            print(self.description + " playing \"" + self.movie + "\"")
        elif isinstance(arg, int):
            if self.movie is None:
                print(f"{self.description} can't play chapter {arg} no movie selected")
            else:
                self.current_chapter = arg
            print(
                f"{self.description} playing chapter {self.current_chapter}"
                + " of \""
                + self.movie
                + "\""
            )

    def stop(self):
        self.current_chapter = 0
        print(self.description + " stopped \"" + self.movie + "\"")

    def pause(self):
        print(self.description + " paused \"" + self.movie + "\"")

    def set_two_channel_audio(self):
        print(f"{self.description} set two channel audio")

    def set_surround_audio(self):
        print(f"{self.description} set surround audio")


class Projector:
    def __init__(self, description, player):
        self.description = description
        self.player = player

    def __str__(self):
        return self.description

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def wide_screen_mode(self):
        print(self.description + " in widescreen mode (16x9 aspect ratio)")

    def tv_mode(self):
        print(self.description + " in tv mode (4x3 aspect ratio)")


class Screen:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

    def up(self):
        print(f"{self.description} going up")

    def down(self):
        print(f"{self.description} going down")


class TheaterLights:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def dim(self, level):
        print(f"{self.description} dimming to {level} %")


class PopcornPopper:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def pop(self):
        print(f"{self.description} popping popcorn!")
