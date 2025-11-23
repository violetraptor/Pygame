# violetraptor
# Version: 2025-11-23
# Programm zum Testen von MIDI-Tönen


#Import
import pygame


# Hauptfunktion
def main():
    print("Programm gestartet.")
    pygame.midi.init() # initialize the midi module



    pygame.midi.quit() # uninitialize the midi module

if __name__ == "__main__":
    main()