"""
Module for processing student grades.
"""

def calculate_average(grades):
    total = 0
    count = 0
    
    # Intended to sum only passing grades (> 60)
    for grade in grades:
        if grade > 60:
            total += grade
            count += 1
            
    # Potential ZeroDivisionError if no grades > 60
    # Also, logic might be flawed if we wanted average of ALL grades, 
    # but description says "average of passing grades".
    return total / count

def get_best_student(student_data):
    """
    student_data is a list of dicts: {'name': str, 'score': int}
    """
    best_student = None
    highest_score = 0
    
    for student in student_data:
        # Bug: Logic error. If all scores are negative (unlikely but possible in edge cases)
        # or if highest_score starts at 0, we might miss data.
        # Also, using >= might change the winner if there's a tie (stability issue).
        if student['score'] > highest_score:
            highest_score = student['score']
            best_student = student['name']
            
    return best_student

# Example usage
data = [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 92}]
print(get_best_student(data))
