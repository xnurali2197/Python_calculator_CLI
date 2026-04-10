"""
Professional CLI Calculator
A simple yet powerful command-line calculator with proper error handling
"""

def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


def multiply(x, y):
    """Multiply two numbers"""
    return x * y


def divide(x, y):
    """Divide two numbers with zero check"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y


def get_valid_number(prompt):
    """Get and validate number input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Error: Please enter a valid number")


def get_operation():
    """Get and validate operation choice"""
    operations = {
        '+': ('qo\'shish', add),
        '-': ('ayirish', subtract),
        '*': ('ko\'paytirish', multiply),
        '/': ('bo\'lish', divide)
    }
    
    print("\n📊 Available operations:")
    print("  + : qo'shish (Addition)")
    print("  - : ayirish (Subtraction)")
    print("  * : ko'paytirish (Multiplication)")
    print("  / : bo'lish (Division)")
    
    while True:
        choice = input("\nSelect operation (+, -, *, /): ").strip()
        if choice in operations:
            return operations[choice]
        print("❌ Invalid operation. Please try again.")


def main():
    """Main calculator loop"""
    print("=" * 50)
    print("🧮 Welcome to Professional CLI Calculator")
    print("=" * 50)
    
    history = []
    
    while True:
        try:
            # Get inputs
            num1 = get_valid_number("\nEnter first number: ")
            operation_name, operation_func = get_operation()
            num2 = get_valid_number("Enter second number: ")
            
            # Calculate
            result = operation_func(num1, num2)
            
            # Display result
            print(f"\n✅ Result: {num1} {list(operation_func.__doc__)[0]} {num2} = {result}")
            
            # Store in history
            history.append(f"{num1} {operation_name} {num2} = {result}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            continue
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            continue
        
        # Ask to continue
        while True:
            choice = input("\nDo you want to continue? (yes/no): ").strip().lower()
            if choice in ['yes', 'y', 'ha', 'h']:
                break
            elif choice in ['no', 'n', 'yo\'q', 'y']:
                print("\n📜 Calculation History:")
                if history:
                    for i, calc in enumerate(history, 1):
                        print(f"  {i}. {calc}")
                else:
                    print("  No calculations performed")
                print("\n👋 Thank you for using Calculator!")
                return
            else:
                print("❌ Please enter 'yes' or 'no'")


if __name__ == "__main__":
    main()
