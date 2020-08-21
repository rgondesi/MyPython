__all__ = ["extract_upper"]

def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

print(f"__name__ in helpers.py: {__name__}")
print("HELLO FROM HELPERS")