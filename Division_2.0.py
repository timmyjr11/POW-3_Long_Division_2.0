'''
Authors: Timothy Wright and Hannah Veveiros
Date: 9/12/2022

Program that solves the Pre-calc POW#3 Long Divison

NOTE: As stated from "Eclipse Public License - v 2.0" 
anyone that uses this program user MUST cite the link from which they obtained the program.
The purpose is to discourage cheating and only use this as a resource to find your own solution to the problem
The link is found here: https://github.com/timmyjr11/POW-3_Long_Division_2.0/blob/master/Division_2.0.py
'''

# For loop that increments the divisor
for divisor in range(100, 1000):
    # For that increments the dividend
    for dividend in range(10000000, 100000000):
        # Creates the answer
        answer = dividend / divisor

        # If answer is above 100,000 then restart and increment the dividend by one
        if answer > 100000:
            break

        # Casts the dividend and answer to string to manipulate
        dividend = str(dividend)
        answer = str(answer)

        # Collects the first four values in the dividend then
        # subtracts by the divisor times the first value in the answer
        step_one = int(dividend[0:4]) - divisor * int(answer[0])

        # Part one converts the first step into a string then concatenates the next two values in the dividend
        # Part two converts part one back into an int then
        # subtracts the divisor times the third value in the answer
        step_two_part_one = str(step_one) + dividend[4] + dividend[5]
        step_two_part_two = int(step_two_part_one) - divisor * int(answer[2])

        # Part one converts the first step into a string then concatenates the next two values in the dividend
        # Part two converts part one back into an int then
        # subtracts the divisor times the fifth value in the answer
        step_three_part_one = str(step_two_part_two) + dividend[6] + dividend[7]
        step_three_part_two = int(step_three_part_one) - divisor * int(answer[4])

        # If the third value in answer = 8, if there is no remainder,
        # if the length of the number that subtracts in step one = 4,
        # if the answer of step one has the length of 2, if the answer of step two has the length of 2,
        # and if the answer to step 3 has the length of 1, then the answer is found
        if int(answer[2]) == 8 and int(dividend) % divisor == 0 and len(str(divisor * int(answer[0]))) == 4 and \
                len(str(step_one)) == 2 and len(str(step_two_part_two)) == 2 and len(str(step_three_part_two)) == 1:
            # Prints the Divisor, Dividend, Answer, all intermediate steps, and then exits
            print(f"Found: Divisor = {divisor}, Dividend = {dividend}, Answer = {answer}")
            print(f"Step One = {step_one}, Step two = {step_two_part_two}, Step three = {step_three_part_two}")
            exit(0)
        # Else print then increment the loop by one and try again
        else:
            print(f"Divisor = {divisor}, Dividend = {dividend}, Answer = {answer}")
