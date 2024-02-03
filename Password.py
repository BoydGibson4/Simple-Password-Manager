# Boyd Gibson
#Password Manager
#24/11/2022
#===========================================================================================

from guizero import *
#importing everything from the guizero library
import time
#importing the time
import random
#importing random so that the generated password ccan be randomised

#===========================================================================================

#declaring 
global Gpass
Gpass = ""
global char
char = "0123456789"
global password
password = ""
global text
text = ""
global i
i = 0



#===========================================================================================

app = App(bg = "white", title="Password Manager", width = 630, height = 300, layout = "grid")

#===========================================================================================



def invert():
    global i
    if Invert.text == "Invert" and i%2 == 0:
        #if the Invert button is clicked then the color of the buttons
        #and text will be changed to hopefuly suite the user better
        Title.tk.configure(background = "black")
        Dtext.tk.configure(background = "black")
        DtextInput.tk.configure(background = "black")
        Tbox.tk.configure(background = "black")
        Gpassword.tk.configure(background = "black")
        Cpassword.tk.configure(background = "black")
        Save.tk.configure(background = "black")
        Time.tk.configure(background = "black")
        Invert.tk.configure(background = "black")

        Title.text_color =  "white"
        Dtext.text_color =  "white"
        DtextInput.text_color =  "white"
        Tbox.text_color =  "white"
        Gpassword.text_color =  "white"
        Cpassword.text_color =  "white"
        Save.text_color =  "white"
        Time.text_color =  "white"
        Invert.text_color =  "white"
        #counter to keep track of what color scheme is meant to be used
        i=i+1
        
    else:
        #if the Invert button is clicked again then the color of the buttons
        #and text will be changed once again back to the original color scheme
        Title.tk.configure(background = "#AEB0FB")
        Dtext.tk.configure(background = "#AEB0FB")
        DtextInput.tk.configure(background = "#AEB0FB")
        Tbox.tk.configure(background = "#AEB0FB")
        Gpassword.tk.configure(background = "#AEB0FB")
        Cpassword.tk.configure(background = "#AEB0FB")
        Save.tk.configure(background = "#AEB0FB")
        Time.tk.configure(background = "#AEB0FB")
        Invert.tk.configure(background = "#AEB0FB")

        Title.text_color =  "black"
        Dtext.text_color =  "black"
        DtextInput.text_color =  "black"
        Tbox.text_color =  "black"
        Gpassword.text_color =  "black"
        Cpassword.text_color =  "black"
        Save.text_color =  "black"
        Time.text_color =  "black"
        Invert.text_color =  "black"
        #counter to keep track of what color scheme is meant to be used
        i=i+1
        
    return i

#===========================================================================================

def Generate():
    global password
    global Tbox
    global Gpass
    # setting to "" so that Tbox is empty for when they 
    # want to create another password
    Tbox.value = ""
    password = ""
    Gpass = ""
    
    #loop to make the generated password
    for i in range (0, 8):
      nextchar = random.choice(char)
      Gpass = Gpass + nextchar

    Tbox.value = Gpass
    password = Tbox.value
    
    return password

def Create():
    global password
    # setting to "" so that Tbox is empty for when they 
    # want to create another password
    Tbox.value = ""
    password = ""
    Gpass = ""

    password = Tbox.value
    return password
    #returning the entered password
def descriptive ():
    global text
    text = Dtext.value
    return text
    #returning the entered text 

def save():
#write passwords to a new file
    global text
    password = Tbox.value
    #creating the file
    filename = "Password Manager"
    file = open(filename, "a") 
    #entering the password and descriptive text to the file
    file.writelines (DtextInput.value +": ")
    file.writelines (password +" : " + systemtime  + "\n")
    file.close()
    #closing the file

    # setting to "" so that Tbox is empty for when they 
    # want to create another password
    Tbox.value = ""
    Gpass = ""
    DtextInput.value = ""
    text = ""

#===========================================================================================

#Creating the title of the interface
Title = Text(app, text="Password Manager", grid=[2,0], align="top")
Title.tk.configure(background = "#AEB0FB")
Title.text_color =  "black"

#===========================================================================================

#space so that the design doesnt look as cluncky
Space2 = Text(app, text=" ", grid=[0,1], align="left")

#creating the descriptive text label
Dtext = Text(app, text="Descriptive Text", grid=[0,2], align="left")
Dtext.tk.configure(background = "#AEB0FB")
Dtext.text_color =  "black"

#creating the descriptive text, text box
DtextInput = TextBox(app, grid=[1,2])
DtextInput.tk.configure(background = "#AEB0FB")

#space so that the design doesnt look as cluncky
Space1 = Text(app, text="", grid=[2,2])

#textbos for the password to be generaated/created
Tbox = TextBox(app, grid=[3,2])
Tbox.tk.configure(background = "#AEB0FB")

#gererate password button which will call the Generate function that will 
#generate the random password
Gpassword = PushButton(app,command=Generate, text = "Generate Password", grid=[2,3])
Gpassword.tk.configure(background = "#AEB0FB")

#Create password button which will call the Create function that will 
#allow the user to create there password
Cpassword = PushButton(app,command=Create, text = "Create Password", grid=[4,3])
Cpassword.tk.configure(background = "#AEB0FB")

#save button which will save bothe the password and the descriptive text to the created file
Save = PushButton(app,command=save, text = "Save Password", grid=[3,4])
Save.tk.configure(background = "#AEB0FB")

#===========================================================================================

#displayes the date and time upon opening the prigram
systemtime = time.asctime(time.localtime(time.time()))

#creates the label that the date and time will be displayed in
Time = Text(app, text=systemtime, grid=[4,5])
Time.tk.configure(background = "#AEB0FB")

#invert button which ill call the invert function to invert the color schemem of the interfacce
Invert = PushButton(app,command=invert, text = "Invert", grid=[0,5])
Invert.width = 8
Invert.height = 1
Invert.tk.configure(background = "#AEB0FB")

#===========================================================================================

#running the interface
app.display()

#===========================================================================================