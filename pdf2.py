import tkinter as tk
from tkinter import filedialog
import os 
import pandas as pd
from PIL import Image
window = tk.Tk()
window.wm_attributes('-topmost', 1)
window.withdraw()
def merge_images_to_pdf(directory_path):
    image_files = [f for f in os.listdir(directory_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    image_files.sort()

    if not image_files:
        print("No image files found in the selected directory.")
        return

    pdf_filename = os.path.join(directory_path, 'merged_images.pdf')
    images = [Image.open(os.path.join(directory_path, img)) for img in image_files]
    images[0].save(pdf_filename, save_all=True, append_images=images[1:])

    print(f"PDF created successfully: {pdf_filename}")

def merge_image_to_pdf(file_path):
    image_file = file_path
    dot_index = file_path.rfind('.')
    file_path = file_path[:dot_index] + '.pdf'
    pdf_filename = file_path
    print(pdf_filename)
    images = Image.open(image_file)
    images = images.convert("RGB")
    images.save(pdf_filename)
    print(f"PDF created successfully : {pdf_filename}")


def selectfile():
    file_path = filedialog.askopenfilename(parent=window, title="Select a File", filetypes=(("All files", "*.*"),("Text files", "*.txt")))
    if file_path:
        merge_image_to_pdf(file_path)
def selectfolder():
    directory_path = filedialog.askdirectory(title="Select Directory")
    if directory_path:
        merge_images_to_pdf(directory_path)

while True:
    print("1. Convert single file to PDF")
    print("2. Convert multiple files to PDF")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        print("Convert given file to PDF")
        selectfile()

    elif choice == '2':
        print("Converting given files to PDF")
        selectfolder()

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")












