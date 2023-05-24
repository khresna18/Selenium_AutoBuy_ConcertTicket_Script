import os
import time

def open_exe_file(file_path, interval, browser):
    h = 0
    while True:
        os.startfile(file_path)
        time.sleep(interval)
        h = h + 1
        if h == browser :
            break
        

# Example usage
file_path = "C:/Users/ASUS/Desktop/script coldplay/dist/Runner.exe"  # Replace with the actual path to your .exe file
interval = 0.01
browser = 2
open_exe_file(file_path, interval, browser)



print_hello(interval)
