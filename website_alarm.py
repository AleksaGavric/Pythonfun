import random
import time
import webbrowser


def set_alarm():
    """Prompt the user to enter the alarm time and validate the format."""
    alarm_time = input("Enter alarm time (format HH:MM): ")

    while not validate_time_format(alarm_time):
        alarm_time = input("Please enter alarm time in the correct format (HH:MM): ")

    print(
        "Alarm set. Please keep this window running if the alarm hasn't gone off yet."
    )

    return alarm_time


def validate_time_format(time_str):
    """Validate the format of the alarm time."""
    try:
        time.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


def run_alarm(alarm_time):
    """Continuously check the current time and open a random link if it matches the alarm time."""
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            webbrowser.open("https://google.com")
            break


def main():
    """Main function to set the alarm and run the alarm program."""
    alarm_time = set_alarm()
    run_alarm(alarm_time)


if __name__ == "__main__":
    main()
