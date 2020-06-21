import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='simple_tracker',  # Replace with your own username
    version='0.1.0',
    author='Brennen Herbruck',
    author_email='brennen.hrbruck@gmail.com',
    description='A small example package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bherbruck/simple_tracker',
    packages=['simple_tracker'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
