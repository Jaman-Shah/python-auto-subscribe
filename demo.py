import pyautogui
import time

mainPath = r"C:\Users\Dell\OneDrive\Desktop\first-python"

# Image file paths (if you need to use them later)


time.sleep(2)

minimizeBtn = mainPath + r"\minimize.PNG"
positionOfMinimize = pyautogui.locateOnScreen(minimizeBtn)
pyautogui.moveTo(positionOfMinimize)
pyautogui.leftClick(positionOfMinimize)

time.sleep(1)
# Open a new tab in the browser
pyautogui.hotkey("ctrl", "t")

# Wait for the new tab to open
time.sleep(3)

# Type "youtube" into the address bar
pyautogui.typewrite("youtube.com")

# Press Enter to navigate to YouTube
pyautogui.press("enter")

# Wait for YouTube to load completely
time.sleep(5)

# Now type "/" into the address bar or anywhere
pyautogui.typewrite("/")



pyautogui.typewrite("Stack Learner")
time.sleep(2)
pyautogui.press("enter")





time.sleep(3)

subscribeStackLearnerImage = mainPath + r"\stackLearner.PNG"
positionOfsubscribeStackLearnerImage = pyautogui.locateOnScreen(subscribeStackLearnerImage)
pyautogui.moveTo(positionOfsubscribeStackLearnerImage)

pyautogui.leftClick(positionOfsubscribeStackLearnerImage)













