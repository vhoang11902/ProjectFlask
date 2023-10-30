from flask import Flask, render_template
import model.category
import model.product

app = Flask(__name__)


@app.route("/")
def home():
    cate = model.category.get_categories()
    prods = model.product.get_products()
    return render_template('index.html', categories=cate, products=prods)


@app.route("/category/<int:category_id>")
def category(category_id):
    cate = model.category.get_categories()
    prods = model.product.get_products_by_category(category_id)
    return render_template('category.html', category=cate, products=prods)


if __name__ == "__main__":
    app.run(debug=True)
