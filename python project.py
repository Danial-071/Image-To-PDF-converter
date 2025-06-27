import numpy as np
import tkinter as tk
from tkinter import filedialog
import sys
from reportlab.pdfgen import canvas
import os
from PIL import Image,ImageTk
from reportlab.lib.colors import white
class imagetoPDF:
    def __init__(self,root):
        self.root=root
        self.image_paths=[]
        self.output_pdf=tk.StringVar()
        self.selected_images=tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.initialize()

    def initialize(self):   
        title_label=tk.Label(self.root,text="Image to PDF converter",font=("Helvetica",16,"bold"))
        title_label.pack(pady=12)

        select_button=tk.Button(self.root,text="Select Images",command=self.select_images)
        select_button.pack(pady=(30,30))

        self.selected_images.pack(pady=(0,10),fill=tk.BOTH,expand=True)

        label=tk.Label(self.root,text="Enter Output PDf label name")
        label.pack()

        self.pdf_name=tk.Entry(self.root,textvariable=self.output_pdf, width=40, justify="center")
        self.pdf_name.pack()
        
        convert_button=tk.Button(self.root,text="Convert",command=self.convert_images)
        convert_button.pack(padx=(20,20))

    def select_images(self):
      self.image_paths = filedialog.askopenfilenames(
      title="Select the file name",
      filetypes=[("Image files", "*.png *.jpeg *.jpg")])

      self.update_images()

    def update_images(self):
        self.selected_images.delete(0,tk.END)   
         
        for i in self.image_paths:
            file=os.path.basename(i)
            self.selected_images.insert(tk.END,file)

    def convert_images(self):
          if not self.image_paths:
              return
          pdf_path=self.pdf_name.get()+ ".pdf" if self.output_pdf.get() else "output.pdf"
          pdf=canvas.Canvas(pdf_path, pagesize=(612,792))
          for i in self.image_paths:
              image=Image.open(i)
              availible_width=540
              availible_height=720
              scale_factor=min(availible_width/image.width , availible_height/image.height)
              new_width=image.width*scale_factor
              new_height=image.height*scale_factor
              x_centered=(612-new_width)/2
              y_centered=(792-new_height)/2
            
              pdf.setFillColor(white)
              pdf.rect(0,0,612,792,fill=True)
              pdf.drawInlineImage(i,x_centered,y_centered,width=new_width, height=new_height)

              pdf.showPage()
          pdf.save()   
     

def main():
   root=tk.Tk()   
   root.title("Image to PDF converter")
   converter=imagetoPDF(root)
   root.geometry("1000x500")
   root.mainloop()

if __name__=="__main__" :
   main() 