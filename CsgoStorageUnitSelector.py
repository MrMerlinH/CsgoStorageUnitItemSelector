import tkinter as tkk
import time, math
from pynput.mouse import Button, Controller

root = tkk.Tk()
root.title("CS:GO fast Storage")
mouse = Controller()
input_Number = tkk.Entry(root, width=10)
input_Number.grid(row=0, column=0)



def myClick():
   
    
    
    numberItems = int(input_Number.get())
    selectedItems_count = 0

    time.sleep(5)
    for scrollCount in range(0, 32):
        if (scrollCount % 8 == 0) and (scrollCount > 1):
            mouse.scroll(0, -1)
            time.sleep(0.20)
        for i in range (0,4):
            for x in range(0,8):
                if selectedItems_count >= numberItems:
                    break
                mouse.position = (300+190*x,250+220*i)
                selectedItems_count = selectedItems_count + 1
                time.sleep(0.015)
                mouse.click(Button.left, 1)
    
        if selectedItems_count >= numberItems:
            break
        mouse.scroll(0, -9)
        time.sleep(0.2)


myButton = tkk.Button(root, text="Start!", padx=50, pady=20, command=myClick)
myButton.grid(row=0, column=2)

myLabel4 = tkk.Label(root, text = "Open CS:GO fast after pressing the \"Start!\" Button")
myLabel4.grid(row=2, columnspan=3)


root.mainloop()
    



#280, 310  1:1
#480, 310  1:2
#280 530   2:1
#mouse.position = (285, 250)
#time.sleep(5)
#for scrollCount in range(0, 9):
    #mouse.scroll(0, -9)