import setuptools

# Take README.md as long description for the package
with open('README.md', 'r') as fh:
    long_description: str = fh.read()

# Setup Wanalyzer package
setuptools.setup(
    name='wanalyzer',
    version='1.0',
    author='C911N',
    description='WhatsApp exported chats parsing and filtering tool (python module)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/C911N/Wanalyzer',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
