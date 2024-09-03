# Binary to Denary Converter

## Project Overview

This project involves designing, coding, testing, and evaluating a Python program that converts between binary and decimal (denary) numbers. The purpose of this project is to demonstrate two different approaches to solving the problem: using Python's built-in functions and implementing custom algorithms. The project is organised into two branches: `simple` and `complex`.

## Branches

### 1. Simple Branch

The `simple` branch focuses on utilising Python's built-in functions for converting between binary and decimal numbers. This approach is straightforward and leverages Python’s powerful standard library to achieve the desired conversions with minimal code.

#### Key Functions Used:
- **`bin()`**: Converts a decimal (integer) number to a binary string.
- **`int()`**: Converts a binary string to a decimal number by specifying the base as 2.

#### Example Usage:
```python
decimal_number = 43
binary_string = bin(decimal_number)[2:]  # Output: '101011'

binary_string = '101011'
decimal_number = int(binary_string, 2)  # Output: 43
```

#### Benefits:
- **Simplicity**: The built-in functions require less code and are easy to understand.
- **Efficiency**: These functions are optimised and perform the conversions quickly.

### 2. Complex Branch

The `complex` branch showcases a manual implementation of algorithms to convert between binary and decimal numbers. This approach shows the logic behind the conversions and how these processes work under the hood.

#### Custom Algorithms:

- **Decimal to Binary**:
  - Divides the decimal number by 2 repeatedly.
  - Records the remainders.
  - The binary equivalent is formed by reading the remainders in reverse order.

- **Binary to Decimal**:
  - Iterates over each bit in the binary string.
  - Multiplies each bit by the power of 2 corresponding to its position.
  - Sums all these values to get the decimal equivalent.

#### Example Code:
```python
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n = n // 2
    binary.reverse()
    return ''.join(binary)

def binary_to_decimal(b):
    decimal_value = 0
    power = 0
    for digit in reversed(b):
        decimal_value += int(digit) * (2 ** power)
        power += 1
    return decimal_value
```

#### Benefits:
- **Educational Value**: Provides insight into the manual process of conversion, which is valuable for understanding binary arithmetic.
- **Customisation**: Allows for more control over the conversion process, which can be modified or extended as needed.
- **Algorithmic Thinking**: Encourages thinking in terms of algorithms and problem-solving.
- **Error Handling**: Provides the opportunity to implement custom error handling logic.
- **Scalability**: Can be extended to handle larger numbers or additional conversion types.
- **Performance Analysis**: Allows for a detailed performance analysis of the custom algorithms.

## Testing

Both branches have been tested with various inputs to ensure correctness. The test cases include:
- Converting a range of decimal numbers (e.g., 0, 1, 43, 255) to binary and verifying the output.
- Converting a range of binary strings (e.g., '0', '1', '101011', '11111111') to decimal and verifying the output.
- Handling invalid inputs, such as non-binary strings or out-of-range decimal numbers, and ensuring appropriate error messages are displayed.

### Test Plan and Results:

| Test Case                        | Input                | Expected Output                | Simple Branch Output  | Complex Branch Output | Pass/Fail |
|----------------------------------|----------------------|--------------------------------|------------------------|------------------------|-----------|
| Convert decimal 43 to binary     | Decimal: 43          | Binary: 101011                 | 101011                 | 101011                 | Pass      |
| Convert binary 101011 to decimal | Binary: 101011       | Decimal: 43                    | 43                     | 43                     | Pass      |
| Convert decimal 0 to binary      | Decimal: 0           | Binary: 0                      | 0                      | 0                      | Pass      |
| Convert binary 0 to decimal      | Binary: 0            | Decimal: 0                     | 0                      | 0                      | Pass      |
| Invalid binary input             | Binary: 102          | Error message                  | Error message          | Error message          | Pass      |
| Invalid decimal input            | Decimal: 300         | Error message                  | Error message          | Error message          | Pass      |

## Evaluation

### Comparison of Methods:
- **Simplicity vs. Understanding**: The `simple` branch demonstrates the ease of using built-in Python functions, making it the best choice for quick and efficient development. However, the `complex` branch offers a detailed view of the underlying logic, which is useful for educational purposes.
- **Performance**: The built-in functions in the `simple` branch are highly optimised and perform faster than the custom algorithms in the `complex` branch. However, for the given problem size (values up to 255), the performance difference is negligible.

### Potential Improvements:
- **Complex Branch**:
  - Extend the custom algorithm to handle larger numbers and negative integers.
  - Implement additional error handling for non-numeric input.
- **Simple Branch**:
  - While the simple branch is already efficient, adding more detailed comments could improve code readability and understanding.

## Conclusion

This project demonstrates two different approaches to solving the binary-decimal conversion problem. By exploring both the simplicity of built-in functions and the complexity of manual algorithms, the project showcases a balanced understanding of Python programming and binary arithmetic. 

Feel free to explore the two branches to see the differences in implementation, and refer to the code and test results for more details.

---

### How to Use

1. Visit bridging.leoroberts.uk to access the hosted app.
2. Type a decimal into the decimal field or a binary into the binary field.
3. The converted number will appear in the other box, you can edit and it will update real time.
