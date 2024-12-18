# Text Analyzer Project

This project is a text analyzer that allows users to log in and select one of three predefined texts to analyze. The analysis includes word count, title case characters, upper case characters, lower case characters, numeric characters, and the sum of all numbers in the text. Additionally, it provides a text-based bar chart of word length occurrences.

## Features

- User authentication
- Selection of predefined texts
- Text analysis:
  - Word count
  - Title case characters
  - Upper case characters
  - Lower case characters
  - Numeric characters
  - Sum of all numbers
  - Word length occurrences graph (using stars)

## Installation

No additional libraries are required for this project.

## Usage

1. Run the script `index.py`.
2. Enter your username and password.
3. Select the text you want to analyze by entering the corresponding number.
4. View the analysis results and the word length occurrences graph.

## Example

```sh
$ python index.py
Enter username: bob
Enter password: 123

Hi bob, we have 3 texts to be analyzed.
1. This is the first text bruzz. It has some rizzy words and numbers like 1234.
2. Here is the second text (sigma). It also has words and numbers like 456.
3. Finally, this is the third text. It contains words and numbers like 789.

Enter the number of the text you want to analyze (1-3): 1

There are 11 words in the selected text.
There are 1 title case characters in the selected text.
There are 4 upper case characters in the selected text.
There are 38 lower case characters in the selected text.
There are 4 numeric characters in the selected text.
The sum of all the numbers is: 10

Word Length Occurrences:
1| * |1
2| ** |2
3| *** |3
4| **** |4