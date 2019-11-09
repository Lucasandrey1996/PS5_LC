# import the library
from appJar import gui
from gpiozero import LED, Button
from time import sleep, time

#definition des E/S
# Avertisseurs lumineux & sonores
LP1_r = LED(4)
LP2_r = LED(17)
LP3_r = LED(27)
LP4_r = LED(22)
LP1_b = LED(23)
LP2_b = LED(24)
LP3_b = LED(25)
LP4_b = LED(12)
BUZ_r = LED(5)
BUZ_b = LED(20)
SP = LED(6)

# Signaux Chrono
SC_r = LED(26)
SC_b = LED(21)

# Sorties de puissance
EA_r = LED(13)
EA_b = LED(18)
RP_r = LED(19)
RP_b = LED(16)


# definition des callback

# fonction sleep maison
def MySleep(delay, T_init):
    i=0
    while ((T_init+delay)>time()):
        i=i+1
#     print(time())
#     print(T_init)
#     print(delay)
    return i
        

# gestion du bouton "Qualifications"
def Qualif():
    global qualif
    qualif=1
    app_Welcome.stop()

# gestion des boutons "Rouge" & "Bleu"
def Colour(button):
    global couleur
    if button == "Rouge":
        couleur=1
        app_Welcome.stop()
    else:
        couleur=-1
        app_Welcome.stop()
        
# gestion du bouton "Select" lorsque "Rouge" à été sélectionné
def Select_red_delay():
    global avance_s
    avance_s = validNumEntry(app_Select_red_delay.getEntry("Avance"))
    app_Select_red_delay.stop()
    
# gestion du bouton "Select" lorsque "Rouge" à été sélectionné
def Select_blue_delay():
    global avance_s
    avance_s = validNumEntry(app_Select_blue_delay.getEntry("Avance"))
    app_Select_blue_delay.stop()
    
# gestion du bouton "Start"
def Start_Q():
    global ready
    ready = 1
    app_Qualif.stop()
    
def Start_red():
    global ready
    ready = 1
    app_Start_red.stop()
    
def Start_blue():
    global ready
    ready = 1
    app_Start_blue.stop()
    
# gestion du départ   
def Launch():
    # define globals variables
    global qualif
    global couleur
    global avance_s
    global ready
    global error
    
    #definition des E/S
    # Avertisseurs lumineux & sonores
    global LP1_r
    global LP2_r
    global LP3_r
    global LP4_r
    global LP1_b
    global LP2_b
    global LP3_b
    global LP4_b
    global BUZ_r
    global BUZ_b

    # Signaux Chrono
    global SC_r
    global SC_b

    # Sorties de puissance
    global EA_r
    global EA_b
    global RP_r
    global RP_b
    
    # Locals variables
    delay=0.5
    init_time=time()
    
    if qualif==1:
        #séquence de départ en phase de qualification
        SP.on()
        
        LP1_r.on()
        LP1_b.on()
        BUZ_r.on()
        BUZ_b.on()
        MySleep(delay,init_time)
        BUZ_r.off()
        BUZ_b.off()
        MySleep(delay*2,init_time)
        
        LP2_r.on()
        LP2_b.on()
        BUZ_r.on()
        BUZ_b.on()
        MySleep(delay*3,init_time)
        BUZ_r.off()
        BUZ_b.off()
        MySleep(delay*4,init_time)
        
        LP3_r.on()
        LP3_b.on()
        BUZ_r.on()
        BUZ_b.on()
        MySleep(delay*5,init_time)
        BUZ_r.off()
        BUZ_b.off()
        MySleep(delay*6,init_time)
        
        LP4_r.on()
        LP4_b.on()
        BUZ_r.on()
        BUZ_b.on()
        
        SC_r.on()
        SC_b.on()
        EA_r.on()
        EA_b.on()
        
        MySleep(delay*8,init_time)
        
        BUZ_r.off()
        BUZ_b.off()
        SP.on()
    
    print("Launch execution time = ", time()-init_time)
    return 0

# test si l'entrée numérique est valide
def validNumEntry(c):
    global error
    try:
        r = float(c)
        return r
    except ValueError:
        error=1
        return 0

# affiche les variables dans la console   
def PrintVar():
    global qualif
    global couleur
    global avance_s
    global ready
    global error
    print(" ")
    print("Check variables")
    print("-couleur   = ",couleur)
    print("-qualif    = ",qualif)
    print("-avance [s]= ",avance_s)
    print("-ready     = ",ready)
    print("-Error     = ",error)

while 1:
    # initialise varibles (#b: 0=>FALSE / 1=>TRUE)
    qualif=0#b
    couleur=0
    avance_s=0
    ready=0#b
    error=0#b
    
    # initialise GPIO
    # Avertisseurs lumineux & sonores
    LP1_r.off()
    LP2_r.off()
    LP3_r.off()
    LP4_r.off()
    LP1_b.off()
    LP2_b.off()
    LP3_b.off()
    LP4_b.off()
    BUZ_r.off()
    BUZ_b.off()
    SP.off()
    
    # Signaux Chrono
    SC_r.off()
    SC_b.off()
    
    # Sorties de puissance
    EA_r.off()
    EA_b.off()
    RP_r.off()
    RP_b.off()
    
    # Création de la fenêtre
    with gui("Initialisation", "600x300", bg='snow', font={'size':22}) as app_Welcome:
        app_Welcome.label("Pour un départ sans délais", bg='lightgreen', fg='black')
        app_Welcome.buttons(["Qualifications"], [Qualif])
        app_Welcome.label("Pour un départ avec une avance du côté :", bg='yellow', fg='black')
        app_Welcome.buttons(["Rouge", "Bleu"], [Colour, Colour])
     
    # Check variables
    PrintVar()
    
    if qualif==1:
        # Création de la fenêtre
        with gui("Qualifications", "600x300", bg='snow', font={'size':22}) as app_Qualif:
            app_Qualif.label("Pressez start pour donner le départ", bg='tomato', fg='black')
            app_Qualif.buttons(["Start"], [Start_Q])
            
    elif couleur==1:
        # Création de la fenêtre
        with gui("Avance pour la piste rouge", "600x300", bg='red', font={'size':22}) as app_Select_red_delay:
            app_Select_red_delay.label("Definissez l'avance pour le côté rouge", bg='tomato', fg='black')
            app_Select_red_delay.entry("Avance", label=True, focus=True)
            app_Select_red_delay.buttons(["Select"], [Select_red_delay])
    
    elif couleur==-1:
        # Création de la fenêtre
        with gui("Avance pour la piste bleu", "600x300", bg='blue', font={'size':22}) as app_Select_blue_delay:
            app_Select_blue_delay.label("Definissez l'avance pour le côté bleu", bg='deepskyblue', fg='black')
            app_Select_blue_delay.entry("Avance", label=True, focus=True)
            app_Select_blue_delay.buttons(["Select"], [Select_blue_delay])
            
    else:
        error=1
    
    # Check variables
    PrintVar()
    
    if (error==0)and(ready==0):
        if couleur==1:
            # Création de la fenêtre
            with gui("Confirmation du délais", "600x300", bg='red', font={'size':22}) as app_Start_red:
                app_Start_red.label("Avance pour le côté rouge (en secondes):", bg='tomato', fg='black')
                app_Start_red.label(avance_s, bg='yellow', fg='black')
                app_Start_red.buttons(["Start", "Cancel"], [Start_red,app_Start_red.stop])
    
        elif couleur==-1:
            # Création de la fenêtre
            with gui("Confirmation du délais", "600x300", bg='blue', font={'size':22}) as app_Start_blue:
                app_Start_blue.label("Avance pour le côté bleu (en secondes):", bg='deepskyblue', fg='black')
                app_Start_blue.label(avance_s, bg='yellow', fg='black')
                app_Start_blue.buttons(["Start", "Cancel"], [Start_blue,app_Start_blue.stop])
    else:
        avance_s=0
    
        # Check variables
    PrintVar()
    
    if (error==0)and(ready!=0):
        Launch()
        # Création de la fenêtre
        with gui("done", "600x300", bg='snow', font={'size':22}) as app_Launch:
            app_Launch.label("Le départ à été donné...", bg='snow', fg='black')
            app_Launch.buttons(["OK"], [app_Launch.stop])
    else:
        # Création de la fenêtre
        with gui("error", "600x300", bg='snow', font={'size':22}) as app_Error:
            app_Error.label("Un problème est survenu,", bg='snow', fg='black')
            app_Error.label("aucun départ n'est donné...", bg='snow', fg='black')
            app_Error.buttons(["OK"], [app_Error.stop])
            
    
    
    
    