# 🧮 Professional CLI Calculator

A simple yet powerful command-line calculator built with Python featuring proper error handling, input validation, and calculation history.

## Features ✨

- **Basic Operations**: Addition, Subtraction, Multiplication, Division
- **Error Handling**: Zero division check, invalid input handling
- **Input Validation**: Proper validation for numeric inputs
- **Calculation History**: Track all calculations in current session
- **User-Friendly**: Clear prompts and error messages in English and Uzbek
- **Modular Code**: Each operation is a separate function
- **Infinite Loop**: Continue calculations until user exits

## Requirements 📋

- Python 3.6+
- No external dependencies

## Installation & Usage 🚀

### Run the calculator:
```bash
python calculator.py
```

### How to use:
1. Enter the first number
2. Choose an operation (+, -, *, /)
3. Enter the second number
4. View the result
5. Choose to continue or exit
6. See calculation history on exit

### Example:
```
🧮 Welcome to Professional CLI Calculator
==================================================

Enter first number: 10
📊 Available operations:
  + : qo'shish (Addition)
  - : ayirish (Subtraction)
  * : ko'paytirish (Multiplication)
  / : bo'lish (Division)

Select operation (+, -, *, /): +
Enter second number: 5

✅ Result: 10.0 + 5.0 = 15.0
```

## Code Structure 📁

```
01-python-calculator/
├── calculator.py      # Main calculator application
└── README.md         # This file
```

## Functions 🔧

- `add(x, y)` - Addition operation
- `subtract(x, y)` - Subtraction operation
- `multiply(x, y)` - Multiplication operation
- `divide(x, y)` - Division with zero check
- `get_valid_number(prompt)` - Input validation for numbers
- `get_operation()` - Input validation for operations
- `main()` - Main calculator loop

## Error Handling ⚠️

- **Invalid numbers**: User is prompted to enter valid numbers again
- **Division by zero**: Special error message displayed
- **Invalid operations**: User selects from valid options
- **Unexpected errors**: Caught and displayed gracefully

## Bonus Features 🎁

- ✅ Calculation history tracking
- ✅ User-friendly error messages
- ✅ Support for both English and Uzbek instructions

## Future Enhancements 💡

- Add more operations (power, modulo, square root)
- Save history to file
- Support for multiple calculations in one line
- Statistics (sum of all calculations, etc.)

## Author 👨‍💻

Created as part of 1-week GitHub pushing marathon

## License 📜

MIT License - Free to use and modify
