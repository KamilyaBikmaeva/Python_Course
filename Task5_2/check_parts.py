import re


class InvalidEmailException(Exception):
    pass


class EmailChecker:
    email_reg = r'^([a-zA-Z0-9_\-\.]+|(?P<left_error>.*))@' \
                  r'([a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5}|(?P<right_error>.*))$'

    def check_email(self, string):
        pattern = re.compile(self.email_reg)
        result = pattern.match(string).groupdict()
        if result['left_error'] is not None and result['right_error'] is not None:
            raise InvalidEmailException(f"Error: Email is invalid ({result['left_error']}@{result['right_error']})")
        elif result['left_error'] is not None:
            raise InvalidEmailException(f"Error: {string}  Left part is invalid ({result['left_error']})")
        elif result['right_error'] is not None:
            raise InvalidEmailException(f"Error: {string}  Right part  is invalid ({result['right_error']})")
        else:
            return f'Valid email: {string}'


if __name__ == '__main__':
    check = EmailChecker()
    with open('emails.txt') as file:
        for line in file:
            try:
                print(check.check_email(line), end='')
            except Exception as exc:
                print(exc)
