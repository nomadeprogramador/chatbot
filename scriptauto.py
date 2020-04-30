#1 posicao > 2 > clicarD > 3 Scroll > ClickD > Scroll
import pyautogui
import time
pyautogui.confirm(text='ByProgramador.nomade', title='@programador.nomade', buttons=['OK', 'Cancel'])
time.sleep(2) # PosI = Point(x=472, y=284)
pyautogui.moveTo(x=502,y=284)
print(pyautogui.position())
# Size(width=1366, height=768)
#print(pyautogui.size())
time.sleep(2)
for i in range(1,30):
    pyautogui.doubleClick()
    time.sleep(0.5)
    pyautogui.scroll(-25)
    pyautogui.moveTo(x=502,y=300)
    print(pyautogui.position())
