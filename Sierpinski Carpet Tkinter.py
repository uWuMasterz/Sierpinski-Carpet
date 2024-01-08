try:
    from Tkinter import *
except:
    from tkinter import *

if __name__ == "__main__":


    root = Tk()
    canvas = Canvas(root, width = 500, height = 500, bg = "white")
    canvas.pack()
    x = 0
    y = 0

    def draw(n,widthSize):
        global x,y
        if n == 0:
            canvas.create_rectangle((x, y, x+widthSize, y+widthSize), width = 1, fill ="black")

        else:
            for a in range (4):
                for j in range (2):
                    draw(n-1,widthSize/3)

                    if a == 0:
                        x = x + widthSize/3

                    elif a == 1:
                        y = y + widthSize/3


                    elif a == 2:
                        x = x - widthSize/3


                    elif a == 3:
                        y = y - widthSize/3

                """
                if a == 0:
                    for j in range (2):
                        draw(n-1,widthSize/3)
                        x = x + widthSize/3

                elif a == 1:
                    for j in range (2):
                        draw(n-1,widthSize/3)
                        y = y + widthSize/3


                elif a == 2:
                    for j in range (2):
                        draw(n-1,widthSize/3)
                        x = x - widthSize/3


                elif a == 3:
                    for j in range (2):
                        draw(n-1,widthSize/3)
                        y = y - widthSize/3
                        """
    draw(4,500)
    root.mainloop()
