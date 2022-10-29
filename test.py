import pygetwindow as pw
import pyautogui
from mss import mss
from PIL import Image
#init vars
name = __file__.split("\\")[-1]
path = __file__[:-len(name)]
windows = pw.getWindowsWithTitle("edge")[0]
bbox_r = (int(windows.left),int(windows.top),int(windows.right),int(windows.bottom))
def capture_screenshot():
    # Capture entire screen
    with mss() as sct:
        monitor = sct.monitors[0]
        sct_img = sct.grab(monitor)
        # Convert to PIL/Pillow Image
        return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

pic1 = capture_screenshot()
pic1.show()
print(windows.size)
print(windows)