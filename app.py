import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW #do not remove
instant = 0
sizeofletter = 0
import os
FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(FOLDER, 'mostcommonpasswords.txt')
def split(word):
    return [char for char in word]
class TestPassword(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))#creates starting box

        password_label = toga.Label(#creates text "Password:"
            'Password: ',
            style=Pack(padding=(200, 5))#set at pos 200px, 5ox
        )
        self.password_input = toga.TextInput(style=Pack(padding=(200, 5), flex=1))
        #sets place to text input
        name_password = toga.Box(style=Pack(direction=ROW, padding=5))#creates box which contains text and input
        name_password.add(password_label)#adds text and input
        name_password.add(self.password_input)

        button = toga.Button(#creation of button with text "Test Password"
            'Test Password',
            on_press=self.bruteforce,#on press returns text in input
            style=Pack(padding=(20, 5))#location of button
        )

        main_box.add(name_password)#adds box containing input and text to starting box
        main_box.add(button)#adds button to box

        self.main_window = toga.MainWindow(title=self.formal_name)#creates window
        self.main_window.content = main_box
        self.main_window.show()

    def returnpassword(self, widget):
        print(self.password_input.value)#prints the password inputted into console -- subject to change
    def iscommon(self,widget):#checks if password is in the top 10^6 most common passwords
        with open(my_file) as mostcommonfile:
            contents = mostcommonfile.read()
            if self.password_input.value in contents:
                instant = 1#sets instant to 1, meaning that the password would be instantly cracked
    def bruteforce(self,widget):#checks amount of time needed for average desktop cpu to bruteforce the password
        #print(lettercheck) debugging
        if self.password_input.value.isalpha():#checks if has only letters
            if self.password_input.value.isupper() or self.password_input.value.islower():
                sizeofletter = 26#if only upper or lower
            else:
                sizeofletter = 52#if both
        else:
            if self.password_input.value.isnumeric():
                sizeofletter = 10#if only numbers
            else:
                sizeofletter = 100#if letters, numbers, and symbols
        timeTaken = (sizeofletter ** len(self.password_input.value) / (4*10^9))#calculates timetaken
        #print(sizeofletter) debugging
        print(timeTaken)#prints amount of time taken in seconds
                               
def main(): #do not remove
    return TestPassword()

