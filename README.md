# Wordle Solver

The Wordle Solver is a program that helps users solve the popular word guessing game, Wordle. It uses a list of English words to generate all legible 5-letter words, and allows users to enter a combination of letters and symbols that represent their guess and the position of correct letters in that guess. The program then filters the list of words to find all possible matches based on the user's guess and symbols.

# Getting Started

To use the Wordle Solver, you can download or clone the repository and run the program using a Python interpreter. The program requires the NLTK library, which you can install using pip or conda.

pip install nltk

Once you have installed NLTK, you can run the program by running the following command:

python wordle_solver.py


# How to Use

When you run the program, you will be prompted to enter a 5-letter word and a combination of letters and symbols that represent your guess and the position of correct letters in that guess. The symbols you can use are:

_ for an unknown letter

. for a letter that is not in the correct position

X for a letter that is in the correct position

For example, if your guess is "READY" and the correct letters are "R" and "E" in the first and third positions, respectively, you can enter the following symbols:

__RE__
The program will then filter the list of legible words to find all possible matches based on your guess and symbols. It will display the list of possible matches, and prompt you to enter another guess.

# Contributing

If you would like to contribute to the Wordle Solver, you can fork the repository and make your changes. You can then create a pull request to have your changes merged into the main branch.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments

The Wordle Solver uses the NLTK library and the English dictionary corpus from the Natural Language Toolkit, which is licensed under the Apache License, Version 2.0.
