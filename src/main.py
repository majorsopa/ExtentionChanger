import tkinter as tk, os

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'files to change')

window = tk.Tk(className = 'extension changer')
window.geometry('800x250')

textBoxFrame = tk.Frame(master = window, width = 30, height = 10)
extensionToChangeTo = tk.Entry(width = 30)

def changeExtension(endingExtension):

  f = []

  for (dirpath, dirnames, filenames) in os.walk(path):
    
    f.extend(filenames)
  
    j = 0

    for x in filenames:

      file = filenames[j]
      splitAt = file.rfind('.') + 1

      r = file[splitAt:]
      lengthToRemove = len(r)
      file = file[:-lengthToRemove]

      file += endingExtension
      os.rename(path + '/' + filenames[j] , path + '/' + file)

      j += 1

    break

def handle_button_press(event): 
  changeExtension(extensionToChangeTo.get())

buttonFrame = tk.Frame(master = window, width = 20, height = 10)

convertButton = tk.Button(master = buttonFrame, text = 'CONVERT!!!')
convertButton.bind('<Button-1>', handle_button_press)

instructionsFrame = tk.Frame(master = window, width = 200, height = 200)

instructions = tk.Label(master = instructionsFrame, text = 'Place the files you want to change the extension of in the "files to change" folder.\nAll of those file extensions will be changed to the extension you choose by typing in the box, when you press the button.\nExample of what you would type in the box, "png", "jpeg", "txt".\nKindly note the lack of "."')

instructionsFrame.pack(padx = 1, pady = 4)
buttonFrame.pack(padx = 1, pady = 1)
textBoxFrame.pack(padx = 1, pady = 4)

instructions.pack()
convertButton.pack()
extensionToChangeTo.pack()

window.mainloop()
