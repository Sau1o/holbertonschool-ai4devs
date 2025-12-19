def calculate_grade_stats(grades):
    """
    Calculates statistics for a list of student grades.
    Intended: Return average of passing grades (> 60).
    """
    passing_grades = [g for g in grades if g > 60]
    
    total = sum(passing_grades)
    count = len(passing_grades)
    
    # Bug: ZeroDivisionError occurs if no grades are above 60.
    # Logic Error: If list is empty, it crashes instead of returning 0.
    return total / count

def find_top_student(students):
    """
    Intended: Return the name of the student with the highest score.
    students = [{'name': 'A', 'score': 90}, ...]
    """
    best_student = None
    highest_score = -1 # Initialized low to catch 0s
    
    for student in students:
        # Bug: If multiple students have the same high score, 
        # this logic keeps the first one found. Depending on reqs, 
        # might need to return a list or handle ties explicitly.
        # Also, strict > skips updating if score equals highest_score (stability).
        if student['score'] > highest_score:
            highest_score = student['score']
            best_student = student['name']
            
    return best_student
