from tkinter import *
import requests
from PIL import Image, ImageTk


def get_quote():
    kanye_api_resp = requests.get(url="https://api.kanye.rest/")
    kanye_api_resp.raise_for_status()
    response = kanye_api_resp.json()
    quote = response["quote"]
    canvas.itemconfig(quote_text, text=f"{quote}")
    print(quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
background_img = ImageTk.PhotoImage(Image.open("background.png"))
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207,
                                text="Kanye Quote Goes HERE",
                                width=250,
                                font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)
# kanye_img = PhotoImage(file="kanye.png")
kanye_img = ImageTk.PhotoImage(Image.open("kanye.png"))
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
