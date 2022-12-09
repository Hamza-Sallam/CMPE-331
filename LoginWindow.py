"""
    Stage: Development-01
    @author: Hamza Sallam, 120200013
    @author: Mert şen, 119200031 

"""

import tkinter as tk
from time import sleep
#list of users
users = [ ('hamza','pass'),('mert','pass'),('admin','admin')]

class LoginWindow:
    # constructor
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Super Market')
        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()


    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.

        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        #add a label 
        self.title = tk.Label(text='Super Market login page')
        self.lbl01 = tk.Label(text="user name")
        self.lbl02 = tk.Label(text="password")
        #add blank label that holds changes info
        self.info = tk.Label(text="")

        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry()

        self.btn01 = tk.Button(text="login")
        self.btn02 = tk.Button(text="sign up")

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-1>", self.handle_click)
       
   

    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.title.grid(row=0, column=0, padx=10, pady=10)

        self.lbl01.grid(row=1, column=0, padx=10, pady=5)
        self.txt01.grid(row=1, column=1, padx=10, pady=5)

        self.lbl02.grid(row=2, column=0, padx=10, pady=5)
        self.txt02.grid(row=2, column=1, padx=10, pady=5)

        self.btn01.grid(row=3, column=0, padx=10, pady=5)
        self.btn02.grid(row=3, column=1, padx=10, pady=5)

        self.info.grid(row=4,column=0,padx=5,pady=5)

#  a new window 
    def blank_page(self):
        self.blank = tk.Tk()
        self.blank.geometry('500x500')
        self.blank.title('Home')
        self._initializeGUI()
        self._addGUIElementsToFrame()

    #register user if signyp button is clicked
    def signup(self):
        input_user = self.txt01.get()
        input_pass = self.txt02.get()
        #append it to the users list
        users.extend([(input_user,input_pass)])
        #print that the user is registerd successfully
        print('user {} with pass {} signed up succesfully'.format(input_user,input_pass))
        self.info.config(text="signed up succesfully")
    
    def login(self):
       input_user = self.txt01.get()
       input_pass = self.txt02.get() 
       #reset the info label
       self.info.config(text="")
       # iterate through the users list for validation
       for user,passw in users:
            if (user,passw) == (input_user,input_pass):
                #open the window and remove the login page
                self.blank_page()
                self.window.destroy()
                self.blank.mainloop()
        
       
    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        # call validate method if signin button is clicked
        if(event.widget == self.btn01):
            self.login()
            # call signup method if signup button is clicked
        if(event.widget == self.btn02):
            self.signup()       
        pass

# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
