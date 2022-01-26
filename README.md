# microbitMelodies
Repository of melodies for microbit with python

Donations:  btc: 1JK4cmjh8j8ScHWsS7Su3k2QC7muBBzXvG or  
            nano: nano_1iyxmxzoaj89rg7iki3ennsn898dxipxj86frfrxnmod8dqgqa93m5n5bih3

Is a small project for create molodies for microbit with python

"AB:C" Where<br>
    A: Represent the musical note<br>
    B: Represent the level (2: Low, 4: Middle, 8: High)<br>
    C: Represent the duration (2: Low, 4: Middle, 8: High)<br>
    
    notes = [
        "C4:4", # Do
        "D4:4", # Re
        "E4:4", # Mi
        "F4:4", # Fa
        "G4:4", # Sol
        "A4:4", # La
        "B4:4", # Si
        "C5:4", # Do'
        "D5:4", # Re'
    ]

music.play(tune, microbit.pin0, False, False)
    This function:
    tune: music to play
    microbit.pin0: Output pin for the music
    wait: Block the main thread
    loop: Enable the loop of the music

# ES/
Repositorio de melodías para microbit con python
Es un pequeño proyecto para crear molodies para microbit con python

"AB:C" Dónde<br>
    A: Representa la nota musical<br>
    B: Representa el nivel (2: Low, 4: Middle, 8: High)<br>
    C: Representa la duración (2: Low, 4: Middle, 8: High)<br>
    
    notes = [
        "C4:4", # Do
        "D4:4", # Re
        "E4:4", # Mi
        "F4:4", # Fa
        "G4:4", # Sol
        "A4:4", # La
        "B4:4", # Si
        "C5:4", # Do'
        "D5:4", # Re'
    ]
    
music.play(tune, microbit.pin0, False, False)
    Esta función:
    tune: música para tocar
    microbit.pin0: Pin de salida para la música
    espera: bloquea el hilo principal
    repetir: activa el loop de la música
