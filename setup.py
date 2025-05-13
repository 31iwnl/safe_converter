from setuptools import setup, find_packages

setup(
    name='safe_converter',
    version='0.2.1',
    author='31',
    author_email='xhispeco2018@gmail.com',
    description='Универсальный конвертор',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/31iwnl/safe_converter',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
