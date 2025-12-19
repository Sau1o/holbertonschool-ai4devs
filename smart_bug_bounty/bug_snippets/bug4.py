import json

def merge_configs(user_config_path):
    """
    Merges user configuration with system defaults.
    """
    system_defaults = {"theme": "light", "notifications": True, "version": 1}
    
    try:
        # Bug 1: Resource Leak.
        # File is opened without a context manager ('with' statement).
        # If json.load fails, the file handle 'f' remains open indefinitely.
        f = open(user_config_path, 'r')
        user_data = json.load(f)
        
        # Bug 2: Dictionary Update Logic Error.
        # Intended: User settings should override defaults (Priority: User > System).
        # Actual: System defaults are updating (overwriting) the user data.
        user_data.update(system_defaults)
        
        return user_data
        
    except FileNotFoundError:
        return system_defaults
