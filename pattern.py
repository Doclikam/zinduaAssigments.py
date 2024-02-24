import re




string="Please contact jullieta99@gmail.com for assistance. Phone: (254) 257-8000 or (254) 297-9983"
def extract_phone_numbers(string):
    pattern=r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    extract_phone_numbers=re.search(pattern,string)
    return extract_phone_numbers

def extract_email_addresses(string):
    pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,8}"
    extract_email_addresses=re.search(pattern,string)
    return extract_email_addresses
def replace_email_addresses(string, replacement):
    replacement=re.sub(pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,8}",
    repl="REPLACED",
    string=string)
    return replacement



 
print(extract_phone_numbers(string))
print(extract_email_addresses(string))
print(replace_email_addresses(string, "REPLACED"))







