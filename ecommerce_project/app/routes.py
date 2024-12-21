from flask import render_template, jsonify
from app import app
from app.models import Product
from app.utils import calculate_user_discount
from app.logger import logger

@app.route('/products/<int:user_id>')
def get_products_with_discount(user_id):
    try:
        logger.info(f"Processing request for user {user_id}")
        
        # Get discount and category
        discount_rate, user_category = calculate_user_discount(user_id)
        logger.info(f"User category: {user_category}, Discount: {discount_rate}")
        
        # Get products from cache
        products = Product.get_all()
        if not products:
            logger.error("No products retrieved")
            return jsonify({'error': 'No products available'}), 500
            
        logger.info(f"Retrieved {len(products)} products")
        
        discounted_products = []
        for product in products:
            try:
                product_data = {
                    'name': product[1],
                    'description': product[2],
                    'original_price': float(product[3])
                }
                
                if user_category != 'Low':
                    product_data['discounted_price'] = round(product_data['original_price'] * (1 - float(discount_rate)), 2)
                
                discounted_products.append(product_data)
            except Exception as e:
                logger.error(f"Error processing product: {str(e)}")
                continue
        
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
