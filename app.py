from flask import Flask, render_template, request, jsonify
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)


# Custom algorithm for converting decimal to binary
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n = n // 2
    binary.reverse()
    return ''.join(binary)


# Custom algorithm for converting binary to decimal
def binary_to_decimal(b):
    decimal_value = 0
    power = 0
    for digit in reversed(b):
        decimal_value += int(digit) * (2 ** power)
        power += 1
    return decimal_value


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/b2d', methods=['POST'])
def b2d():
    value = request.form.get('binary')
    app.logger.debug(f"Received binary input: {value}")
    value = str(value)

    if not all(char in '01' for char in value):
        app.logger.error("Invalid binary input")
        return jsonify({'error': 'Invalid binary input'}), 400

    try:
        decimal_value = binary_to_decimal(value)
        app.logger.debug(f"Converted to decimal: {decimal_value}")
        return jsonify({'decimal': decimal_value})
    except Exception as e:
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/d2b', methods=['POST'])
def d2b():
    value = request.form.get('decimal')
    app.logger.debug(f"Received decimal input: {value}")

    try:
        decimal_value = int(value)
        if decimal_value < 0:
            raise ValueError("Negative numbers are not allowed")
        binary_value = decimal_to_binary(decimal_value)
        app.logger.debug(f"Converted to binary: {binary_value}")
        return jsonify({'binary': binary_value})
    except ValueError:
        app.logger.error("Invalid decimal input")
        return jsonify({'error': 'Invalid decimal input'}), 400
    except Exception as e:
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
