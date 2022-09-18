from threading import Timer
from playsound import playsound
import time


class Ringtone:
    shouldring = 0
    ringtone = None

    ringstart = 0

    shouldplayhandset = 0
    handsetfile = None
    timerHandset = None

    config = None

    def __init__(self, config):
        self.config = config

    def start(self):
        self.shouldring = 1
        self.ringtone = Timer(0, self.doring)
        self.ringtone.start()
        self.ringstart = time.time()

    def stop(self):
        self.shouldring = 0
        if self.ringtone is not None:
            self.ringtone.cancel()

    def starthandset(self, file):
        self.shouldplayhandset = 1
        self.handsetfile = file
        if self.timerHandset is not None:
            print("[RINGTONE] Handset already playing?")
            return

        self.timerHandset = Timer(0, self.playhandset)
        self.timerHandset.start()

    def stophandset(self):
        self.shouldplayhandset = 0
        if self.timerHandset is not None:
            self.timerHandset.cancel()
            self.timerHandset = None

    def playhandset(self):
        print("Starting dialtone")
        playsound(self.handsetfile, block=True)

    def playfile(self, file):
        playsound(file, block=True)

    def doring(self):
        while self.shouldring:
            playsound(self.config["soundfiles"]["ringtone"], block=True)

            time.sleep(2)
            if time.time() - 60 > self.ringstart:
                self.stop()
