import sys

from setuptools import setup

install_requires = []

if sys.version_info < (2, 7):
    raise DeprecationWarning('Python 2.6 and older are no longer supported by PAY.JP. ')

install_requires.append('requests >= 2.7.0, < 3.0.0')

setup(
    name="payjp",
    version="2.0.0",
    description='PAY.JP python bindings',
    author="PAY.JP",
    author_email='support@pay.jp',
    packages=['payjp', 'payjp.test'],
    url='https://github.com/payjp/payjp-python',
    install_requires=install_requires,
    tests_require=[
        'mock >= 1.3.0'
    ],
    test_suite='payjp.test.all',
)
