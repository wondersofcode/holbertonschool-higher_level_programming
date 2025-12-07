from flask import Flask, render_template
import json
import os

# Instantiate the Flask application
app = Flask(__name__)

# Helper function to read data from the JSON file
def read_json_data(file_path):
    """Reads and parses a JSON file, returning the data or an empty dict on error."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERROR: JSON file not found at {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"ERROR: Could not decode JSON from {file_path}")
        return {}

@app.route('/')
def home():
    """Renders a basic home page (can be index.html from previous task)."""
    return "Welcome to the Dynamic Content Application!"

@app.route('/items')
def items_list():
    """
    Reads items from items.json and renders the items.html template.
    """
    # Define the path to the JSON file (assuming it's in the same directory)
    json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'items.json')
    
    # Read data and extract the list of items
    data = read_json_data(json_file_path)
    items = data.get('items', [])  # Default to an empty list if 'items' key is missing

    # Render the template, passing the list of items
    return render_template('items.html', items=items)

if __name__ == '__main__':
    # Run the application on port 5000 with debug enabled
    app.run(debug=True, port=5000)
