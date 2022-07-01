"""
Functions for widly used outputs to save time and keep
formatting consistant
"""
def debug_var(var_text: str, var_value: any):
    """
    Returns text with the object value for easy and cleaner debugging output
    Example Output: '🪲 Debug: Search String -> a'
    """
    print (f"🪲 Debug: {var_text} -> {var_value}")
