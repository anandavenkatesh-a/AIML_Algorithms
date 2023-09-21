def dpll(cnf_formula, assignment={}):
    # Check for empty clauses
    if any(len(clause) == 0 for clause in cnf_formula):
        return False, {}  # Unsolvable
    
    # Check for all clauses being satisfied
    if all(any(lit in assignment and assignment[lit] for lit in clause) for clause in cnf_formula):
        return True, assignment  # Satisfiable

    # Unit propagation
    unit_clauses = [clause[0] for clause in cnf_formula if len(clause) == 1]
    for lit in unit_clauses:
        assignment[lit] = True

    # Pure literal elimination
    pure_literals = set()
    for clause in cnf_formula:
        for lit in clause:
            if -lit not in pure_literals:
                pure_literals.add(lit)
    for lit in pure_literals:
        assignment[lit] = True

    # Find an unassigned literal (naive approach)
    chosen_lit = None
    for clause in cnf_formula:
        for lit in clause:
            if lit not in assignment and -lit not in assignment:
                chosen_lit = lit
                break
        if chosen_lit is not None:
            break

    if chosen_lit is None:
        # If no unassigned literals are found, the assignment is complete
        return True, assignment

    # Branching: Try both assignments
    result, new_assignment = dpll(cnf_formula, {**assignment, chosen_lit: True})
    if result:
        return True, new_assignment

    result, new_assignment = dpll(cnf_formula, {**assignment, -chosen_lit: True})
    if result:
        return True, new_assignment

    # Backtrack
    return False, {}

# Example usage:
if __name__ == "__main__":
    cnf_formula = [[1, 2, -3], [-1, 3, 4], [-2, -4, 5]]
    is_satisfiable, assignment = dpll(cnf_formula)
    if is_satisfiable:
        print("Satisfiable. Assignment:", assignment)
    else:
        print("Unsatisfiable.")
