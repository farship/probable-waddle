#Test Based




class Clipping():
    global paperclipcount
    intpaperclipcount = 0
    
    def displayPaperclipCount(self):
        print ('Clips: ' + str(paperclipcount))
    
    def addclip(quantity):
        paperclipcount =+ quantity

if __name__ == "__main__":
    ex = Clipping()