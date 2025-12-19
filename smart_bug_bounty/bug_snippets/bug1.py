"""
INTENDED BEHAVIOR:
This function should calculate the ROI (Return on Investment).
If 'investments' sum to 0, it must handle the division gracefully (return 0.0),
instead of crashing.
"""

def calculate_roi(investments, returns):
    """
    Calculates Return on Investment (ROI) for a list of projects.
    """
    total_investment = sum(investments)
    total_return = sum(returns)
    
    # Bug: Logic Error / ZeroDivisionError
    # If the list 'investments' is empty or sums to 0, this crashes.
    # Intended: If investment is 0, ROI should be 0.0 (or handled gracefully).
    roi = (total_return - total_investment) / total_investment
    
    return roi * 100
