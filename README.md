#excusegen 
what is it - generates random excuses for different situations 

## Installation

Clone the repository and install dependencies using pipenv:

    git clone https://github.com/<your-username>/excusegen.git
    cd excusegen
    pipenv install

Enter the virtual environment:

    pipenv shell

Install the package locally:

    pip install .

## Usage

Run the package from the command line:

    python3 -m excusegen

Or use it in Python code:

    from excusegen import generate

    print(generate())              # returns a general excuse
    print(generate("deadline"))    # returns a deadline-related excuse
    print(generate("meeting"))     # returns a meeting-related excuse

Available categories:
- general
- deadline
- meeting
- class

## Testing

Run tests using pytest:

    pipenv run pytest

Expected output:

    ==================== 1 passed in 0.00s ====================
    