from playsound import playsound

import abc
from threading import Thread

class BeatModelInterface(abc.ABC):
    def initialize():
        raise NotImplementedError

    def on():
        raise NotImplementedError

    def off():
        raise NotImplementedError

    def setBPM(bpm: int):
        raise NotImplementedError

    def getBPM():
        raise NotImplementedError

    def registerObserver(o: BeatObserver):
        raise NotImplementedError

    def removeObserver(o: BeatObserver):
        raise NotImplementedError

    def registerObserver(o: BPMObserver):
        raise NotImplementedError

    def removeObserver(o: BPMObserver):
        raise NotImplementedError


class BeatModel(BeatModelInterface):
    def __init__(self) -> None:
        beat_observers = []
        bpm_observers = []
        bpm = 90
        thread = Thread()
        stop = False
        clip = 'clap.wav'

    def initialize():
        try: 
            File resource = new File("clap.wav")
            clip = (Clip) AudioSystem.getLine(new Line.Info(Clip.class))
            clip.open(AudioSystem.getAudioInputStream(resource))
        except Exception as ex:
            print("Error: Can't load clip")
            print(ex)


def dj_test_drive():
    model = BeatModel()
    controller = BeatController(model)


if __name__ == "__main__":
    dj_test_drive()
