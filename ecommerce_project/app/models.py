from app import db
from app.logger import logger

class Product(db.Model):
    __tablename__ = 'PRODUCT'
    
    ProductID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Description = db.Column(db.String(500))
    Price = db.Column(db.Numeric(10, 2))
    Weight = db.Column(db.Numeric(10, 2))
    HSCode = db.Column(db.String(20))
    MinimumStock = db.Column(db.Integer)
    
    _cache = None
    
    @classmethod
    def get_all(cls):
        try:
            if cls._cache is not None:
                logger.info("Returning products from cache")
                return cls._cache
                
            logger.info("Fetching products from database")
            products = cls.query.all()
            cls._cache = products
            logger.info(f"Cached {len(products)} products")
            return products
            
        except Exception as e:
            logger.error(f"Error fetching products: {str(e)}")
            return cls._cache if cls._cache is not None else []
