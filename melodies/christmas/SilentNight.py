from microbit import *
import music
import microbit

tune = [
        "G4:4", "A4:2", "G4:4", "E4:8",

        "G4:4", "A4:2", "G4:4", "E4:8",
        
        "D5:8", "D5:4", "B4:8", "B4:4", "C5:8", "C5:4", "G4:8",
        
        "A4:8", "A4:4", "C5:4", "B4:2", "A4:4", "G4:4", "A4:2", "G4:4",
        "E4:8",
        
        "A4:8", "A4:4", "C5:4", "B4:2", "A4:4", "G4:4", "A4:2", "G4:4",
        "E4:8",
        
        "D5:8", "D5:4", "F5:4", "D5:2", "B4:4", "C5:8", "E5:8",
        
        "C5:4", "G4:4", "E4:4", "G4:4", "F4:4", "D4:4", "C4:4"
       ]
music.play(tune, microbit.pin0, False, False)
