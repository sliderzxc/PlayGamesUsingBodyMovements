import pyautogui


class ManageHandSwipes:
    valueHorizontal = 30
    valueVertical = 30

    def handle(self, coordinates, new_coordinates):
        if coordinates[0] > new_coordinates[0] + self.valueHorizontal:
            pyautogui.press('right')
            print("Right", end='\n\n\n')
        elif coordinates[0] < new_coordinates[0] - self.valueHorizontal:
            pyautogui.press('left')
            print("Left", end='\n\n\n')
        if coordinates[1] > new_coordinates[1] + self.valueVertical:
            pyautogui.press('up')
            print("Up", end='\n\n\n')
        elif coordinates[1] < new_coordinates[1] - self.valueVertical:
            pyautogui.press('down')
            print("Down", end='\n\n\n')
        return new_coordinates
