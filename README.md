# A GUI Hangman Game in Python

Welcome to this repository containing a hangman game built in Python. The game typically displays the number of attempts and guesses of a random word out of the <b>.txt</b> file (included in this repository) remaining before the hangman is fully drawn.

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributions](#contributions)
- [License](#license)

## Introduction

The following code contains a hangman game that features the basic rules of the hangman game with a little random word functionaity.

## Dependencies

To run this implementation, you need:

- Python 3.x
- The `random` module (usually included in Python standard library)
- The `tkinter` module (usually included in Python standard library)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/elcruzo/gui-hangman.git
   cd gui-hangman
   ```

2. Ensure you have Python 3.x installed. You can check by running:

   ```bash
   python3 --version
   ```

   If Python is not installed, you can download it from the official [Python website](https://www.python.org/downloads/).

## Usage

1. Navigate to the project directory containing the `index.py` file.

2. Open the `index.py` file in your preferred text editor or IDE.

3. Run the `index.py` script using the following command:

   ```bash
   python3 index.py
   ```

6. Upon execution, the script will present a pop-up displaying a text input field in which you type in the word and submit your guess.

7. If you run into any errors saying "FileNotFoundError: [Errno 2] No such file or directory", replace the path of the "wordlist.txt" (on the third line of the script) with it's relative path on your local machine.

## Example

Here's a brief example of how to run the code:

```bash
git clone https://github.com/elcruzo/gui-hangman.git
cd gui-hangman
python3 index.py
```

You will see a "Remaining attempts" note, displayed beneath the input field and upon each correct letter guess indicating the number of remaining guesses for that word until you guess the word correctly.

## Contributions

Contributions to this repository are welcome! If you have any improvements or feature suggestions, feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Have fun playing my Hangman Game! If you have any questions or run into issues, don't hesitate to ask for help.

