
Scientific Calculator Web Application

Introduction  
This Scientific Calculator Web Application is a responsive, browser-based tool developed using Flask (Python) for the backend and HTML/CSS/JavaScript for the frontend. It allows users to perform both basic and scientific mathematical operations, including trigonometric functions, logarithms, factorials, and power functions. The application features a clean UI, precision control, input validation, and displays exact trigonometric results for special angles.

Objective
- Demonstrate Flask as a Python web framework.
- Build a modern UI using HTML, CSS, and JavaScript.
- Support various mathematical operations via a web interface.
- Implement input validation and exception handling.
- Return exact values for special trigonometric angles (e.g., sin(30°) = 1/2).

Features
- Basic operations: Addition, Subtraction, Multiplication, Division, Power.
- Scientific operations: Square Root, Factorial, Logarithm (base e and base 10).
- Trigonometric functions (input in degrees): sin, cos, tan.
- Exact values for angles like 30°, 45°, 60°.
- Input validation with clear error messages.
- Decimal precision control (2 to 10 decimal places).
- Simple, modern, responsive UI.

Technologies Used
Frontend:
- HTML5
- CSS3
- JavaScript (basic interaction)

Backend:
- Python 3.x
- Flask microframework
- Jinja2 templating
- Math module (Python)

Project Structure
scientific_calculator_app/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── (optional: CSS/JS files)
├── venv/ (not uploaded)

How to Run the Project

1. Install Python 3.x.

2. Create and activate a virtual environment:

Windows
python -m venv venv
venv\Scripts ctivate

Linux/macOS
python3 -m venv venv
source venv/bin/activate

3. Install Flask:
pip install flask

4. Run the app:
python app.py

5. Open in your browser:  
http://127.0.0.1:5000/

Future Enhancements
- Dark mode toggle.
- MathJax/LaTeX rendering for exact fractions.
- Graphical visualization for functions.
- Keyboard input support.
- Angle unit toggle (Degrees ↔ Radians).
- Calculation history.
- Save recent calculations with localStorage.

Conclusion  
This project showcases the integration of Python backend logic with modern web technologies to build a functional scientific calculator. It serves as both a learning project and a foundation for future feature enhancements.
