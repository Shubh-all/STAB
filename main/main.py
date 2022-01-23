import datetime
from operator import itemgetter
from tkinter import *
from tkinter import ttk
from Results import *
from pathlib import Path
from EnterValues3.build.EnterValues3 import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from algo import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def main_window(splash_root):
    splash_root.destroy()
    window = Tk()
    window.geometry("1280x720")
    window.title("Result")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        80.0,
        fill="#3888FF",
        outline="")

    canvas.create_text(
        63.0,
        121.0,
        anchor="nw",
        text="Enter Values",
        fill="#3888FF",
        font=("Inter Medium", 28 * -1)
    )

    canvas.create_text(
        70.0,
        23.0,
        anchor="nw",
        text="STAB Calculator",
        fill="#FFFFFF",
        font=("Inter Bold", 28 * -1)
    )

    canvas.create_text(
        1176.0,
        28.0,
        anchor="nw",
        text="Version 2.3",
        fill="#FFFFFF",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        1129.0,
        48.0,
        anchor="nw",
        text="All Rights Reserved",
        fill="#FFFFFF",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        63.0,
        99.0,
        anchor="nw",
        text="Define Stocks & Sieves",
        fill="#273340",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        194.0,
        108.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        10.0,
        15.0,
        image=image_image_2
    )


    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        1118.0,
        55.0,
        image=image_image_3
    )

    # canvas.create_rectangle(
    #     136.0,
    #     203.0,
    #     776.0,
    #     398.0,
    #     fill="#F1F5FF",
    #     outline="")





    # entry_image_1 = PhotoImage(
    #     file=relative_to_assets("entry_1.png"))
    # entry_bg_1 = canvas.create_image(
    #     197.5,
    #     245.0,
    #     image=entry_image_1
    # )


    # button_image_1 = PhotoImage(
    #     file=relative_to_assets("button_1.png"))
    #

    # button_image_2 = PhotoImage(
    #     file=relative_to_assets("button_2.png"))
    # button_2 = Button(
    #     image=button_image_2,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_2 clicked"),
    #     relief="flat"
    # )
    # button_2.place(
    #     x=1094.0,
    #     y=223.0,
    #     width=108.0,
    #     height=31.0
    # )

    # canvas.create_rectangle(
    #     20.0,
    #     124.0,
    #     48.0,
    #     152.0,
    #     fill="#000000",
    #     outline="")

    # button_image_3 = PhotoImage(
    #     file=relative_to_assets("button_3.png"))
    # button_3 = Button(
    #     window,
    #     image=button_image_3,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_3 clicked"),
    #     relief="flat"
    # )
    # button_3.place(
    #     x=20.0,
    #     y=124.0,
    #     width=28.0,
    #     height=28.0
    # )

    #####HERE#####

    canvas.create_text(
        160.0,
        223.0,
        anchor="nw",
        text="Sieve Gradation",
        fill="#283341",
        font=("OpenSansRoman Regular", 18 * -1)
    )

    canvas.create_text(
        160.0,
        283.0,
        anchor="nw",
        text="No. of Stocks",
        fill="#283341",
        font=("OpenSansRoman Regular", 18 * -1)
    )

    canvas.create_text(
        160.0,
        318.0,
        anchor="nw",
        text="No. of Sieves",
        fill="#283341",
        font=("OpenSansRoman Regular", 18 * -1)
    )

    canvas.create_text(
        160.0,
        353.0,
        anchor="nw",
        text="Enter value of Sieve by",
        fill="#283341",
        font=("OpenSansRoman Regular", 18 * -1)
    )

    canvas.create_text(
        385.0,
        223.0,
        anchor="nw",
        text=":",
        fill="#283341",
        font=("OpenSansRoman Regular", 18 * -1)
    )

    canvas.create_text(
        385.0,
        283.0,
        anchor="nw",
        text=":",
        fill="#283341",
        font=("OpenSansRoman Regular", 18 * -1)
    )

    canvas.create_text(
        385.0,
        318.0,
        anchor="nw",
        text=":",
        fill="#283341",
        font=("OpenSansRoman Regular", 18 * -1)
    )

    canvas.create_text(
        385.0,
        353.0,
        anchor="nw",
        text=":",
        fill="#283341",
        font=("OpenSansRoman Regular", 18 * -1)
    )

    canvas.create_text(
        181.0,
        251.0,
        anchor="nw",
        text="Select the type of sieves used",
        fill="#283341",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    canvas.create_text(
        919.0,
        203.0,
        anchor="nw",
        text="Abbreviations",
        fill="#283341",
        font=("OpenSansRoman Regular", 14 * -1,"bold")
    )

    name=["WMM","DBM","BC","SMA","DLC","PQC"]

    y1=238
    for i in range(6):
        canvas.create_text(
            932.0,
            y1,
            anchor="nw",
            text=name[i],
            fill="#283341",
            font=("OpenSansRoman Regular", 12 * -1)
        )
        canvas.create_text(
            976.0,
            y1,
            anchor="nw",
            text=":",
            fill="#283341",
            font=("OpenSansRoman Regular", 12 * -1)
        )

        canvas.create_text(
            991.0,
            y1,
            anchor="nw",
            text="Lorem ipsum doler sit amen",
            fill="#283341",
            font=("OpenSansRoman Regular", 12 * -1)
        )
        y1+=24


    ###########DROP DOWNS#############

    ######numStockPiles######
    numStockPiles = IntVar()
    numStockPiles.set(2)
    Stock=ttk.Combobox(window, textvariable=numStockPiles,width=28,height=24)
    Stock['values']=(2,3,4,5)
    Stock.place(x=436,y=283, anchor="nw")
    Stock.current()
    ######numStockPiles######

    ######numStockPiles######
    numSieves = IntVar()
    numSieves.set(1)
    Sieves = ttk.Combobox(window, textvariable=numSieves, width=28, height=24)
    Sieves['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    Sieves.place(x=436, y=318, anchor="nw")
    Sieves.current()
    ######numStockPiles######

    ######numStockPiles######
    sieveGradation = StringVar()
    sieveGradation = ttk.Combobox(window, textvariable=sieveGradation, width=28, height=24)
    sieveGradation['values'] = ("WMM","DBM - 37.5mm","DBM - 26.5mm","BC - 19mm","BC - 13.2mm","SMA - 13mm","SMA - 19mm","DLC","PQC","Other")
    sieveGradation.place(x=436, y=222, anchor="nw")
    sieveGradation.current(0)
    ######numStockPiles######

    ###########DROP DOWNS#############

    button_1 = Button(
            window,
            text="Next -->",
            borderwidth=0,
            highlightthickness=0,
            bg="#3888FF",
            fg="#FFFFFF",
            command=lambda: Enter_Values3(window,numSieves,numStockPiles),
            relief="flat"
        )
    button_1.place(
        x=668.0,
        y=419.0,
        width=108.0,
        height=31.0
    )

    #####HERE#####
    window.resizable(False, False)
    window.mainloop()