# Interactive Calculator

A command-line interactive calculator built in Python. It supports basic arithmetic operations (add, subtract, multiply, divide, power) and also provides an interactive shell mode.

## Features

- Addition, subtraction, multiplication, division, exponentiation
- Interactive shell mode for continuous calculations
- Clear error handling (e.g., division by zero)
- Simple, extensible code structure

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/interactive-calculator.git
   cd interactive-calculator
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install the package in editable mode (for development):

   ```bash
   pip install -e .
   ```

## Usage

After installation, you can use the `interactive-calculator` command:

```bash
# Show help
interactive-calculator --help

# Perform operations directly
interactive-calculator add 5 7
interactive-calculator subtract 10 3
interactive-calculator multiply 4 2.5
interactive-calculator divide 9 3
interactive-calculator power 2 8

# Enter interactive shell mode
interactive-calculator interactive
```

Inside the interactive shell, type operations (`add`, `subtract`, `multiply`, `divide`, `power`), provide numbers when prompted, or type `exit` to quit.

## Running Tests

We use `pytest` for unit testing. To run tests:

```bash
pytest
```

## Project Structure

```text
.
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── src
│   └── interactive_calculator
│       ├── __init__.py
│       ├── calculator.py
│       └── cli.py
└── tests
    ├── __init__.py
    └── test_calculator.py
```

## License

MIT License. Feel free to use and modify as you like.
