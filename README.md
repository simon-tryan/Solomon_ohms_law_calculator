# Solomon_ohms_law_calculator
A Python-based Ohm's Law and Electrical Power Calculator
 # Ohm's Law and Power Calculator

## What it does
This program allows the user to calculate Voltage, Current, Resistance, or Power using Ohm’s Law and the power formula. The user selects what they want to find, enters the known values, and gets the result with correct units. The program continues running until the user decides to quit.

## How to run it
Install Python 3, then run:

```bash
python ohms_law_calculator.py
 ==================================================
   OHM'S LAW & POWER CALCULATOR
==================================================

What do you want to calculate?
1. Voltage (V)
2. Current (I)
3. Resistance (R)
4. Power (P)
5. Quit
Enter your choice (1-5): 1
Enter Current (A): 2
Enter Resistance (Ω): 10

==================================================
Voltage = 20.00 V
Formula used: V = I × R → 2.0 × 10.0
==================================================

What do you want to calculate?
1. Voltage (V)
2. Current (I)
3. Resistance (R)
4. Power (P)
5. Quit
Enter your choice (1-5): 5

==================================================
           SESSION SUMMARY
==================================================
You performed 1 calculation(s):

1. Voltage = 20.00 V

Thank you for using the calculator!
==================================================
 My own twist
I added a Calculation History and Session Summary. Every successful calculation is stored. When the user quits, the program displays a summary of all the calculations performed during that session.
What I learned
I learned how to properly validate user input so the program does not crash when someone types a letter instead of a number. I also learned how to use a list to store previous results and display them neatly at the end.
Author
Solomon Philip ibukunoluwa
ND1 Mechatronics Engineering, YabaTech