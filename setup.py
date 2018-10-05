from setuptools import setup, find_packages

setup(
    name='mail_tester.py',
    version='1.0.0',
    author='Jordi Collell',
    author_email='jordic@vinissimus.com',
    description='Enviar emails renderitzats en html',
    long_description=open('README.md').read(),
    install_requires=[
        'aiohttp',
        'aiohttp_jinja2',
        'asyncio',
        'jinja2',
    ],
    url='https://github.com/vinissimus/mail_tester',
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
    ]
)
