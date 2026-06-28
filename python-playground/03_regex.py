# Regular expression
import re
text = "Mere numbers: 0300-1234567, 042-1234567, 021-1234567"
result = re.search(r"\d{4}-\d{7}", text)
if result:
    print("Found", result.group())

found_number = re.findall(r"\d{3,4}-\d{7}", text)
print("Found Numbers:", found_number)

text = "Call me at 0300-1234567"
new_text = re.sub(r"\d{4}-\d{7}", "XXX-XXXXXXX", text)
print(new_text)

text = "PK12345"
result = re.match(r"[A-Z]{2}\d{5}", text)
print(result.group())  # PK12345

def validateEmail(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    return False
print(validateEmail("ali@gmail.com"))
print(validateEmail("ali@.com"))

def validate_pk_phone(number):
    patterns = [
        r"^03\d{9}$",
        r"^03\d{2}-\d{7}$",
        r"^\+92\d{10}$"
    ]
    for pattern in patterns:
        if(re.match(pattern, number)):
            return True
        return False

print(validate_pk_phone("03001234567"))     # True
print(validate_pk_phone("0300-1234567"))    # True
print(validate_pk_phone("+923001234567"))   # True
