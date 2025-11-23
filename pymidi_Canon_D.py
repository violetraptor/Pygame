# violetraptor
# Version: 2025-11-23
# Program for testing Musical Instrument Digital Interface (Midi) in PyGame
# Docs: https://www.pygame.org/docs/ref/midi.html#pygame.midi.init




#Import
import time # for short breaks between two MIDI instruments
import pygame # main PyGame module
import pygame.midi # MIDI PyGame module


# function
# This function gives us the port for the MIDI output device.
def getanmidiOut ():
    # print the devices and use the last output port.
    n_midi_devices = pygame.midi.get_count()
    print(f"This computer has ", n_midi_devices, " MIDI devices:")

    for i in range(pygame.midi.get_count()):
        r = pygame.midi.get_device_info(i)
        (interf, name, is_input, is_output, is_opened) = r
        print(f"\t", interf, name, is_input, is_output, is_opened)
        if is_output:
            last_port = i
    
    return last_port

# The main code is now inside a function, so you only need to "press" a key. 
def press_key(midi_out, tn_note, tn_bar):
    frequencyOfnote = 0
    time.sleep(0.025)
    midi_out.note_on(note= tn_note,velocity=127)
    time.sleep(tn_bar)
    midi_out.note_off(note= tn_note,velocity=0)
    frequencyOfnote = pygame.midi.midi_to_frequency(tn_note)
    print(f"Note ", tn_note, "has the frequency ", frequencyOfnote)



# main function
def main():
    print("Program run <3")
    
    # variables
    stateMIDI = False # the MIDI state of the program
    instrument = 1 
    pitch = 0
    n_sounds = 4 # playbacks
    bar = 60.00/100.00

    #keys
    pk_C = 36
    pk_D = 38 # 37 is a black key on an piano
    pk_E = 40
    pk_F = 41
    pk_G = 43
    pk_A = 45
    pk_H = 47
    pk_c = pk_C + 12
    pk_d = pk_D + 12
    pk_e = pk_E + 12
    pk_f = pk_F + 12
    pk_g = pk_G + 12
    pk_a = pk_A + 12
    pk_h = pk_H + 12
    pk_c1 = pk_c + 12
    pk_d1 = pk_d + 12
    pk_e1 = pk_e + 12
    pk_f1 = pk_f + 12
    pk_g1 = pk_g + 12
    pk_a1 = pk_a + 12
    pk_h1 = pk_h + 12
    pk_c2 = pk_c1 + 12
    pk_d2 = pk_d1 + 12
    pk_e2 = pk_e1 + 12
    pk_f2 = pk_f1 + 12
    pk_g2 = pk_g1 + 12
    pk_a2 = pk_a1 + 12
    pk_h2 = pk_h1 + 12

    


    pygame.init()
    pygame.midi.init() # initialize the midi module

    stateMIDI = pygame.midi.get_init() # returns True if the midi module is currently initialized
    print(f"PyGame MIDI is initialize? ", stateMIDI)

    midiPort = getanmidiOut() #  See the functions at line 12
    # midiPort = pygame.midi.get_default_output_id() # short way 
    print(f"This system will use MIDI port ", midiPort)

    midi_out = pygame.midi.Output(midiPort, 0) # Output(device_id, latency=0) | latency is the delay in milliseconds applied to timestamps to determine when the output should actually occur.

    # select an instrument, with a value between 0 and 127
    midi_out.set_instrument(instrument) # set_instrument(instrument_id, channel=0) | You can find a list of all MIDI Level 1 instruments at the end of this code. Adjust the pitch of a channel: -8192 to +8191
    midi_out.pitch_bend(pitch) # channel

    # Our Song is here
    bar = bar/2.0
    for i in range(n_sounds):   

        if i == 1:
            midi_out.note_on(note= pk_f2,velocity=127)
        elif i > 1:
            midi_out.note_on(note= pk_f2,velocity=127)
            midi_out.note_on(note= pk_d2,velocity=127)
            midi_out.note_on(note= pk_a1,velocity=127)
        press_key(midi_out, pk_d, bar)
        press_key(midi_out, pk_a, bar)
        press_key(midi_out, pk_d1, bar)
        press_key(midi_out, pk_f1, bar)
        if i == 1:
            midi_out.note_off(note= pk_f2,velocity=0)
        elif i > 1:
            midi_out.note_on(note= pk_f2,velocity=0)
            midi_out.note_on(note= pk_d2,velocity=0)
            midi_out.note_on(note= pk_a1,velocity=0)


        if i == 1:
            midi_out.note_on(note= pk_e2,velocity=127)
        elif i > 1:
            midi_out.note_on(note= pk_e2,velocity=127)
            midi_out.note_on(note= pk_c2,velocity=127)
            midi_out.note_on(note= pk_a1,velocity=127)
        press_key(midi_out, pk_A, bar)
        press_key(midi_out, pk_e, bar)
        press_key(midi_out, pk_a, bar)
        press_key(midi_out, pk_c1, bar)
        if i == 1:
            midi_out.note_off(note= pk_e2,velocity=0)
        elif i > 1:
            midi_out.note_on(note= pk_e2,velocity=0)
            midi_out.note_on(note= pk_c2,velocity=0)
            midi_out.note_on(note= pk_a1,velocity=0)

        if i == 1:
            midi_out.note_on(note= pk_d2,velocity=127)
        elif i > 1:
            midi_out.note_on(note= pk_d2,velocity=127)
            midi_out.note_on(note= pk_h1,velocity=127)
            midi_out.note_on(note= pk_f1,velocity=127)
        press_key(midi_out, pk_H, bar)
        press_key(midi_out, pk_f, bar)
        press_key(midi_out, pk_h, bar)
        press_key(midi_out, pk_d1, bar)
        if i == 1:
            midi_out.note_off(note= pk_d2,velocity=0)
        elif i > 1:
            midi_out.note_on(note= pk_d2,velocity=0)
            midi_out.note_on(note= pk_h1,velocity=0)
            midi_out.note_on(note= pk_f1,velocity=0)

        if i == 1:
            midi_out.note_on(note= pk_c2,velocity=127)
        elif i > 1:
            midi_out.note_on(note= pk_c2,velocity=127)
            midi_out.note_on(note= pk_a1,velocity=127)
            midi_out.note_on(note= pk_f1,velocity=127)
        press_key(midi_out, pk_F, bar)
        press_key(midi_out, pk_c, bar)
        press_key(midi_out, pk_f, bar)
        press_key(midi_out, pk_a, bar)
        if i == 1:
            midi_out.note_off(note= pk_c2,velocity=0)
        elif i > 1:
            midi_out.note_on(note= pk_c2,velocity=0)
            midi_out.note_on(note= pk_a1,velocity=0)
            midi_out.note_on(note= pk_f1,velocity=0)

        if i == 1:
            midi_out.note_on(note= pk_h1,velocity=127)
        elif i > 1:
            midi_out.note_on(note= pk_h1,velocity=127)
            midi_out.note_on(note= pk_g1,velocity=127)
            midi_out.note_on(note= pk_d1,velocity=127)
        press_key(midi_out, pk_G, bar)
        press_key(midi_out, pk_d, bar)
        press_key(midi_out, pk_g, bar)
        press_key(midi_out, pk_h, bar)
        if i == 1:
            midi_out.note_off(note= pk_h1,velocity=0)
        elif i > 1:
            midi_out.note_on(note= pk_h1,velocity=0)
            midi_out.note_on(note= pk_g1,velocity=0)
            midi_out.note_on(note= pk_d1,velocity=0)

        if i == 1:
            midi_out.note_on(note= pk_a1,velocity=127)
        elif i > 1:
            midi_out.note_on(note= pk_a1,velocity=127)
            midi_out.note_on(note= pk_f1,velocity=127)
            midi_out.note_on(note= pk_d1,velocity=127)
        press_key(midi_out, pk_D, bar)
        press_key(midi_out, pk_A, bar)
        press_key(midi_out, pk_d, bar)
        press_key(midi_out, pk_f, bar)
        if i == 1:
            midi_out.note_off(note= pk_a1,velocity=0)
        elif i > 1:
            midi_out.note_on(note= pk_a1,velocity=0)
            midi_out.note_on(note= pk_f1,velocity=0)
            midi_out.note_on(note= pk_d1,velocity=0)

        if i == 1:
            midi_out.note_on(note= pk_h1,velocity=127)
        elif i > 1:
            midi_out.note_on(note= pk_h1,velocity=127)
            midi_out.note_on(note= pk_g1,velocity=127)
            midi_out.note_on(note= pk_d1,velocity=127)
        press_key(midi_out, pk_G, bar)
        press_key(midi_out, pk_d, bar)
        press_key(midi_out, pk_g, bar)
        press_key(midi_out, pk_h, bar)
        if i == 1:
            midi_out.note_off(note= pk_h1,velocity=0)
        elif i > 1:
            midi_out.note_on(note= pk_h1,velocity=0)
            midi_out.note_on(note= pk_g1,velocity=0)
            midi_out.note_on(note= pk_d1,velocity=0)

        if i == 1:
            midi_out.note_on(note= pk_c2,velocity=127)
        elif i > 1:
            midi_out.note_on(note= pk_c2,velocity=127)
            midi_out.note_on(note= pk_a1,velocity=127)
            midi_out.note_on(note= pk_e1,velocity=127)
        press_key(midi_out, pk_A, bar)
        press_key(midi_out, pk_e, bar)
        press_key(midi_out, pk_a, bar)
        press_key(midi_out, pk_c1, bar)
        if i == 1:
            midi_out.note_off(note= pk_c2,velocity=0)
        elif i > 1:
            midi_out.note_on(note= pk_c2,velocity=0)
            midi_out.note_on(note= pk_a1,velocity=0)
            midi_out.note_on(note= pk_e1,velocity=0)






    pygame.midi.quit() # uninitialize the midi module
    pygame.quit()
    print("Program ends")

if __name__ == "__main__":
    main()



"""
Piano:
1 Acoustic Grand Piano
2 Bright Acoustic Piano
3 Electric Grand Piano
4 Honky-tonk Piano
5 Electric Piano 1
6 Electric Piano 2
7 Harpsichord
8 Clavinet

Chromatic Percussion:
9 Celesta
10 Glockenspiel
11 Music Box
12 Vibraphone
13 Marimba
14 Xylophone
15 Tubular Bells
16 Dulcimer

Organ:
17 Drawbar Organ
18 Percussive Organ
19 Rock Organ
20 Church Organ
21 Reed Organ
22 Accordion
23 Harmonica
24 Tango Accordion

Guitar:
25 Acoustic Guitar (nylon)
26 Acoustic Guitar (steel)
27 Electric Guitar (jazz)
28 Electric Guitar (clean)
29 Electric Guitar (muted)
30 Overdriven Guitar
31 Distortion Guitar
32 Guitar harmonics

Bass:
33 Acoustic Bass
34 Electric Bass (finger)
35 Electric Bass (pick)
36 Fretless Bass
37 Slap Bass 1
38 Slap Bass 2
39 Synth Bass 1
40 Synth Bass 2

Strings:
41 Violin
42 Viola
43 Cello
44 Contrabass
45 Tremolo Strings
46 Pizzicato Strings
47 Orchestral Harp
48 Timpani

Strings (continued):
49 String Ensemble 1
50 String Ensemble 2
51 Synth Strings 1
52 Synth Strings 2
53 Choir Aahs
54 Voice Oohs
55 Synth Voice
56 Orchestra Hit

Brass:
57 Trumpet
58 Trombone
59 Tuba
60 Muted Trumpet
61 French Horn
62 Brass Section
63 Synth Brass 1
64 Synth Brass 2

Reed:
65 Soprano Sax
66 Alto Sax
67 Tenor Sax
68 Baritone Sax
69 Oboe
70 English Horn
71 Bassoon
72 Clarinet

Pipe:
73 Piccolo
74 Flute
75 Recorder
76 Pan Flute
77 Blown Bottle
78 Shakuhachi
79 Whistle
80 Ocarina

Synth Lead:
81 Lead 1 (square)
82 Lead 2 (sawtooth)
83 Lead 3 (calliope)
84 Lead 4 (chiff)
85 Lead 5 (charang)
86 Lead 6 (voice)
87 Lead 7 (fifths)
88 Lead 8 (bass + lead)

Synth Pad:
89 Pad 1 (new age)
90 Pad 2 (warm)
91 Pad 3 (polysynth)
92 Pad 4 (choir)
93 Pad 5 (bowed)
94 Pad 6 (metallic)
95 Pad 7 (halo)
96 Pad 8 (sweep)

Synth Effects:
97 FX 1 (rain)
98 FX 2 (soundtrack)
99 FX 3 (crystal)
100 FX 4 (atmosphere)
101 FX 5 (brightness)
102 FX 6 (goblins)
103 FX 7 (echoes)
104 FX 8 (sci-fi)

Ethnic:
105 Sitar
106 Banjo
107 Shamisen
108 Koto
109 Kalimba
110 Bag pipe
111 Fiddle
112 Shanai

Percussive:
113 Tinkle Bell
114 Agogo
115 Steel Drums
116 Woodblock
117 Taiko Drum
118 Melodic Tom
119 Synth Drum

Sound effects:
120 Reverse Cymbal
121 Guitar Fret Noise
122 Breath Noise
123 Seashore
124 Bird Tweet
125 Telephone Ring
126 Helicopter
127 Applause
128 Gunshot
"""