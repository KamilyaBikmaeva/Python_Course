import re


def check_email(email):
    email_reg = r'^[a-zA-Z0-9_\-\.]*@[a-zA-Z0-9_\-\.]*\.[a-zA-Z]{2,3}$'
    if re.search(email_reg, email):
        print("Valid Email: ", email)

    else:
        print("Invalid Email: ", email)


if __name__ == '__main__':
    email1 = "ankitrai_326@gmail.com"
    email2 = "my.oWnsiTe@our_eaRth.org"
    email3 = "ankitrai326.com"
    email4 = "freoij.ferf.er12r23@hasid.com"
    email5 =" er!wed.fer@yandex.ru"
    check_email(email1)
    check_email(email2)
    check_email(email3)
    check_email(email4)
    check_email(email5)