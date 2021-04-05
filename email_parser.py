import re


def email_parser(email):
    email_regex = re.compile(r'^([^\d][a-z\d\+]+)[^+]@([^\d][a-z\d]+)\.com', re.IGNORECASE)
    validating_email = email_regex.match(email)

    if not validating_email:
        return None
    splitting_email =  re.split('@',email)
    parsing_dict = {'username': splitting_email[0], 'domain': splitting_email[1]}
    print(validating_email)
    return parsing_dict
        