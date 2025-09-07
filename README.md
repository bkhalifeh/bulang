# Bulang Programming Language

A lightweight, Java-like programming language implemented in Python with a complete interpreter featuring lexical analysis, syntax parsing, and execution engine.

## 🚀 Features

- **Java-like Syntax**: Familiar C-style syntax with braces and semicolons
- **Static Typing**: Explicit type declarations for variables
- **Control Flow**: Support for if/else statements, else-if chains, and while loops
- **Expression Evaluation**: Complex arithmetic and logical expressions with proper precedence
- **Block Scoping**: Lexical scoping with nested block support
- **Built-in Functions**: Print statements for output
- **Error Handling**: Comprehensive error reporting for syntax and runtime errors

## 📋 Language Specification

### Data Types

| Type      | Description       | Default Value | Example         |
| --------- | ----------------- | ------------- | --------------- |
| `int`     | Integer numbers   | `0`           | `42`, `-17`     |
| `String`  | Text strings      | `""`          | `"Hello World"` |
| `boolean` | True/false values | `false`       | `true`, `false` |

### Variable Declaration and Assignment

```java
// Variable declaration with initialization
int x = 10;
string name = "Bulang";
boolean isActive = true;

// Declaration without initialization (uses default value)
int y;        // y = 0
string msg;   // msg = ""
boolean flag; // flag = false

// Variable assignment
x = 20;
name = "Updated";
isActive = false;
```

### Operators

#### Arithmetic Operators

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division

#### Comparison Operators

- `==` Equal to
- `!=` Not equal to
- `<` Less than
- `>` Greater than
- `<=` Less than or equal to
- `>=` Greater than or equal to

#### Assignment Operator

- `=` Assignment

### Control Flow

#### If-Else Statements

```java
// Simple if statement
if (x > 0) {
    print("Positive number");
}

// If-else statement
if (age >= 18) {
    print("Adult");
} else {
    print("Minor");
}

// If-else-if chains
if (score >= 90) {
    print("Grade A");
} else if (score >= 80) {
    print("Grade B");
} else if (score >= 70) {
    print("Grade C");
} else {
    print("Grade F");
}
```

#### While Loops

```java
// Basic while loop
int i = 0;
while (i < 5) {
    print(i);
    i = i + 1;
}

// Nested while loops
int outer = 0;
while (outer < 3) {
    int inner = 0;
    while (inner < 2) {
        print("Outer: " + outer + ", Inner: " + inner);
        inner = inner + 1;
    }
    outer = outer + 1;
}
```

### Block Statements and Scoping

```java
int globalVar = 100;

{
    int blockVar = 200;
    print(globalVar);  // Accessible: 100
    print(blockVar);   // Accessible: 200

    {
        int nestedVar = 300;
        print(globalVar);  // Accessible: 100
        print(blockVar);   // Accessible: 200
        print(nestedVar);  // Accessible: 300
    }

    // print(nestedVar); // Error: nestedVar not accessible here
}

// print(blockVar); // Error: blockVar not accessible here
print(globalVar);    // Accessible: 100
```

### Built-in Functions

#### Print Statement

```java
print(expression);

// Examples
print("Hello, World!");
print(42);
print(x + y * 2);
print(name);
```

### Complex Expressions

```java
// Arithmetic expressions with precedence
int result = 10 + 5 * 2;        // result = 20 (not 30)
int complex = (10 + 5) * 2;     // complex = 30

// Nested expressions
int nested = ((a + b) * (c - d)) / (e + f);

// Boolean expressions
boolean condition = (x > 0) && (y < 100);
if ((age >= 18) && (hasLicense == true)) {
    print("Can drive");
}
```

## 🛠️ Installation and Usage

### Prerequisites

- Python 3.6 or higher

### Running Bulang Code

1. **Save your Bulang code** in a string or file:

```python
code = '''
int x = 10;
int y = 20;
int sum = x + y;
print("The sum is:");
print(sum);
'''
```

2. **Execute using the interpreter**:

```python
from bulang import run_bulang

# Run your Bulang code
run_bulang(code)
```

3. **Complete example**:

```python
# example.py
from bulang import run_bulang

# Factorial calculation program
factorial_program = '''
int num = 5;
int factorial = 1;
int counter = 1;

print("Calculating factorial of:");
print(num);

while (counter <= num) {
    factorial = factorial * counter;
    counter = counter + 1;
}

print("Factorial result:");
print(factorial);
'''

run_bulang(factorial_program)
```

## 📝 Example Programs

### 1. Basic Calculator

```java
int a = 15;
int b = 7;

print("Addition:");
print(a + b);

print("Subtraction:");
print(a - b);

print("Multiplication:");
print(a * b);

print("Division:");
print(a / b);
```

### 2. Grade Calculator

```java
int score = 87;

if (score >= 90) {
    print("Grade: A");
    print("Excellent!");
} else if (score >= 80) {
    print("Grade: B");
    print("Good job!");
} else if (score >= 70) {
    print("Grade: C");
    print("Average");
} else if (score >= 60) {
    print("Grade: D");
    print("Below average");
} else {
    print("Grade: F");
    print("Failed");
}
```

### 3. Number Pattern Generator

```java
int rows = 4;
int i = 1;

while (i <= rows) {
    int j = 1;
    while (j <= i) {
        print(j);
        j = j + 1;
    }
    print("---");
    i = i + 1;
}
```

### 4. Complex Nested Logic

```java
int x = 5;
int y = 10;
int z = 15;

if (x > 0) {
    print("x is positive");

    if (y > x) {
        print("y is greater than x");

        while (z > y) {
            print("z is currently:");
            print(z);
            z = z - 3;
        }
    }
} else {
    print("x is not positive");
}

print("Final values:");
print("x ="); print(x);
print("y ="); print(y);
print("z ="); print(z);
```

## 🏗️ Architecture

The Bulang interpreter consists of three main components:

### 1. **Lexer (Tokenizer)**

- Converts source code into tokens
- Handles keywords, operators, literals, and identifiers
- Provides line number tracking for error reporting

### 2. **Parser**

- Implements recursive descent parsing
- Builds Abstract Syntax Tree (AST) from tokens
- Enforces proper operator precedence and associativity
- Handles complex nested expressions and statements

### 3. **Interpreter**

- Executes AST using the Visitor pattern
- Manages variable environments and scoping
- Handles control flow execution
- Provides runtime error checking

## 🚫 Current Limitations

- **No functions/methods**: Cannot define custom functions
- **No arrays**: Only primitive data types supported
- **No for loops**: Only while loops available
- **No logical operators**: No `&&`, `||`, `!` operators
- **No string operations**: Limited string manipulation
- **No file I/O**: No file reading/writing capabilities
- **No classes/objects**: No object-oriented features

## 🔧 Error Handling

### Syntax Errors

```
Parser error at line 3: Expected ';' after variable declaration
```

### Runtime Errors

```
Error: Undefined variable: undefinedVar
Error: Division by zero
```

### Lexer Errors

```
Lexer error at line 2: Unexpected character: @
```

## 🧪 Testing

The interpreter includes comprehensive test cases covering:

- Basic arithmetic operations
- Variable declarations and assignments
- Control flow statements (if/else, while)
- Complex nested expressions
- Block scoping and variable visibility
- Error conditions and edge cases

Run tests with:

```bash
PYTHONPATH=. python3 test
```

## 🤝 Contributing

Contributions are welcome! Potential areas for improvement:

- Add support for functions and parameters
- Implement for loops and do-while loops
- Add logical operators (&&, ||, !)
- Support for arrays and collections
- String manipulation functions
- File I/O operations
- Object-oriented features
- Better error messages with suggestions

## 📄 License

This project is open source and available under the MIT License.

---

**Bulang** - A simple yet powerful programming language for learning language implementation concepts and basic programming constructs.
