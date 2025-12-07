from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# -----------------------------
# Load JSON
# -----------------------------
def load_json_data(product_id=None):
    try:
        with open("products.json") as json_file:
            data = json.load(json_file)

        if product_id:
            data = [p for p in data if int(p.get("id")) == product_id]

        return data
    except Exception as e:
        return {"error": f"JSON loading error: {str(e)}"}


# -----------------------------
# Load CSV
# -----------------------------
def load_csv_data(product_id=None):
    try:
        products = []
        with open("products.csv") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)

        if product_id:
            products = [p for p in products if p["id"] == product_id]

        return products
    except Exception as e:
        return {"error": f"CSV loading error: {str(e)}"}


# -----------------------------
# Load SQL (SQLite)
# -----------------------------
def load_sql_data(product_id=None):
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        if product_id:
            cursor.execute(
                "SELECT id, name, category, price FROM Products WHERE id = ?",
                (product_id,)
            )
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")

        rows = cursor.fetchall()
        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        return products

    except Exception as e:
        return {"error": f"Database error: {str(e)}"}


# -----------------------------
# Main Route
# -----------------------------
@app.route("/products")
def products():
    source = request.args.get("source", "").lower()
    product_id = request.args.get("id")

    if product_id:
        try:
            product_id = int(product_id)
        except:
            return render_template("product_display.html",
                                   error="Invalid ID",
                                   products=None)

    if source == "json":
        products = load_json_data(product_id)

    elif source == "csv":
        products = load_csv_data(product_id)

    elif source == "sql":
        products = load_sql_data(product_id)

    else:
        return render_template("product_display.html",
                               error="Wrong source",
                               products=None)

    # Error from loader
    if isinstance(products, dict) and "error" in products:
        return render_template("product_display.html",
                               error=products["error"],
                               products=None)

    # 🔥 REQUIRED FOR THE TEST
    # If ID was provided but no product exists → show "Product not found"
    if product_id and products == []:
        return render_template("product_display.html",
                               error="Product not found",
                               products=None)

    return render_template("product_display.html",
                           error=None,
                           products=products)

if __name__ == "__main__":
    app.run(debug=True)
