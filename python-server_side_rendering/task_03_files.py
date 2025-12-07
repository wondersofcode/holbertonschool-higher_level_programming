from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

# Path helpers (assumes JSON/CSV are next to this file)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, 'products.json')
CSV_PATH = os.path.join(BASE_DIR, 'products.csv')

def read_products_json(path=JSON_PATH):
    """Read products from JSON file and return a list of dicts with typed fields."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Ensure types are normalized
        products = []
        for item in data:
            products.append({
                'id': int(item.get('id')),
                'name': item.get('name', ''),
                'category': item.get('category', ''),
                'price': float(item.get('price', 0.0))
            })
        return products
    except FileNotFoundError:
        return []  # or raise if you prefer
    except Exception:
        # In case JSON malformed
        return []

def read_products_csv(path=CSV_PATH):
    """Read products from CSV file and return a list of dicts with typed fields."""
    products = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Defensive parsing with fallback defaults
                try:
                    pid = int(row.get('id', '').strip())
                except Exception:
                    # skip rows with invalid id
                    continue
                try:
                    price = float(row.get('price', 0.0))
                except Exception:
                    price = 0.0
                products.append({
                    'id': pid,
                    'name': row.get('name', '').strip(),
                    'category': row.get('category', '').strip(),
                    'price': price
                })
    except FileNotFoundError:
        return []
    except Exception:
        return []
    return products

@app.route('/products')
def products():
    """
    Query params:
      - source: 'json' or 'csv' (defaults to 'json' if not provided)
      - id: optional product id to filter (integer)
    """
    source = request.args.get('source', 'json').lower().strip()
    id_param = request.args.get('id', None)

    # Validate source
    if source not in ('json', 'csv'):
        # Render template with error message "Wrong source"
        return render_template('product_display.html',
                               products=None,
                               error="Wrong source. Allowed values: 'json' or 'csv'.",
                               source=source,
                               requested_id=id_param)

    # Read products depending on source
    if source == 'json':
        all_products = read_products_json()
    else:
        all_products = read_products_csv()

    # If id is provided, try to parse and filter
    if id_param is not None and id_param != '':
        # Validate id is integer
        try:
            requested_id = int(id_param)
        except ValueError:
            return render_template('product_display.html',
                                   products=None,
                                   error="Invalid id parameter. Must be an integer.",
                                   source=source,
                                   requested_id=id_param)

        # Find product with matching id
        matched = [p for p in all_products if p.get('id') == requested_id]
        if not matched:
            return render_template('product_display.html',
                                   products=None,
                                   error=f"Product not found for id={requested_id}.",
                                   source=source,
                                   requested_id=requested_id)
        # found one (or potentially multiple if duplicate ids exist) — pass them
        return render_template('product_display.html',
                               products=matched,
                               error=None,
                               source=source,
                               requested_id=requested_id)

    # No id provided — render all products
    return render_template('product_display.html',
                           products=all_products,
                           error=None,
                           source=source,
                           requested_id=None)

if __name__ == '__main__':
    # Run dev server on port 5000
    app.run(debug=True)
