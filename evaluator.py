from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os

class Evaluator():
    def __init__(self, root, img, tx_attributes):

        self.my_img=ImageTk.PhotoImage(Image.open("./masterdumps/"+img))
        self.root=root
        self.tx_attributes=tx_attributes

        if not tx_attributes[7]:
            self.upPath="./gigapixel/"
        else:
            self.upPath="./ESRGAN/"
        try:
            self.upImg = ImageTk.PhotoImage(Image.open(self.upPath+img))
        except:
            self.upImg = ImageTk.PhotoImage(Image.open("404.png"))
        self.leftFrame = Frame(self.root, width=600, height=990, padx=5, pady=5)
        self.leftFrame.pack(side=LEFT,anchor=N)
        self.rightFrame = Frame(self.root, width=1300, height=990, padx=5, pady=5)
        self.rightFrame.pack(side=LEFT, anchor=NW, expand=1)

        

    def display_original(self):
        
        self.display=LabelFrame(self.leftFrame, text=self.tx_attributes[0], bd=5, width=600, height=600, pady=10)
        self.display.pack(side=TOP, fill=BOTH, anchor=S, expand=1)
        self.eval_img=Label(self.display, image=self.my_img, height=600, width=600)
        self.eval_img.pack(side=TOP, fill=Y, anchor=CENTER, expand=1)

    def eval_frame(self):
        self.evalframe=LabelFrame(self.leftFrame, text="Classify texture:", width=600, bd=5, height=300, padx=10, pady=10)
        self.evalframe.pack(side=BOTTOM,fill=BOTH, expand=0)
        
        self.sizelabel=Label(self.evalframe, text="Dimensions: "+str(self.my_img.width())+"x"+str(self.my_img.height())+" px")
        self.sizelabel.pack(side=TOP, expand=0)

        self.gname=StringVar(self.root)
        self.gname.set(str(self.tx_attributes[1]))
        self.gnamelabel=Entry(self.evalframe, textvariable=self.gname)
        self.gnamelabel.pack(side=TOP, fill=X, expand=1)
        optionList=["New", "Ground", "Wall", "Metallic", "Object/Prop", "NPC", "Enemy", "Foliage",
                    "UI", "Zack - 2nd Class", "Zack - 1st Class", "Zack - Buster Sword", "Cissnei", "Tseng", "Angeal", "Genesis", "Hollander", "Lazard", "Sephiroth", "Cloud", "Tifa"]

        self.catoption = StringVar(self.root)
        self.catoption.set(self.tx_attributes[4])
        print(self.catoption.get())
        
        self.catlist = OptionMenu(self.evalframe, self.catoption, *optionList)
        self.catlist.pack(side=TOP, fill=X, expand=1)

        self.hastextvar=IntVar(self.root)
        self.hastextvar.set(self.tx_attributes[5])
        self.hastext=Checkbutton(self.evalframe, text="Text element?", variable=self.hastextvar)
        self.hastext.pack(side=LEFT, expand=1)

        self.hasshinravar=IntVar(self.root)
        self.hasshinravar.set(self.tx_attributes[6])
        self.hasshinra=Checkbutton(self.evalframe, text="Shinra Logo?", variable=self.hasshinravar)
        self.hasshinra.pack(side=LEFT, fill=X, expand=1)

        self.useesrganvar=IntVar(self.root)
        self.useesrganvar.set(self.tx_attributes[7])
        self.useesrgan=Checkbutton(self.evalframe, text="Use ESRGAN?", variable=self.useesrganvar)
        self.useesrgan.pack(side=LEFT, fill=X, expand=1)

        self.ignoretexturevar=IntVar(self.root)
        self.ignoretexturevar.set(self.tx_attributes[8])
        self.ignoretexture=Checkbutton(self.evalframe, text="Ignore texture", variable=self.ignoretexturevar)
        self.ignoretexture.pack(side=BOTTOM, fill=X, expand=1)
        
        
    def write_record(self):
        update_attributes = [self.gname.get(), self.catoption.get(), self.hastextvar.get(), self.hasshinravar.get(), self.useesrganvar.get(), self.ignoretexturevar.get(), self.tx_attributes[0] ]

        return update_attributes

    def update_frames(self, img, tx_attributes):
        self.tx_attributes=tx_attributes
        if not tx_attributes[7]:
            self.upPath="./gigapixel/"
        else:
            self.upPath="./ESRGAN/"
        try:
            self.upImg = ImageTk.PhotoImage(Image.open(self.upPath+img))
        except:
            self.upImg = ImageTk.PhotoImage(Image.open("404.png"))
        self.my_img=ImageTk.PhotoImage(Image.open("./masterdumps/"+img))
        self.upscaled_img['image'] = self.upImg
        self.display['text']=self.tx_attributes[0]
        self.eval_img['image']=self.my_img
        self.sizelabel['text']="Dimensions: "+str(self.my_img.width())+"x"+str(self.my_img.height())+" px"
        self.gname.set(str(self.tx_attributes[1]))
        self.catoption.set(self.tx_attributes[4])
        self.hastextvar.set(self.tx_attributes[5])
        self.hasshinravar.set(self.tx_attributes[6])
        self.useesrganvar.set(self.tx_attributes[7])
        self.ignoretexturevar.set(self.tx_attributes[8])

    def return_left(self):
        return self.leftFrame
    def openImages(self):
        origPath=(os.getcwd()+'/masterdumps/'+self.tx_attributes[0])
        upscalePath=(os.getcwd()+self.upPath+self.tx_attributes[0])
        os.startfile(origPath)
        print(origPath)
        os.startfile(upscalePath)
        print(upscalePath)

    def drawOpen(self):
        self.button_Open=Button(self.leftFrame, text="Open in Editor", command=lambda: self.openImages())
        self.button_Open.pack(side=BOTTOM, anchor = S, fill=X)
        #self.button_Open.bind('<Button-1>', self.openImages)
################################################### RIGHT PANEL #################################################################

    def display_upscale(self):
        self.updisplay=LabelFrame(self.rightFrame, text=(self.upPath+self.tx_attributes[0]), bd=5, width=1300, height=1000, pady=10)
        self.updisplay.pack(fill=BOTH, anchor=W, expand=1)
        self.upscaled_img=Label(self.updisplay, image=self.upImg, height=990, width=1290)
        self.upscaled_img.pack(side=LEFT, fill=BOTH, expand=1)
    

        


        """try:
            os.startfile(origPath)
        except:
            #os.startfile("404.png")
            print("coudln't open")
        try:
            #os.startfile("404.png")
            print("coudln't open")
        except:
            os.startfile("404.png")"""
        
