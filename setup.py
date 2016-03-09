from setuptools import setup, find_packages

setup(
    name='backend_test',
    description='Test task',
    long_description=open('README.md').read(),
    author='kryptex',
    url='https://github.com/thakryptex/backend_test/',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django == 1.8",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
