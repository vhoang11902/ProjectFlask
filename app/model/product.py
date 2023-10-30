def get_products():
    products = [{
        "id": 1,
        "name": "Phone 1",
        "price": 200000,
        "image": "https://assets.swappie.com/cdn-cgi/image/width=600,height=600,fit=contain,format=auto/swappie-iphone-14-pro-max-deep-purple.png?v=38",
        "category_id": 1
    }, {
        "id": 2,
        "name": "Phone 2",
        "price": 200000,
        "image": "https://assets.swappie.com/cdn-cgi/image/width=600,height=600,fit=contain,format=auto/swappie-iphone-14-pro-max-deep-purple.png?v=38",
        "category_id": 1
    }, {
        "id": 3,
        "name": "Phone 21",
        "price": 200000,
        "image": "https://assets.swappie.com/cdn-cgi/image/width=600,height=600,fit=contain,format=auto/swappie-iphone-14-pro-max-deep-purple.png?v=38",
        "category_id": 2
    }, {
        "id": 4,
        "name": "Phone 22",
        "price": 200000,
        "image": "https://assets.swappie.com/cdn-cgi/image/width=600,height=600,fit=contain,format=auto/swappie-iphone-14-pro-max-deep-purple.png?v=38",
        "category_id": 2
    },
    ]
    return products


def get_products_by_category(category_id):
    return [p for p in get_products() if p["category_id"] == category_id]
