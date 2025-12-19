"""
Log file analyzer tool.
"""

def parse_log_file(filename):
    error_count = 0
    warnings = []

    try:
        # Bug: File is opened but never explicitly closed if an error occurs 
        # later in the block (no 'with' context manager used).
        f = open(filename, 'r')
        
        lines = f.readlines()
        
        for line in lines:
            # Intended: find lines starting with specific codes
            if line.startswith("ERROR"):
                error_count += 1
            elif line.startswith("WARN"):
                # Bug: Appending the whole line including newline char might break formatting later
                warnings.append(line)
                
            # Bug: Potential mutable default argument logic if this function 
            # were more complex, but here: logic error in processing timestamps.
            # Assuming log format "LEVEL TIMESTAMP MSG".
            parts = line.split(" ")
            if len(parts) < 3:
                continue
                
        return {"errors": error_count, "warnings": warnings}
        
    except FileNotFoundError:
        print("Log file not found.")
        return None
    # Missing f.close() here implies resource leak
