from setuptools import setup, find_packages

setup(
    name="heart_disease_prediction",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "pywebio",
        "pickle-mixin",
    ],
    entry_points={
        'console_scripts': [
            'heart_disease_prediction=your_script_name:main',
        ],
    },
    description="A heart disease prediction model with a web interface using PyWebIO",
    author="Ayush Singh",
    author_email="ayushmeeta12@gmail.com",
    url="https://github.com/ayushsingh2278/Heart-Disease-Detection",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
