import time
import argparse
import pyautogui

DEFAULT_DELAY = 0.75
STARTUP_DELAY = 5


def press(key: str) -> None:
    """Press a key.
    Using vanilla `pyautogui.press()` will not register the keystroke
    because GT requires you hold a keypress for a small duration."""
    
    with pyautogui.hold(key):
        time.sleep(0.2)
    time.sleep(DEFAULT_DELAY)  # delay after any press


def hold(key: str, duration: float) -> None:
    """Hold a key for some duration."""
    with pyautogui.hold(key):
        time.sleep(duration)


def sleep(seconds: float):
    time.sleep(seconds)


def focus_window():
    """Focus the window by clicking on the center of the primary screen."""
    # Click center of screen to focus remote play window.
    # You can reposition and resize remote play window, just
    # make sure you update where you click. I don't know how to
    # use pyautogui in headless mode.
    print(
        "Using startup delay of "
        + str(STARTUP_DELAY)
        + " seconds. Switch to PS Remote Play window now"
    )
    time.sleep(STARTUP_DELAY)


def start_exploit(section):
    """Begin a cycle"""

    print(" [-] Entering Cafe.")
    press("enter")
    sleep(5)
    press("left")
    press("enter")
    press("down")
    press("right")
    press("enter")
    press("up")

    if section == "ROTARY":
        press("right")
        press("right")

        # Inside Rotary Engine

    press("enter")
    press("enter")
    sleep(1)  # Exploiting
    press("escape")
    press("escape")
    press("escape")
    sleep(5)

    # Back to map to open ticket
    press("right")
    press("enter")
    sleep(5)
    press("right")
    press("right")
    press("right")
    press("enter")
    press("enter")
    press("enter")
    print(" [-] Opening ticket.")
    sleep(16)

    # Accepting any kind of ticket, avoids using image detection
    press("enter")
    sleep(10)
    press("enter")
    sleep(5)
    press("enter")
    press("enter")

    print(" [-] Accepting ticket.")
    press("enter")  # accept ticket

    # Back out of tickets
    print(" [-] Going back to map.")
    press("escape")
    press("escape")
    sleep(4)
    press("left")  # Place cursor on Menu to start over


if __name__ == "__main__":
    cycles = 0
    focus_window()
    while True:
        start_exploit("")
        start_exploit("ROTARY")
        cycles += 1
        print(" [+] Cycles completed: " + str(cycles))
