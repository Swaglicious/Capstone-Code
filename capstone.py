

import time
from mfrc522 import SimpleMFRC522

# Vairable IDs
# FLASH_vid1 = put path
# FLASH_vid2 = put path
# FLASH_vid3 = put path
# FLASH_vid4 = put path
# STATIC_vid = put path
# SENSOR_ONE = put id
# SENSOR_TWO = put id
# SENSOR_THREE = put id
# SENSOR_FOUR = put id

try:
    print("Starting default loop...")
    play_loop(STATIC_vid)

    while True:
        id, text = reader.read_no_block()

        if id is not None:
            print(f"RFID detected: {id}")

            if id == TARGET_TAG_ID:
                print("Matched target tag!")

                player.stop()
                time.sleep(1)

                play_once(SPECIAL_VIDEO)
                wait_until_finished()

                print("Returning to default loop...")
                play_loop(DEFAULT_VIDEO)

            else:
                print("Unknown tag")

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Exiting...")
    player.stop()