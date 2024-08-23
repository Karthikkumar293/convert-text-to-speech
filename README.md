# Karthik Text to Speech

This script converts text input into speech using the `pyttsx3` library in Python.

## Prerequisites

- Python 3.x must be installed on your system.

## Installation

1. Install the `pyttsx3` library by running the following command in your terminal:

    ```bash
    pip install pyttsx3
    ```

## Usage

1. Create a Python script file named `text_to_speech.py` and add the following code:

    ```python
    import pyttsx3

    print("WELCOME TO KARTHIK TEXT TO SPEECH")
    text = input("Enter your text: ")
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()
    ```

2. Run the Python script by executing the following command in your terminal:

    ```bash
    python text_to_speech.py
    ```

3. After running the script, enter the text you want to convert to speech when prompted. The script will then read the text aloud.

## Notes

- You can adjust the speech rate by modifying the `rate` property in the Python script.
- Ensure your system has speakers or headphones to hear the speech output.

---

By following these instructions, you can convert text to speech using Python.
