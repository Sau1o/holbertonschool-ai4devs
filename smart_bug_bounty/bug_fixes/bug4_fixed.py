"""
FIX APPLIED:
1. Used 'with open' context manager to ensure file closure.
2. Corrected dictionary update logic (System defaults copied first, then User overrides).
"""
import json

def merge_configs(user_config_path):
    system_defaults = {"theme": "light", "notifications": True}
    
    try:
        # Fix 1: Context manager for resource safety
        with open(user_config_path, 'r') as f:
            user_data = json.load(f)
        
        # Fix 2: Correct merge order (User overrides System)
        final_config = system_defaults.copy()
        final_config.update(user_data)
        
        return final_config
        
    except (FileNotFoundError, json.JSONDecodeError):
        return system_defaults
