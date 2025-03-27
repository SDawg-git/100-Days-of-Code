import time
import pyautogui

screenWidth, screenHeight = pyautogui.size() #grabs the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position()
#print(currentMouseX, currentMouseY)

#280, 750      TOP LEFT             X SHOULD BE THE SAME FOR BOTH TOP LEFT AND BOTTOM LEFT
#290, 940      BOTTOM LEFT                          AND TOP BOTTOM RIGHT

#335, 800      TOP RIGHT            Y SHOULD BE THE SAME FOR TOP LEFT AND BOTTOM LEFT
#330, 945      BOTTOM RIGHT                         AND BOTTOM RIGHT AND BOTTOM LEFT


#possible refined coords:
#285, 775
#285, 940

#335, 775
#335, 940




time.sleep(5)
im1 = pyautogui.screenshot(region=(285,775,50,165))
#im1.save("C:\\Users\\dzemo\\Desktop\\Screenshot.png")
im1.save("Base.png")                             #used to make sure the area I specified is correct

while True:
    im2 = pyautogui.screenshot(region=(285,775,50,165))
    im2.save("Compare.png")
    if open("Compare.png", "rb").read() != open("Base.png", "rb").read():
        pyautogui.press("up")

    #the bot fails when the game gets faster, could consider moving the base screenshot to a bit to the right after
    #x amount of seconds. Could be difficult if it takes a screenshot if a cactus is in the way
