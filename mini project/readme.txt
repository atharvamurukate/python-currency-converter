# Python Modern Currency Converter

## Overview
This project is a modern currency converter built using Python and Flask. It allows users to convert between different currencies.

## Features
- Convert between multiple currencies
- Fetch real-time exchange rates
- User-friendly web interface

## Requirements
- Python 3.x
- `requests` library for fetching exchange rates
- `flask` library for the web framework

## Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required libraries using pip:
   ```
   pip install requests flask
   ```

## Usage
1. Run the Flask application to start the web server:
   ```
   python app.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000/`.
3. Use the interface to select the currencies you want to convert between.
4. Enter the amount you want to convert.
5. Click the "Convert" button to see the converted amount.

## Files
- `app.py`: The main script to run the Flask application.
- `converter.py`: Contains the logic for currency conversion.
- `templates/index.html`: The HTML file for the web interface.
- `static/styles.css`: The CSS file for styling the web interface.
- `static/script.js`: The JavaScript file for frontend logic.

## License
This project is licensed under the MIT License.

## Acknowledgements
- Exchange rate data provided by [ExchangeRate-API](https://www.exchangerate-api.com/)

## Pushing to GitHub
1. Create a GitHub repository.
2. Initialize a Git repository in your project directory:
   ```
   git init
   ```
3. Add your files to the repository:
   ```
   git add .
   ```
4. Commit your changes:
   ```
   git commit -m "Initial commit"
   ```
5. Add the remote repository:
   ```
   git remote add origin <your-repository-url>
   ```
   Replace `<your-repository-url>` with the URL of your GitHub repository.
6. Push your changes:
   ```
   git push -u origin master
   ```
