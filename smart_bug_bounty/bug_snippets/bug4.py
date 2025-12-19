import json

def load_config(filepath):
    """
    Intended: Load a JSON configuration file and return a dictionary.
    Should handle missing files gracefully by returning a default dict.
    """
    default_config = {"retries": 3, "timeout": 10}
    
    try:
        # Bug: Resource Leak. 'f' is opened but not closed if JSON parsing fails 
        # or if an exception is raised before close() (which is missing entirely).
        # Should use 'with open(...) as f:' context manager.
        f = open(filepath, 'r')
        data = f.read()
        config = json.loads(data)
        
        # Bug: Dictionary merge logic error. 
        # This overwrites user config with defaults instead of filling in missing keys.
        # Intended: user config overrides default.
        config.update(default_config) 
        
        return config
    except FileNotFoundError:
        return default_config
    except json.JSONDecodeError:
        return default_config
