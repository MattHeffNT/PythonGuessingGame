
# Import Tkinter, Python's GUI library , sys and random which has some other useful features
from tkinter import *

import sys
import random

# this code uses class Guess, for ease of design where functions can be placed and called

class Guess():

     #This function is the class constructor
    def __init__(self,root):

        # delaring the GUI vairable as root, and giving the window the "Guess the number" name
        self.root= root
        root.title("Guess the number")
        #Here the code is specifying window format, including background colour and GUI window size
        root.configure(background='black')
        root.resizable(width=800, height=600)

        # Here the code, adds two menu bar items to the GUI, including a feature to start a new game, or quit

        menubar = Menu(root)
        root.config(menu=menubar)
        menubar.add_command(label="New Game",command=self.MainMenu)
        menubar.add_command(label="Quit!",command=self.quitATM)

    ########################################### main menu GUI #################################################

        # here the label and button to appear on the main menu are formatted for style, and the button's command is
        # assigned to starting a new game. These will later be gridded so as to make them visible to the user

        self.label= Label(root, text="Welcome to the Python Guessing Game",fg="white",bg="black",font="bold")

        self.newGame_button= Button(root, text="New Game",fg="white",bg="black",activebackground="white",command=self.newGame)

    ############# ##############################Game page GUI settings##################################################

        #here the game's feature and labels, including, a user input feature, a button to submit the answer, and an
        #error window. Here the code assigns style and button commands to be later gridded and made visible to the user

        self.newGame_input= Entry(root,text="",font = "Helvetica 15 bold")

        self.submit=Button(root, text="Submit",fg="white",bg="black",activebackground="white",command=self.newGame_return)

        self.menubutton= Button(root, text="New Game",fg="white",bg="black",activebackground="white",command=self.MainMenu)

        self.newGame_label=Label(root, text="Choose a number between 1 and 20",font="bold",fg="white",bg="black")

        self.newGame_error=Label(root, text="Error, please choose a valid number", font="bold",fg="white",bg="black")

        self.okbutton= Button(root, text="ok",fg="white",bg="black",command=self.error_return)

     ######################################## Warmer/ messages #########################################################

        # These labels are styling and specifying the message a user will recieve if he or she
        # enters an incorrect/correct value, as well as provide tips to when the user is close to the answer.
        # these will later be gridded and made visible to the user.

        self.warmerH=Label(root,text="Getting warmer, just a bit higher",font="bold",fg="white",bg="black")
        self.warmerL=Label(root,text="Getting warmer, just a bit lower",font="bold",fg="white",bg="black")
        self.very_warmH=Label (root,text="Getting very warm, just a bit higher",font="bold",fg="white",bg="black")
        self.very_warmL=Label (root,text="Getting very warm, just a bit lower",font="bold",fg="white",bg="black")
        self.hotH=Label(root,text="Getting HOT, just a bit higher",font="bold",fg="white",bg="black")
        self.hotL=Label(root,text="Getting HOT, just a bit lower",font="bold",fg="white",bg="black")
        self.generalH=Label (root, text="Incorrect, try a little bit higher",font="bold",fg="white",bg="black")
        self.generalL=Label (root, text="Incorrect, try a little bit lower",font="bold",fg="white",bg="black")
        self.win= Label (root,text="Congratulations you guessed correctly",font="bold",fg="white",bg="black")

    #####################################################################################################################
        #here the code calls the MainMenu function to get the GUI started properly
        self.MainMenu()
    #####################################################################################################################

    def MainMenu(self):

        #the main menu function calls firstly the RemoveAll function, to clear the grid of any formatting and buttons etc
        #that may be on the window. Then the function proceeds to grid the main menu buttons and labels as declared above.

        self.RemoveAll()

        self.label.grid(row=0,column=2,padx=(10,10),pady=(10,10))
        self.newGame_button.grid(row=1,column=2)
        self.newGame_button.config( height = 2, width = 10)

    def RemoveAll(self):

        # the RemoveAll function as highlighted above, removes all the formatting, buttons, labels,
        # inputs etc from the screen.

        self.label.grid_remove()
        self.newGame_button.grid_remove()
        self.submit.grid_remove()
        self.newGame_input.grid_remove()
        self.newGame_label.grid_remove()
        self.okbutton.grid_remove()
        self.newGame_error.grid_remove()
        self.okbutton.grid_remove()
        self.newGame_error.grid_remove()


        self.warmerH.grid_remove()
        self.warmerL.grid_remove()
        self.very_warmH.grid_remove()
        self.very_warmL.grid_remove()
        self.hotH.grid_remove()
        self.hotL.grid_remove()
        self.win.grid_remove()
        self.generalH.grid_remove()
        self.generalL.grid_remove()

    def randomize (self):
        #this function assigns a range from 1,20 to the variable C, followed by creating the global variable X, which
        #is then assigned a random sample function, which essentially randomizes the number to be guessed by the user.

        c=range(1,20)
        global x
        x= random.sample(c,19)

    def error_return (self):

        #when you press ok after an error in the game GUI it calls this function. first it removes any formatting
        # that may be on the screen,  then the code regrids all the Newgame_return GUI labels and buttons,
        # but this time without re-randomizing the number to be guessed. The game GUI will
        # be explained in its own function

        self.RemoveAll()

        self.newGame_label.grid(row=0,column=1,padx=(10, 10))
        #self.newGame_label.config( height = 5, width = 30)

        self.newGame_input.grid(row=1,column=1)
        self.newGame_input.config( width = 5,borderwidth=2,justify=CENTER)

        input=(self.newGame_input.get())
        self.submit.grid(row=3,column=1,padx=(10, 10),pady=(10,10))
        self.submit.config( height = 2, width = 10)

    def newGame(self):

        # when the newgame function is called , it first removes all formatting in the GUI window, by calling the
        # RemoveAll function.

        self.RemoveAll()

        # Then the newgame function calls the self.randomize functions to carry over it's values and variables

        self.randomize()

        #here i've placed a comnmented out print cheat , so that for testing purposes the coder can see the number
        # to be guessed. This is followed by resizing the window to ensure the text doesn't change the window size.

        #print ((x[2]))

        root.geometry("300x100")
        # number is then assigned as a global variable, a random number from self.randomize function
        global Number
        Number= x[2]

        # Here Number.txt value is now assigned to the Number variable, where the random number is written into the
        #file. This is to ensure that the number won't change every time the player causes an error etc.

        Number=("Number.txt")
        f=open("Number.txt",'w')
        Number=f.write(str(x[2]))
        f.close()

        # the new game label is gridded to be visible to the user
        self.newGame_label.grid(row=0,column=1,padx=(10, 10))

        #the code displays an text input for the user to enter their guess. Below that the code sets the dimensions of
        # the input to display.

        self.newGame_input.grid(row=1,column=1)
        self.newGame_input.config( width = 5,borderwidth=2,justify=CENTER)

        #here the code assigns the user's input, to the input variable. This is followed by gridding the submit button
        # and setting its dimensions to display. Once the submit button is pressed, it calls the newGame_return function

        input=(self.newGame_input.get())
        self.submit.grid(row=3,column=1,padx=(10, 10),pady=(10,10))
        self.submit.config( height = 2, width = 10)

    def newGame_return (self):

        # when the newgame_return function is called , it first removes all formatting in the GUI window, by calling the
        # RemoveAll function.

        self.RemoveAll()

        #root geometry is used again to  ensure the text, labels etc don't change the window size.
        root.geometry("300x100")

        #once again the user input is dispalyed, this is so that the user can continue having tries at guessing until
        #they get it right.
        self.newGame_input.grid(row=1,column=2)
        self.newGame_input.config(width = 5,borderwidth=2,justify=CENTER)

        #here the code opens the Number.txt file, then assigns the value in the text file as an integer to a new Number
        # variable
        f=open("Number.txt",'r')
        Number=f.readline()
        Number=(int(Number))

        #this code displays the new game label and submit button as well as configuring button style to be displayed.
        self.newGame_label.grid(row=0,column=2,padx=(10, 10))
        self.submit.grid(row=3,column=2,padx=(10, 10),pady=(10,10))
        self.submit.config( height = 2, width = 10)

        # Here is where the game is essentially played, a try/except handler is used to ensure that the user doesn't
        # enter any symobls, alphabetic characters etc.
        try:
            #the user input on a second/third/ ad infinitum go is assigned to the input variable.
            input=int(self.newGame_input.get())

            #the code here then runs through the user inputs, checking whether the input and value in the Number.txt
            #file correspond (if they do, then the user wins). Other elif conditions are used to generate hints to the
            #user, whether they are close to the random number or not, and then providing hints to when the user's guess
            #is really close to the random number.

            if input==Number:
                self.RemoveAll()
                root.geometry("300x100")
                self.win.grid(row=0,column=2,padx=(5, 0),pady=(0,10))

                self.okbutton.grid (row=3,column=2)
                self.okbutton.config( height = 2, width = 10)
                self.newGame_input.delete(0, "end")

            elif input==Number-3 :
                self.RemoveAll()
                root.geometry("300x100")
                self.warmerH.grid(row=0,column=2,padx=(5, 0),pady=(0,10))
                self.warmerH.config( height = 0, width = 30)

                self.okbutton.grid (row=3,column=2)
                self.okbutton.config( height = 2, width = 10)
                self.newGame_input.delete(0, "end")

            elif input==Number+3:
                self.RemoveAll()
                root.geometry("300x100")
                self.warmerL.grid(row=0,column=2,padx=(5, 0),pady=(0,10))
                self.warmerL.config( height = 0, width = 30)

                self.okbutton.grid (row=3,column=2)
                self.okbutton.config( height = 2, width = 10)
                self.newGame_input.delete(0, "end")

            elif input==Number-2 :
                self.RemoveAll()
                root.geometry("300x100")
                self.warmerH.grid(row=0,column=2,padx=(5, 0),pady=(0,10))
                self.warmerH.config( height = 0, width = 30)

                self.okbutton.grid (row=3,column=2)
                self.okbutton.config( height = 2, width = 10)
                self.newGame_input.delete(0, "end")

            elif input==Number+2:
                self.RemoveAll()
                root.geometry("300x100")
                self.warmerL.grid(row=0,column=2,padx=(5, 0),pady=(0,10))
                self.warmerL.config( height = 0, width = 30)

                self.okbutton.grid (row=3,column=2)
                self.okbutton.config( height = 2, width = 10)
                self.newGame_input.delete(0, "end")

            elif input==Number-1 :
                self.RemoveAll()
                root.geometry("300x100")
                self.hotH.grid(row=0,column=2,padx=(5, 0),pady=(0,10))
                self.hotH.config( height = 0, width = 30)

                self.okbutton.grid (row=3,column=2)
                self.okbutton.config( height = 2, width = 10)

            elif input==Number+1:
                self.RemoveAll()
                root.geometry("300x100")
                self.hotL.grid(row=0,column=2,padx=(5, 0),pady=(0,10))
                self.hotL.config( height = 0, width = 30)


                self.okbutton.grid (row=3,column=2)
                self.okbutton.config( height = 2, width = 10)

            elif input>Number:
                self.RemoveAll()
                #root.geometry("300x100")
                self.generalL.grid(row=0,column=2)
                self.generalL.config( height = 0, width = 30)

                self.okbutton.grid (row=3,column=2)
                self.okbutton.config( height = 2, width = 10)

            elif input<Number:
                self.RemoveAll()
                #root.geometry("300x100")
                self.generalH.grid(row=0,column=2,padx=(5, 0),pady=(0,10))
                self.generalH.config( height = 0, width = 30)

                self.okbutton.grid (row=3,column=2,padx=(5, 0),pady=(0,10))
                self.okbutton.config( height = 2, width = 10)

            else:
                self.newGame_input.delete(0, "end")
        #these errors make sure that syntax of user input is correct, if not, it displays a seperate screen, that can
        #return the user back to the game while, not generating a new random number.
        except ValueError:
            self.RemoveAll()
            self.newGame_error.grid(row=0,column=1,padx=(10, 0))
            self.okbutton.grid (row=2,column=1,padx=(10, 0),pady=(10,10))
            self.newGame_input.delete(0, "end")

        except SyntaxError:
            self.RemoveAll()
            self.newGame_error.grid(row=0,column=1,padx=(10, 0))
            self.okbutton.grid (row=2,column=1,padx=(10, 0),pady=(10,10))
            self.newGame_input.delete(0, "end")

        except TypeError:
            self.RemoveAll()
            self.newGame_error.grid(row=0,column=1,padx=(10, 10))
            self.okbutton.grid (row=2,column=1,padx=(10, 0),pady=(10,10))
            self.newGame_input.delete(0, "end")

    # quits the game.
    def quitATM(self):
        self.root.quit
        sys.exit(0)

#loop GUI, through each iteration, it calls different as user requests,until user terminates the loop
root=Tk()
ATM= Guess(root)

root.mainloop()
