document.addEventListener('DOMContentLoaded', () => {
    const binaryInput = document.getElementById('binary');
    const decimalInput = document.getElementById('decimal');
    const form = document.getElementById('conversionForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way
        const binaryValue = binaryInput.value;
        const decimalValue = decimalInput.value;

        if (binaryValue) {
            convertBinaryToDecimal(binaryValue);
        } else if (decimalValue) {
            convertDecimalToBinary(decimalValue);
        }
    });

    binaryInput.addEventListener('input', function() {
        if (this.value) {
            convertBinaryToDecimal(this.value);
        }
    });

    decimalInput.addEventListener('input', function() {
        if (this.value) {
            convertDecimalToBinary(this.value);
        }
    });

    function convertBinaryToDecimal(binary) {
        fetch('/api/b2d', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'binary': binary
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error(data.error);
            } else {
                decimalInput.value = data.decimal;
            }
        })
        .catch(error => console.error('Error:', error));
    }

    function convertDecimalToBinary(decimal) {
        fetch('/api/d2b', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'decimal': decimal
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error(data.error);
            } else {
                binaryInput.value = data.binary;
            }
        })
        .catch(error => console.error('Error:', error));
    }
});
