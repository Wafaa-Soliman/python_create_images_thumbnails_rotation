from PIL import Image, ExifTags
import glob
import os
import ntpath
import tkinter
import tkinter.filedialog
from tkinter import ttk, messagebox
from tkinter.ttk import *

form = tkinter.Tk()

w = 600
h = 400
sw = form.winfo_screenwidth()
sh = form.winfo_screenheight()
x = (sw - w) / 2
y = (sh - h) / 2

form.geometry('%dx%d+%d+%d' % (w, h, x, y))

  
# This will create style object 
style = Style() 
  
# This will be adding style, and  
# naming that style variable as  
# W.Tbutton (TButton is used for ttk.Button). 
  
style.configure('select.TButton', font =
               ('calibri', 20, 'bold'), 
                foreground = 'blue') 

style.configure('create.TButton', font =
               ('calibri', 20, 'bold'), 
                foreground = 'green') 

style.configure('quit.TButton', font =
               ('calibri', 20, 'bold'), 
                foreground = 'red') 

def closeForm():
    form.destroy()
def openFolder():
    folder_selected = tkinter.filedialog.askdirectory()
    openFolder.dirPath = folder_selected + '/*JPG'
    # print(openFolder.dirPath)

def img_thumb_rotate():
        
    for infile in glob.glob(openFolder.dirPath):
        # file : maen path and name of image without extension
        # infile: mean image name and path  with Extension
        file, ext = os.path.splitext(infile)
        targetPath = os.path.dirname(file)
        # print(targetPath)
        imName = ntpath.basename(infile)
        # print(imName)
        im = Image.open(infile)

        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        try:
            exif = dict(im._getexif())

            if exif:
                exif = dict(exif.items())
                if exif[orientation] == 3:
                    im = im.rotate(180, expand=True)
                    im.save(targetPath + "\\" + imName, "JPEG")
                elif exif[orientation] == 6:
                    im = im.rotate(270, expand=True)
                    im.save(targetPath + "\\" + imName, "JPEG")

                elif exif[orientation] == 8:
                    im = im.rotate(90, expand=True)
                    im.save(targetPath + "\\" + imName, "JPEG")
        except:
            # There is AttributeError: _getexif sometimes.
            pass
        # print(im)
        w, h = im.size
        imgSize = os.path.getsize(infile)
        if imgSize < 2000000:
            sizeThum = 0.6 * w, 0.8 * h
            # print(sizeThum)
            im.thumbnail(sizeThum)
            im.save(targetPath + "\\" + "thubm_" + imName, "JPEG")
        else:
            sizeThum = 0.2 * w, 0.3 * h
            # print(sizeThum)
            im.thumbnail(sizeThum)
            im.save(targetPath + "\\" + "thubm_" + imName, "JPEG")

    messagebox.showinfo("Successfully", "Successfully Created Thumbnails And Rotated Images")

selectBtn = Button(form, text='Select Directory', style='select.TButton', command=openFolder)
selectBtn.grid(row = 2, column = 7, pady = 30, padx=200, ipady=10, ipadx=10)

createBtn = Button(form, text='Create Thumbnail And Rotate Images', style='create.TButton', command=img_thumb_rotate)
createBtn.grid(row = 7, column = 7, pady = 30, ipady=10, ipadx=10)

closeBtn = Button(form, text='Quit !', style = 'quit.TButton', command=closeForm)
closeBtn.grid(row = 15, column = 7, pady = 30, ipady=10, ipadx=10)

form.resizable(False, False)
form.title('Creating images thumbnails and Rotation')
form.mainloop()



