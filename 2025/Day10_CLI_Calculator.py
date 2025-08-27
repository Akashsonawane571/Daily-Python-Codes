# Day10_CLI_Calculator.py
# Command Line Calculator using argparse

import argparse

def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "❌ Division by zero!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🧮 Simple CLI Calculator")
    
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"],
                        help="Operation to perform")
    parser.add_argument("x", type=float, help="First number")
    parser.add_argument("y", type=float, help="Second number")

    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.x, args.y)
    elif args.operation == "sub":
        result = sub(args.x, args.y)
    elif args.operation == "mul":
        result = mul(args.x, args.y)
    elif args.operation == "div":
        result = div(args.x, args.y)

    print(f"✅ Result: {result}")
