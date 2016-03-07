from setuptools import setup, find_packages

setup(
    name='backend_test',
    description='Test task',
    long_description=open('README.md').read(),
    author='kryptex',
    url='https://github.com/thakryptex/backend_test/',
    # packages=['backend_test', 'url_parser'],
    include_package_data=True,
    install_requires=[
        "Django == 1.8",
    ],
    packages=find_packages(),
    zip_safe=False,
)
