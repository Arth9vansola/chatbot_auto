import pyautogui
import time
import pyperclip

# Step 1: Click at the icon position (1011, 1044)
pyautogui.moveTo(985, 1047)  # Move to the position
time.sleep(0.5)               # Pause briefly
pyautogui.click()             # Perform the click

# Step 2: Drag from (1350, 150) to (1885, 945)
pyautogui.moveTo(1350, 150)   # Move to the starting position
time.sleep(0.5)               # Pause briefly
pyautogui.mouseDown()         # Press and hold the mouse button
pyautogui.moveTo(1885, 945, duration=1)  # Drag to the ending position (smoothly over 1 second)
pyautogui.mouseUp()           # Release the mouse button

# Step 3: Copy the selected text into the clipboard
pyautogui.hotkey('ctrl', 'c') # Send Ctrl+C to copy the text
time.sleep(0.5)               # Pause briefly for clipboard to update

# Step 4: Store clipboard content into a variable
copied_text = pyperclip.paste()

# Step 5: Print the copied text to verify
print("")
