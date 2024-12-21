from flask import render_template, jsonify
from app import app, logger
from app.models import Product
from app.utils import calculate_user_discount

@app.route('/products/<int:user_id>')
def get_products_with_discount(user_id):
    try:
        discount_rate, user_category = calculate_user_discount(user_id)
        products = Product.get_all()
        discounted_products = []
        
        for product in products:
            product_data = {
                'name': product.Name,
                'description': product.Description,
                'original_price': float(product.Price)
            }
            
            if user_category != 'Low':
                product_data['discounted_price'] = round(product_data['original_price'] * (1 - float(discount_rate)), 2)
            
            discounted_products.append(product_data)
        
        return render_template('product_list.html', 
                             products=discounted_products,
                             user_category=user_category,
                             discount_percentage=discount_rate * 100)
    
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/clear-cache')
def clear_cache():
    Product._cache = None
    return jsonify({'message': 'Cache cleared successfully'})
