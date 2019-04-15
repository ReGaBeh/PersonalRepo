import pyttsx3  # Importing necessary modules
import argparse


# This function uses pyttsx3 to read out the input
def read(input, rate, volume):
    if not rate:    # if statements to assign rate/volume default values
        rate = 100  # when none ar given by checking if rate/volume have
    if not volume:  # values, if not then the defaults are assigned
        volume = 1

    engine = pyttsx3.init()  # Initialising the speech synthesizer

    engine.setProperty('rate', rate)      # Setting the rate and volume properties
    engine.setProperty('volume', volume)  # with the rate and volume vars

    engine.say(str(input))  # Queueing the input string
    engine.runAndWait()  # 'Reading' out the queue


if __name__ == '__main__':  # Only runs if the file is not run from import
    parser = argparse.ArgumentParser()  # Initialising the parser

    # Creating the arguments input, rate, and volume. Only input is required and
    # is a positional argument
    parser.add_argument('input', help='Defines what will be read out by the tts')
    parser.add_argument(
        '--rate', help='Defines the speed at which input will be read (must be int, 100=100%)')
    parser.add_argument('--volume', help='Defines volume, must be float value between 0 and 1')

    args = parser.parse_args()  # Parsing the argumnets given

    # Printing the entered arguments
    print(f'\n{args.input}\n rate, volume = {args.rate} {args.volume}')
    read(args.input, args.rate, args.volume)  # Calling the read() function
