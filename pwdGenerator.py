import random

def generate():
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@$%^#&*()_+?><|'
    pwdlen = 8
    return ''.join(random.sample(s, pwdlen))


print(generate())

