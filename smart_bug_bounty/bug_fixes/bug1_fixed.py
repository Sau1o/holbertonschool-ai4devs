"""
FIX APPLIED:
Added a check for zero investment to prevent ZeroDivisionError.
"""

def calculate_roi(investments, returns):
    total_investment = sum(investments)
    total_return = sum(returns)
    
    # Fix: Handle zero investment gracefully
    if total_investment == 0:
        return 0.0
        
    roi = (total_return - total_investment) / total_investment
    
    return roi * 100
