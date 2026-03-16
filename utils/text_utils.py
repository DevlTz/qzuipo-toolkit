def validate_input(text, key=None):
    if not text:
        raise ValueError("No input provided.")
    if key is None:
        raise ValueError("No key provided.")

def clean_text(text):
    return text.strip()

def print_result(operation, original, result):
    print(f"\n[{operation}]")
    print(f"  Original : {original}")
    print(f"  Result   : {result}")