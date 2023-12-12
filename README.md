CodeVita 2023 Python Solutions

Problem 1: Bubble Sort with Position Tracking

You are given two arrays: data and positions.
data contains elements to be sorted using bubble sort.
positions stores the initial positions of each element in data.
Your task is to sort data using bubble sort while ensuring the corresponding elements in positions reflect their new positions after each swap.
Example:

Input:

data: 5 3 7 12 8

positions: 12 45 65 34 22

Output:

data: 3 5 7 8 12

positions: 45 12 65 22 34

Problem 2: Recursive Digit Sum and Scientific Notation

You receive a number and a name as input.
Your task is to:
Sum the digits of the number recursively until you reach a single digit (the significant figure).
Convert the original number to scientific notation with the significant figure as the mantissa.
Determine the exponent based on the number of digits in the original number.
If the exponent is odd, select the character at the odd position in the name and append it to the scientific notation string.
Print the resulting string.
Example:

Input:

2 054785949 rajarajeswari

00.00000934749 bhuvaneswari

Output:

fiv.onee+sev@rjrjsai

nin.nine-six@hvnsai

Problem 4: Optimal Route with Goods and Tax

You are given a list of cities, their connections, goods available, and tax rates.
Your task is to find the optimal route for a traveler starting from a designated city and visiting all other cities while maximizing the collected goods and minimizing the total tax paid.
The decision-making criteria for choosing the next city are:
Maximize goods: Choose the city with the most goods available.
Minimize tax: If multiple cities offer the same amount of goods, prioritize the city with the lowest tax rate.
Lexicographic order: If goods and tax are equal between two cities, choose the one with the earlier name alphabetically.
Backtrack to the starting city after visiting all cities, paying any final tax due.
Example:

Input:

8 

hyderabad delhi 10 15

hyderabad pune 24 60

delhi kolkata 36 56

pune kasi 4 90

delhi chennai 16 100

kasi manali 41 45

chennai madhurai 8 20

Output:

hyderabad-pune-kasi-manali-kasi-pune-hyderabad-delhi-kolkata-delhi-chennai-madhurai-chennai-delhi-hyderabad

666

