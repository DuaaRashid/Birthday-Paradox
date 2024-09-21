# Birthday Paradox Simulation

This project is a Python implementation that simulates the **Birthday Paradox**, which states that in a group of just 23 people, there's a better-than-even chance that at least two people will share the same birthday. The code generates random birthdays and calculates the probability of at least one shared birthday within a group for multiple iterations.

## Features
- **Random Birthday Generation**: Birthdays are randomly generated using lists of months and dates.
- **Duplicate Birthday Detection**: The program checks for matching birthdays in a list.
- **Probability Calculation**: After running the simulation 1000 times, the program calculates the probability of at least one birthday match.

## How It Works
1. The user inputs the number of people (`noOfTime`), which represents the size of the group.
2. The program generates random birthdays for each group and checks if any two people share the same birthday.
3. It runs the simulation 1000 times to gather data and computes the percentage of simulations where at least two people had matching birthdays.

## Code Structure
- **`getRandomBirthday(index)`**: Generates a list of random birthdays for a given group size.
- **`getMatch(bList)`**: Checks for duplicate birthdays in the list.
- **`main()`**: Runs the simulation 1000 times, counts the matches, and calculates the probability.

## Usage
To run the project, simply execute the Python script. You'll be prompted to input the number of people for which you want to simulate birthdays.

```bash
python birthday_paradox.py
```

Example input and output:
```
Enter a number: 23
Total no of matches: 508
Result: 50.8%
```

## Dependencies
- Python 3.x
- No external libraries are required (standard Python library `random` is used).

## License
This project is licensed under the MIT License.
