# The Cryptic Password
# Satisfiability and the P vs. NP problem


'''A secret agency needs to crack a cryptic password to gain access to a highly classified document. The password consists of four characters, each character being either a lowercase letter or a digit. However, the password is encrypted in such a way that the following rules must be satisfied:

    Rule 1: The first and last characters of the password must be the same.
    Rule 2: The second character must be a digit.
    Rule 3: If the third character is a digit, then the fourth character must be a lowercase letter.

The agency wants to determine if there exists a valid password that satisfies these rules. To solve this problem, we can encode it as a SAT problem.

First, let's assign variables to represent the properties of each character in the password. We'll use the following encoding scheme:

    Variables x1, x2, x3, and x4 represent the four characters of the password, respectively.
    Variables d1 and d2 represent whether the second character is a digit or not.
    Variables l3 and l4 represent whether the third and fourth characters are lowercase letters or not.

Now, let's write the clauses that capture the rules of the problem:

    The first and last characters must be the same:
        Clause 1: (!x1 v x4) AND (x1 v !x4)
    The second character must be a digit:
        Clause 2: (!x2 v d1) AND (x2 v !d1)
    If the third character is a digit, the fourth character must be a lowercase letter:
        Clause 3: (!x3 v !d2 v l4)

We can also add additional clauses to ensure that each character is either a lowercase letter or a digit:

    Clause 4: (x1 v !d1 v !l3)
    Clause 5: (x2 v d2)
    Clause 6: (x3 v !l3)
    Clause 7: (x4 v !l4)

To solve this SAT problem, we can use a SAT solver library in Python such as pycosat  to check if a valid password exists:'''


import pycosat

def solve_password():
    clauses = [
        [-1, 4], [1, -4],    # Clause 1
        [-2, 5], [2, -5],    # Clause 2
        [-3, -6, 7],         # Clause 3
        [1, -5, -6],         # Clause 4
        [2, 6],              # Clause 5
        [3, -7],             # Clause 6
        [4, -7]              # Clause 7
    ]
    
    solution = pycosat.solve(clauses)
    if solution != "UNSAT":
        password = ""
        for i in range(4):
            if solution[i] > 0:
                password += chr(ord("a") + i)
            else:
                password += str(abs(solution[i]))
        return password
    else:
        return "No valid password exists."

password = solve_password()
print("The valid password is:", password)


'''In this code, we define the clauses as a list of lists, where each inner list represents a clause. The negative sign (-) represents negation, and positive numbers represent variables. We then use the pycosat.solve() function to solve the SAT problem defined by the clauses. If a solution exists (i.e., a valid password is found), we decode the solution to obtain the characters of the password. The characters are determined based on whether the corresponding variables are positive or negative.

Finally, we print the valid password if one is found, or a message indicating that no valid password exists.

Note: You'll need to install the pycosat library to run this code. You can install it by running pip install pycosat.

When you run the code, it will attempt to find a valid password that satisfies the given rules. If such a password exists, it will be displayed as the output. Otherwise, the code will indicate that no valid password exists.

'''