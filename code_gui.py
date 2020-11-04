# requires installation of the pyautogui module
from pyautogui import *
n = prompt(text="Enter the length of your pinus: ", title="View pinus", default="")
alert(text=f"""Your pinus: 

8{int(n)*"="}D""", title="View pinus", button="OK")