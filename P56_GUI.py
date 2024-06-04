# windows  = GUI elements: buttons, text boxes, labels, images
# windows = serves a sa contained to hold or contains these widgets

from pathlib import Path
from tkinter import *


def main():
    window = Tk()  # instantiate on instance of a window
    window.geometry("420x420")
    window.title("Test GUI")
    icon_path = Path(__file__).parent / 'Apple.png'
    for x in image_names():
        print(x)
    return

    assert icon_path.exists()

   #  Time 6:13