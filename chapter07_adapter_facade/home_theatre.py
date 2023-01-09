from facade.home_theatre_facade import HomeTheaterFacade
from separates.separates import Amplifier, Tuner, StreamingPlayer, Projector


def theatre_test_drive():
    amp = Amplifier("Amplifier")
    tuner = Tuner("AM/FM Tuner", amp)
    player = StreamingPlayer("Streaming Player", amp)
    # cd = CdPlayer("CD Player", amp)
    projector = Projector("Projector", player)
    # lights = TheaterLights("Theater Ceiling Lights")
    # screen = Screen("Theater Screen")
    # popper = PopcornPopper("Popcorn Popper")

    home_theater = HomeTheaterFacade(amp, tuner,
                                     player,
                                     projector,
                                     # screen,
                                     # lights,
                                     # popper
                                     )

    home_theater.watch_movie("Raiders of the Lost Ark")
    home_theater.end_movie()


if __name__ == '__main__':
    theatre_test_drive()
