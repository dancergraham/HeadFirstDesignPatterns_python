from tkinter import Tk, OptionMenu, mainloop, StringVar, Menu, Label
from PIL import ImageTk, Image

class ImageProxy(Image):
    def __init__(self, url):
        super().__init__(self)
        self.url = url
        self._size = (800, 600)


def main():
    albums = {"Buddha Bar": r"http://images.amazon.com/images/P/B00009XBYK.01.LZZZZZZZ.jpg",
              "Ima": r"http://images.amazon.com/images/P/B000005IRM.01.LZZZZZZZ.jpg",
              "Karma": r"http://images.amazon.com/images/P/B000005DCB.01.LZZZZZZZ.gif",
              "MCMXC a.D.": r"http://images.amazon.com/images/P/B000002URV.01.LZZZZZZZ.jpg",
              "Northern Exposure": r"http://images.amazon.com/images/P/B000003SFN.01.LZZZZZZZ.jpg",
              "Selected Ambient Works: Vol. 2": r"http://images.amazon.com/images/P/B000002MNZ.01.LZZZZZZZ.jpg"
              }
    album = "Selected Ambient Works: Vol. 2"
    url = albums[album]
    root = Tk()
    menubar = Menu(root)
    label = StringVar(root)
    label.set(album)
    menu = OptionMenu(root, label, *albums.keys())
    menubar.add_cascade(label="Album", menu=menu)
    menu.pack()
    img = r"C:\Users\Graham Knapp\OneDrive - Acernis AG\Pictures\Graham Knapp head WTTJ.jpg"
    img = Image.open(img)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.pack()
    mainloop()


if __name__ == '__main__':
    main()
