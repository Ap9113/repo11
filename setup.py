from setuptools import setup, find_packages

setup(
    name="interactive-calculator",
    version="0.1.0",
    description="A simple CLI interactive calculator.",
    author="Your Name",
    author_email="you@example.com",
    url="https://github.com/yourusername/interactive-calculator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click>=8.0.0"
    ],
    entry_points={
        "console_scripts": [
            "interactive-calculator=interactive_calculator.cli:cli"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
