from setuptools import setup, find_packages

setup(
    name='praxis-mlops',
    version='0.1.0',
    author='Builders of Build Club',
    author_email='info@buildclub.com.au',
    description='A utility library for MLOps with virtual environment management and integrated logging.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/buildclub/praxis-mlops',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='mlops, mlflow, wandb, logging, environment',
    install_requires=[
        'numpy',
        'pandas',
        'requests',
        'python-dotenv',
        'PyYAML',
        'logging',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'praxis-mlops=praxis_mlops.cli:main',
        ],
    },
)
