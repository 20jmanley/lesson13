from guizero import App, TextBox, PushButton, yesno, MenuBar, warn


def openFile():
    pass

def saveFile():
    pass

def encryptFile():
    warn("Error", "I don't know how to do that yet")
    
def decryptFile():
    warn("Error", "I don't know how to do that yet")


def closeHandler():
    if yesno("close", "Do you want to quit without saving?"):
        app.destroy()

app = App(title="untitled", height=600, width=600)
data = TextBox(app, height=600, width=600, multiline=True, scrollbar=True)
menubar = MenuBar(app, toplevel = ["File", "Encrypt"],
                  options=[
                      [["Open File", openFile], ["Save File", saveFile]],
                      [["Encrypt", encryptFile], ["Decrypt", decryptFile]]
                    ])
app.on_close(closeHandler)
app.display()