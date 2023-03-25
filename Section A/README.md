# Code Review

1. Create a ecursive function that reverses a string.

Good work with the reverse_string function, the question is understood. There are just some minor fixes for improvement and correctness.

My comments are:
- Be mindful of the function name when doing function calls, they must match (reverse_string != reverseString). Check line 26. Additionally, the standard naming convention would be reverseString (the action followed by the object).
- The function should work with user input and not hard coded as in line 6. 
- Avoid unnecessary print statements as in line 21. 
- Pay attention to syntax, are you closing your brackets where necessary? Hint: where does the reverse_string end?

2. Create a recursive function that, given a number n, prints out the first n Fibonacci numbers (Fibonacci numbers are a sequence where each number is the sum of the previous two - 0 1 1 2 3 5 8...).

The concept of Fibonacci numbers is understood.

My comments are:
- Give functions meaningful names, see line 26.
- The function should work with user input and not hard coded as in line 30. 
- Remember to indent your code, it helps with readability. For example, indentation on line 36 would be helpful.
- Recall the definition of a recursive function, is this function recursive?
- The function must print out the first n Fibonacci numbers, think of how you can store the calculations as you recursively call the function.



