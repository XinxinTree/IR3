from setuptools import setup, find_packages

setup(
    name='IR3',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            # You can define command-line scripts here if necessary
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for processing DNAzyme substrates',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/IR3',  # Update with your actual URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
