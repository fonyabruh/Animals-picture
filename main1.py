import requests
import shutil
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox, filedialog
from os import remove

def finish():
    root.destroy()
    try:
        remove('cat.png')
        remove('fox.png')
        remove('dog.png')
    except FileNotFoundError:
        pass
def image_cat():
    image_url = requests.get("https://api.thecatapi.com/v1/images/search").json()[0]["url"]
    image_response = requests.get(image_url, stream=True)
    with open("cat.png", "wb") as file:
        shutil.copyfileobj(image_response.raw, file)
    show('cat')
def show(name):
    img = Image.open(f"{name}.png")
    width, height = img.size
    imgroot = tk.Toplevel(root)
    imgroot.title(name.title())
    imgroot.geometry(f"{width}x{height+40}")
    photo = ImageTk.PhotoImage(img)
    imglabel = tk.Label(imgroot, image=photo)
    btn = tk.Button(imgroot, text = f"Download {name}", command = lambda: save_image(name), width = 10,height = 2)
    btn.pack(side=tk.TOP)
    imgroot.resizable(False, False)
    imglabel.pack()
    imgroot.mainloop()
def image_dog():
    response = requests.get(requests.get("https://dog.ceo/api/breeds/image/random").json()["message"], stream=True)
    with open("dog.png", "wb") as file:
        shutil.copyfileobj(response.raw, file)
    show('dog')
def save_image(name):
    file_path = filedialog.asksaveasfilename(defaultextension = ".png", filetypes = [("PNG Files", "*.png"), ("All Files", "*.*")])
    if file_path:
        try:
            shutil.copy(f"{name}.png", file_path)
            messagebox.showinfo("Сохранено", "Изображение успешно сохранено.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить изображение:\n{str(e)}")
def image_fox():
    response = requests.get(requests.get("https://randomfox.ca/floof/").json()["image"], stream=True)
    with open("fox.png", "wb") as file:
        shutil.copyfileobj(response.raw, file)
    show('fox')

root = tk.Tk()
root.title("Загрузка котика")
root.title("meow")
root.resizable(True, True)
root.iconphoto(True, tk.PhotoImage(file = "icon.png"))
root.geometry("300x300")
root.protocol("WM_DELETE_WINDOW", finish)
root. resizable(False, False)

button1 = tk.Button(root, text="Show cat", command=image_cat, width=10, height=2)
button2 = tk.Button(root, text="Show dog", command=image_dog, width=10, height=2)
button3 = tk.Button(root, text="Show fox", command=image_fox, width=10, height=2)

button3.pack(side=tk.RIGHT)
button1.pack(side=tk.LEFT)
button2.pack(side=tk.TOP)


root.mainloop()