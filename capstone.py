
#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import os

reader = SimpleMFRC522()


##Variables for Files
visual_files ={
    551721708274: "/home/campse/caps/env/one.mp4",
    207537121893: "/home/campse/caps/env/two.mp4",
    482431805988: "/home/campse/caps/env/three.mp3"
    }

##Loop for clues to be played
    
try:
    print:("Scan Item For Clue.....")
    
    while True:
        id= reader.read() [0];
        print(id);
        
        
        if id in visual_files:
            file_path = visual_files[id]
            print("Playing Clue For Item:", id)
            
            if file_path.endswith(".mp4"):
                os.system(f"cvlc --fullscreen --play-and-exit --no-video-title-show '{file_path}'")
                
            elif file_path.endswith(".mp3"):
                os.system(f"mpg321 '{file_path}'")
                
            else:
                print("File Unsuporrted:", file_path)
                        
        else:
            print("Clue Not Found. Try Again.")
                    
finally:
    GPIO.cleanup()
    
