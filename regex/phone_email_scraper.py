#! python3

import re, pyperclip

# CREATE REGEX FOR PHONE
phoneRegex = re.compile(r"""

# 123-123-1234 or 123-1234 or (123) 123-1234 
(
((\d\d\d) | (\(\d\d\d\)))? # area code (optional)
(\s | -) # first separator
\d\d\d # first 3 digits
- # separator
\d\d\d\d # last 4 digits
(((ext(\.)?\s) |x) # extension word-part (optional)
(\d{2,5}))? # extension number-part (optional)
)
""", re.VERBOSE)

# CREATE REGEX FOR EMAIL

emailRegex = re.compile(r"""

[a-zA-Z0-9_.+]+   # name
@ # at sym
[a-zA-Z0-9_.+]+ # domain name
""", re.VERBOSE)
# GET TEXT FROM CLIPBOARD

text = pyperclip.paste()
# EXTRACT EMAIL + PHONE

extrated_phone = phoneRegex.findall(text)
extrated_email = emailRegex.findall(text)

all_phone_numbers = []
for phone_number in extrated_phone:
    all_phone_numbers.append(phone_number[0])


print(all_phone_numbers)
print(extrated_email)

# COPY EXTRACTED INFO TO CLIPBOARD

results = "\n".join(all_phone_numbers) + "\n".join(extrated_email)
pyperclip.copy(results)