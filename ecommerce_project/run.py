from app import app
from app.models import Product
from app.logger import logger

def initialize_cache():
    try:
        products = Product.get_all()
        if products:
            logger.info(f"Cache initialized with {len(products)} products")
        else:
            logger.warning("No products loaded into cache")
    except Exception as e:
        logger.error(f"Cache initialization error: {str(e)}")

if __name__ == "__main__":
    logger.info("Starting application")
    initialize_cache()
    app.run(debug=True, port=5001)
