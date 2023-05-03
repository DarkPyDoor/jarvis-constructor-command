import tkinter as tk
from tkinter import Misc

import os
from typing import Union, List


def create_labels(count: int, root: Union[Misc, None]) -> List[tk.Label]:
    labels = [tk.Label(root, text='Какое слово/фразу нужно сказать для запуска:') for i in range(count)]
    return labels


def create(path: str):
    try:
        os.mkdir(f"{path}/ahk")
    except Exception as e:
        print("Ошибка:", e)


