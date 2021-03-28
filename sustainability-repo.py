import time
import pyfirmata
from datetime import datetime
from PIL import Image

photo_array = []
level_log = []
date = 0
x = 1
board = pyfirmata.Arduino('appropriate arduino information here')
levelmeter = 0  # measures level of rainwater tank


def initialization():
    """
    Starts compost_alert() and tank_level() functions.
    :return: Acknowledges that both functions have executed successfully.
    """
    compost_alert()
    tank_level()
    print("Initialization ongoing. Time: " + str(datetime.now()))
    return "The compost alert and tank level reporter have been initialized."


def dateset():
    """
    This function sets the current date every day from initial execution and saves it as a string in the format
    YYYYMMDD.
    :return: No return value.
    """
    global date
    global x

    while x > 0:
        date = datetime.now()

        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")
        date = year + month + day


def growth_array():
    """
    This function retrieves an image from the attached computer and stores it in a list, allowing gardeners to monitor
    long-term plant growth.
    :return: No return value.
    """
    global photo_array

    dateset()

    # Retrieves image from user filesystem and stores inside List photo_array.
    daily_image = Image.open("user directory" + str(date) + ".jpeg")
    photo_array = photo_array.append(daily_image)
    time.sleep(86400)  # seconds per day. runs 24hr after first init continuously


def tank_level():
    """
    Records tank level every 15 min and logs it in a list level_log, which is erased every 24hr (96 entries).
    :return:
    """
    global levelmeter
    global level_log

    log_description = "The current level of the rainwater tank in liters is "
    while True:
        if len(level_log) == 96:
            level_log = []
        levelmeter = board.get_pin('a:15:i')
        level_msg = log_description + str(levelmeter)
        level_log = level_log.append(levelmeter)
        print(level_msg)
        time.sleep(900)


def compost_alert():
    """
    Alerts user to fill composter A or B. Composters are filled every two weeks.
    Alerts on weekly basis at time of user initiation.
    :return: No return value.
    """
    weekscounter = 1
    while True:
        if weekscounter % 2 == 0:
            print("Fill Composter B!")
            weekscounter += 1
            time.sleep(604800)
        elif weekscounter % 2 == 1:
            print("Fill Composter A!")
            weekscounter += 1
            time.sleep(604800)
