from flask import Flask, render_template, request, jsonify
import logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/b2d', methods=['POST'])
def b2d():
    value = request.form.get('binary')
    app.logger.debug(f"Received binary input: {value}")
    value = str(value)
    try:
        decimal_value = int(value, 2)
        app.logger.debug(f"Converted to decimal: {decimal_value}")
        return jsonify({'decimal': decimal_value})
    except ValueError:
        app.logger.error("Invalid binary input")
        return jsonify({'error': 'Invalid binary input'}), 400
    except Exception as e:
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/d2b', methods=['POST'])
def d2b():
    value = request.form.get('decimal')
    try:
        binary_value = bin(int(value))[2:]
        return jsonify({'binary': binary_value})
    except ValueError:
        return jsonify({'error': 'Invalid decimal input'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
