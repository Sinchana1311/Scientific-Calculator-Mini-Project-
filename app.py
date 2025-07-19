from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Special angle lookup table for trigonometric values
special_trig_values = {
    'sin': {
        0: '0',
        30: '1/2',
        45: '√2/2',
        60: '√3/2',
        90: '1'
    },
    'cos': {
        0: '1',
        30: '√3/2',
        45: '√2/2',
        60: '1/2',
        90: '0'
    },
    'tan': {
        0: '0',
        30: '1/√3',
        45: '1',
        60: '√3'
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        try:
            operator = request.form.get('operator')
            precision = int(request.form.get('precision', 4))
            num1_raw = request.form.get('num1')
            num2_raw = request.form.get('num2')

            if not num1_raw:
                raise ValueError("First number is required.")
            num1 = float(num1_raw)

            if operator in ['add', 'subtract', 'multiply', 'divide', 'power']:
                if not num2_raw:
                    raise ValueError("Second number is required for this operation.")
                num2 = float(num2_raw)

                if operator == 'add':
                    result = num1 + num2
                elif operator == 'subtract':
                    result = num1 - num2
                elif operator == 'multiply':
                    result = num1 * num2
                elif operator == 'divide':
                    if num2 == 0:
                        raise ValueError("Division by zero is not allowed.")
                    result = num1 / num2
                elif operator == 'power':
                    result = math.pow(num1, num2)

            elif operator == 'sqrt':
                if num1 < 0:
                    raise ValueError("Cannot take square root of negative number.")
                result = math.sqrt(num1)

            elif operator in ['sin', 'cos', 'tan']:
                deg = int(num1)
                if operator == 'tan' and (deg % 180 == 90):
                    raise ValueError("Tan is undefined at 90°, 270°, etc.")

                if deg in special_trig_values[operator]:
                    result = f"{special_trig_values[operator][deg]} (exact)"
                else:
                    val = math.__dict__[operator](math.radians(num1))
                    result = round(val, precision)

            elif operator == 'log':
                if num1 <= 0:
                    raise ValueError("Log is undefined for zero or negative numbers.")
                result = round(math.log(num1), precision)

            elif operator == 'log10':
                if num1 <= 0:
                    raise ValueError("Log10 is undefined for zero or negative numbers.")
                result = round(math.log10(num1), precision)

            elif operator == 'factorial':
                if num1 < 0 or not num1.is_integer():
                    raise ValueError("Factorial only works for non-negative integers.")
                factorial_result = math.factorial(int(num1))
                # Format huge numbers nicely
                if factorial_result > 1e10:
                    result = f"{factorial_result:.5e}"  # scientific notation
                else:
                    result = f"{factorial_result:,}"  # comma-separated

            else:
                raise ValueError("Invalid operation selected.")

        except Exception as e:
            error = str(e)

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
