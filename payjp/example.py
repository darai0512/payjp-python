# coding: utf-8

from payjp import Payjp

payjp = Payjp('sk_test_c62fade9d045b54cd76d7036')

print('Attempting charge...')

resp = payjp.charges.create({
    'amount': 10,
    'currency': 'jpy',
    'card': {
        'number': '4242424242424242',
        'exp_month': 12,
        'exp_year': 2018
    },
    'description': 'a TIROL Choco'
})

print(resp)
print(('Success: %r') % (resp, ))
