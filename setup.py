from setuptools import setup, find_packages

from எண்ணிக்கை import உரைக்கு as உ

with open('تقدیر/تبدیل.txt', 'r', encoding='utf8') as تبدیل_کی_دستاویز:
    تبدیل = உ(تبدیل_کی_دستاویز.read().strip(), 'latin', 'ار')

setup(
    name='taqdir',
    version=تبدیل,
    packages=find_packages(),
    url='https://taqdir.readthedocs.io',
    download_url='https://github.com/julienmalard/taqdir',
    license='GNU 3',
    author='ژولئیں ژاں ملاغ (Julien Jean Malard)',
    author_email='julien.malard@mail.mcgill.ca',
    description='',
    long_description='',
    install_requires=['numpy', 'pandas', 'ennikkai', 'selenium', 'pcse', 'chardet', 'tradssat', 'requests'],
    setup_requires=['ennikkai'],
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    package_data={
        '': ['**/*.txt'],
        'تقدیر': ['*.txt']
    },
)
