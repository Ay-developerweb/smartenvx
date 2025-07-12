# smartenv/utils.py

def str_to_bool(value):
    return str(value).strip().lower() in ['1', 'true', 'yes', 'on']
