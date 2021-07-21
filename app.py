import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW #do not remove
instant = 0
sizeofletter = 0
import os
PASSFOLDER = os.path.dirname(os.path.abspath(__file__))
passfile = os.path.join(PASSFOLDER, 'mostcommonpasswords.txt')
WORDFOLDER = os.path.dirname(os.path.abspath(__file__))
wordfile = os.path.join(WORDFOLDER, 'englishdictionary.txt')
Howmuchtime = "Your password would be cracked in "
textTaken = ""
class TestPassword(toga.App):

    def startup(self):

        main_box = toga.Box(style=Pack(direction=COLUMN))

        password_label = toga.Label(#creates text "Password:"
            'Password: ',
            style = Pack(direction = COLUMN
            ))
        
        self.password_input = toga.TextInput(style = Pack(direction = COLUMN, padding = (100, 5)))
        #sets place to text input
        name_password = toga.Box(style=Pack(direction=COLUMN))#creates box which contains text and input
        name_password.add(password_label)#adds text and input
        name_password.add(self.password_input)
        

        button = toga.Button(#creation of button with text "Test Password"
            'Test Password',
            on_press=self.bruteforce#on press returns text in input
            #location of button
        )
        self.isPIN = toga.Switch("Password is a PIN", id=None, on_toggle=None, is_on=False, enabled=True, factory=None)
        self.HowMuchTime = toga.Label("aaaa ")
        name_password.add(self.isPIN)
        name_password.add(self.HowMuchTime)
        main_box.add(name_password)#adds box containing input and text to starting box
        main_box.add(button)#adds button to box

        self.main_window = toga.MainWindow(title=self.formal_name,size = (400, 700))#creates window
        self.main_window.content = main_box
        self.main_window.show()
    def bruteforce(self,widget):
        if self.isPIN.is_on is True:
            sizeofletter = 10
        else:
            sizeofletter = 62
        timeTaken = (sizeofletter ** len(self.password_input.value) / (4*10^9))#calculates timetaken
        with open(passfile) as mostcommonfile:
            contents = mostcommonfile.read()
            if self.password_input.value in contents:
                textTaken = "Your password would be broken instantly as it is one of the most common passwords in the world"
                timeTaken = -1
        with open(wordfile) as dictionaryfile:
            wordfilecontent = dictionaryfile.read()
            if self.password_input.value in wordfilecontent:
                textTaken = "Your password would be broken instantly as it is a word in the english dictionary"
                timeTaken = -1
        if float(timeTaken) >= 31536000:
            dateTime = timeTaken / 31536000
            textTaken = "It would take {} Years to crack this password".format(int(dateTime))
        if 2592000 <= float(timeTaken) < 31536000:
            dateTime = float(timeTaken) / 259200
            textTaken = "It would take {} Months to crack this password".format(int(dateTime))
        if 86400 <= float(timeTaken) < 2592000:
            dateTime = float(timeTaken) / 86400
            textTaken = "It would take {} Days to crack this password".format(int(dateTime))
        if 3600 <= float(timeTaken) < 86400:
            dateTime = float(timeTaken) / 3600
            textTaken = "It would take {} Hours to crack this password".format(int(dateTime))
        if 60 <= float(timeTaken) < 3600:
            dateTime = float(timeTaken) / 60
            textTaken = "It would take {} Minutes to crack this password".format(int(dateTime))
        if 0 < float(timeTaken) < 60:
            textTaken = "It would take {} Seconds to crack this password".format(int(dateTime))
        if float(timeTaken) == 0:
            textTaken = "Your password would be cracked instantly"
        self.HowMuchTime.text = textTaken    
        
          
def main(): #do not remove
    return TestPassword()

