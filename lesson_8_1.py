import re

RE_EMAIL = re.compile(r"^([\w.'-]+)@([\w-]+\.\w+)")


def email_parse(email_address):
    is_email = re.match(RE_EMAIL, email_address)
    if is_email:
        user_name, domain = is_email.groups()
        return {'username': user_name, 'domain': domain}
    else:
        raise ValueError(f'wrong email: {email_address}')


try:
    print(email_parse(input('Enter an email: ')))
except ValueError as e:
    print(e)
