from setuptools import setup, find_packages

setup(
    name='apns_tool',
    version='1.0.1',
    packages=find_packages(),  # List of Python packages to include
    entry_points={
        'console_scripts': [
            'apns_tool=apns_tool.main:main',
        ],
    },
    install_requires=[
        'setuptools',
        'cryptography==38.0.4',
        'pyOpenSSL==21.0.0',
        'pip',
        'pycparser',
        'cffi',
        'pyperclip',
        'wheel'
    ]
    ,
)
