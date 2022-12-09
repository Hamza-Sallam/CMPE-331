"""
    Stage: Development-01
    @author: Hamza Sallam , 120200013
    @author:  mert şen, 119200031

"""

import tkinter as tk

# create a list of users 
users = [ ('mert','pass'),('hamza','pass'),('admin','admin')]

class LoginWindow:
    # constructor
    def __init__(self):
        self.window = tk.Tk()
        # add a title for the login page
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
        #add a new label
        self.title = tk.Label(text="Super Market Login Page")
        self.lbl01 = tk.Label(text="User name")
        self.lbl02 = tk.Label(text="Password")

        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry()

        self.btn01 = tk.Button(text="login")
        self.btn02 = tk.Button(text="signup")

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-1>", self.handle_click)


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.title.grid(row=1, column=0, padx=10, pady=10)
        self.lbl01.grid(row=1, column=0, padx=10, pady=5)
        self.txt01.grid(row=1, column=1, padx=10, pady=5)

        self.lbl02.grid(row=2, column=0, padx=10, pady=5)
        self.txt02.grid(row=2, column=1, padx=10, pady=5)

        self.btn01.grid(row=3, column=0, padx=10, pady=5)
        self.btn02.grid(row=3, column=1, padx=10, pady=5)

    def blank_page(self):
        self.blank = tk.Tk()
        # add a title for the login page
        self.blank.title('Home')
        self._initializeGUI()
        #adjust size to 500x500
        self.blank.geometry('500x500')
        self._addGUIElementsToFrame()

    def login(self):
        usrnm = self.lbl01.g

    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        pass



# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
