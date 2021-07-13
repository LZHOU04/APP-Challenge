import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW #do not remove


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
            on_press=self.returnpassword,#on press returns text in input
            style=Pack(padding=(20, 5))#location of button
        )

        main_box.add(name_password)#adds box containing input and text to starting box
        main_box.add(button)#adds button to box

        self.main_window = toga.MainWindow(title=self.formal_name)#creates window
        self.main_window.content = main_box
        self.main_window.show()

    def returnpassword(self, widget):
        print(self.password_input.value)#prints the password inputted into console -- subject to change

def main(): #do not remove
    return TestPassword()

