"""NP is the set of all problems that are solvable in polynomial time by a “nondeterministic Turing Machine” (NTM). Very roughly, that’s a TM that, when faced with a choice, can create parallel timelines and try a different choice in each timeline. This is equivalent to the set of all problems that can be verified in polynomial time, which is the definition most non-CS people learn.1

All problems in P are also in NP. It’s an open question whether NP problems can’t be solved in deterministic polynomial time, aka the P=NP problem. If P!=NP, then some NP problems are harder than others. There’s also an upper bound to “how hard” an NP problem can be. This set of “most difficult” NP programs (which again, might just be P) form the NP-complete complexity class. There are also problems that can’t even be verified in polynomial time. NP-hard is the set of all problems that are NP-complete or harder.2 People often conflate NP-complete and NP-hard.

The quintessential NP-complete problem is Boolean SATisfiability , or SAT. A SAT problem consists of a set of boolean variables and a set of clauses, like this:

A | C
!A | D | !E
B | !D | E | F
…

The goal is to find an assignment of variables that makes every clause true. Checking an answer is obviously in P: just plug the proposed assignments into the clauses and see if they all pass. We don’t have a polynomial time algorithm for finding assignments, though, and mathematicians are confident there isn’t one. It’s NP-complete. By the Cook-Levin Theorem, any other NP-complete problem can be converted into a SAT problem, and in fact “convert NP-complete problem to SAT” is in P.


What follows is some Python code focusing on the SAT problem and its verification. Since the SAT problem is an NP-complete problem, we won't be able to find a polynomial-time algorithm to solve it, but we can still demonstrate the verification process.

To start, let's define a simple SAT problem with a few boolean variables and clauses. We'll represent the SAT problem as a list of clauses, where each clause is a set of literals. A literal can be a boolean variable or its negation. 
"""


sat_problem = [{1, 3}, {-1, 4, -5}, {2, -4, 5, 6}]

# Clause 1: Variables 1 and 3 must be true.
# Clause 2: Variable 1 must be false, and variables 4 and 5 must be true.
# Clause 3: Variable 2 must be true, and variables 4, 5, and 6 must be true.


# To verify a given assignment of variables for the SAT problem, we need to check if all the clauses evaluate to True.


def verify_assignment(sat_problem, assignment):
    for clause in sat_problem:
        clause_result = False
        for literal in clause:
            variable, negation = abs(literal), literal < 0
            if (negation and not assignment[variable]) or (not negation and assignment[variable]):
                clause_result = True
                break
        if not clause_result:
            return False
    return True


# The verify_assignment function takes the SAT problem and an assignment dictionary as input. The assignment dictionary maps variable indices to their assigned boolean values (True or False). The function iterates over each clause and checks if at least one literal in the clause evaluates to True based on the assignment. If any clause evaluates to False, it means the assignment is invalid, and the function returns False. Otherwise, if all clauses evaluate to True, the function returns True.


assignment = {1: False, 2: True, 3: True, 4: True, 5: True, 6: True}
is_valid = verify_assignment(sat_problem, assignment)
print("Assignment is valid:", is_valid)


In this example, we assume that variable 1 is False, variables 2, 3, 4, 5, and 6 are True. The verify_assignment function will check if this assignment satisfies all the clauses in the SAT problem. The output will indicate whether the assignment is valid or not.