from django.core.exceptions import ValidationError


def validate_phone(phone_str):
    phone_error = False
    if len(phone_str) == 10 or len(phone_str) == 11:
        c = [i for i in phone_str if i.isdecimal()]
        if c[0] == '8' and len(c) == 11:
            c = ['+', '7'] + c[1:]
        elif c[0] == '9' and len(c) == 10:
            c = ['+', '7'] + c
        elif c[0] == '7' and len(c) == 11:
            c = ['+', '7'] + c[1:]
        else:
            phone_error = True
        if phone_error:
            raise ValidationError('Проверьте номер телефона')
        else:
            # qwe = c[:2] + ['('] + c[2: 5] + [')'] + c[5: 8] + ['-'] + c[8:10] + ['-'] + c[10:]
            return ''.join(c)
    else:
        raise ValidationError('Проверьте длинну номера телефона')