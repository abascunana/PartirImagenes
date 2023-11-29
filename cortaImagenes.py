import os
from tkinter import Tk, filedialog, Button
from PIL import Image
import ctypes

stop = False

def split(imgPath):
    img = Image.open(imgPath)
    w, h = img.size
    imgA = img.crop((0, 0, w // 2, h))
    imgB = img.crop((w // 2, 0, w, h))
    
    return imgA, imgB

def stop_program():
    global stop
    stop = True
    ctypes.windll.user32.MessageBoxW(0, "Programa Detenido", "Programa Detenido", 0)

def select_directory():
    global stop
    stop = False
    directory_path = filedialog.askdirectory()
    if directory_path:
        process_images(directory_path)

def process_images(directory):
    global stop
    splitted_directory = os.path.join(directory, "splitted_images")
    os.makedirs(splitted_directory, exist_ok=True)
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) and not stop:
            img_path = os.path.join(directory, filename)
            imgA, imgB = split(img_path)
            base_filename = os.path.splitext(filename)[0]  
            imgA.save(os.path.join(splitted_directory, f"{base_filename}_A.png"))
            imgB.save(os.path.join(splitted_directory, f"{base_filename}_B.png"))

# GUI setup
root = Tk()
root.title("Corta Imagenes")

select_button = Button(root, text="Selecciona carpeta", command=select_directory)
select_button.pack(pady=20)
stop_button = Button(root, text="Parar acción", command=stop_program)
stop_button.pack(pady=21)

root.mainloop()
