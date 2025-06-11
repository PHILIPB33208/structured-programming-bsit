## differences between Assigning and Declaring a variable giving practical examples of each
"assigning a variable means storing a specific value into a named memory location (the variables) so that it can be used later in the program"
## example
input_score = int(input("Enter your test score:"))
score =input_score # reassignment
if score >=50:
    print("you passed")
else:
    print("you failed.")
    ## declaring a variable
    "declaring a variable means introducing it into the program so it can hold values during execution"
    ## examples
    age =25
    salary =200000
    grade = 'A'
    