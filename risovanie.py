#1
from tkinter import Tk, Canvas, Frame, BOTH
 
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Рисуем линии")
        self.pack(fill=BOTH, expand=1)
 
        canvas = Canvas(self)
        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
 
        canvas.pack(fill=BOTH, expand=1)
 
 
def main():
    root = Tk()
    ex = Example()
    root.geometry("400x250+300+300")
    root.mainloop()
 
 
if __name__ == '__main__':
    main()

#2
from tkinter import Tk, Canvas, Frame, BOTH
 
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Цвета")
        self.pack(fill=BOTH, expand=1)
 
        canvas = Canvas(self)
        canvas.create_rectangle(
            30, 10, 120, 80,
            outline="#fb0", fill="#fb0"
        )
 
        canvas.create_rectangle(
            150, 10, 240, 80,
            outline="#f50", fill="#f50"
        )
 
        canvas.create_rectangle(
            270, 10, 370, 80,
            outline="#05f", fill="#05f"
        )
 
        canvas.pack(fill=BOTH, expand=1)
 
 
def main():
    root = Tk()
    ex = Example()
    root.geometry("400x100+300+300")
    root.mainloop()
 
 
if __name__ == '__main__':
    main()

#3
from tkinter import Tk, Canvas, Frame, BOTH
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Рисуем формы")
        self.pack(fill=BOTH, expand=1)
 
        canvas = Canvas(self)
 
        # Овальная форма.
        canvas.create_oval(
            10, 10, 80, 80, outline="#f11",
            fill="#1f1", width=2
        )
 
        # Овальная форма.
        canvas.create_oval(
            110, 10, 210, 80, outline="#f11",
            fill="#1f1", width=2
        )
 
        # Рисуем прямоугольник.
        canvas.create_rectangle(
            230, 10, 290, 60,
            outline="#f11", fill="#1f1", width=2
        )
 
        # Рисуем дугу.
        canvas.create_arc(
            30, 200, 90, 100, start=0,
            extent=210, outline="#f11", fill="#1f1", width=2
        )
 
        points = [
            150, 100, 200, 120, 240, 180, 210,
            200, 150, 150, 100, 200
        ]
 
        # Рисуем многоугольник.
        canvas.create_polygon(points, outline='#f11',
            fill='#1f1', width=2)
 
        canvas.pack(fill=BOTH, expand=1)
 
 
def main():
    root = Tk()
    ex = Example()
    root.geometry("330x220+300+300")
    root.mainloop()
 
 
if __name__ == '__main__':
    main()

#4
from tkinter import Tk, Canvas, Frame, BOTH, NW
from PIL import Image, ImageTk
 
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Изображение в Canvas")
        self.pack(fill=BOTH, expand=1)
 
        self.img = Image.open("tatras.jpg")
        self.tatras = ImageTk.PhotoImage(self.img)
 
        canvas = Canvas(
            self, width=self.img.size[0]+20,
            height=self.img.size[1]+20
        )
 
        canvas.create_image(10, 10, anchor=NW, image=self.tatras)
        canvas.pack(fill=BOTH, expand=1)
 
 
def main():
    root = Tk()
    ex = Example()
    root.mainloop()
 
 
if __name__ == '__main__':
    main()

#5

rom tkinter import Tk, Canvas, Frame, BOTH, W
 
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Текст и Шрифт в Tkinter")
        self.pack(fill=BOTH, expand=1)
 
        canvas = Canvas(self)
        canvas.create_text(
            20, 30, anchor=W, font="DejavuSansLight",
            text="Красное солнце сгорает дотла"
        )
 
        canvas.create_text(
            20, 60, anchor=W, font="Arial",
            text="На пылающий город падает тень"
        )
 
        canvas.create_text(
            20, 130, anchor=W, font="TimesNewRoman",
            text="Перемен!"
        )
 
        canvas.create_text(
            20, 160, anchor=W, font="ComicSans",
            text="Требуют наши сердца"
        )
 
        canvas.create_text(
            20, 190, anchor=W, font="FreeSerif",
            text="Перемен!"
        )
 
        canvas.create_text(
            20, 220, anchor=W, font="LatoThin",
            text="Требуют наши глаза"
        )
 
        canvas.pack(fill=BOTH, expand=1)
 
 
def main():
    root = Tk()
    ex = Example()
    root.geometry("420x250+300+300")
    root.mainloop()
 
 
if __name__ == '__main__':
    main()
