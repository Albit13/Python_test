def is_valid_email(email):
    if email.count('@') != 1 or email.count('.') != 1:
        return False
    if email.index('@') > email.index('.'):
        return False
    if email.startswith('@') or email.endswith('.'):
        return False
    return True

email = input("Enter your e-mail: ")
if is_valid_email(email):
    print("Email is valid")
else:
    print("Email is not valid")


# aaa@bbb.ccc
# aaa@bbb@ccc.com
# aaa.bbb@ccc.com
# @bbb.ccc
# aaa@bbb.ccc.
# aa.a@bbbccc