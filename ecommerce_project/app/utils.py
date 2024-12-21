import pandas as pd
import pickle
import os
import numpy as np
from sklearn.cluster import KMeans
from app.logger import logger

def calculate_user_discount(user_id):
    try:
        # Load data files
        data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        csv_path = os.path.join(data_dir, 'categorized_users.csv')
        model_path = os.path.join(data_dir, 'kmeans_user_categorization.pkl')
        
        # Read CSV file
        df = pd.read_csv(csv_path)
        
        # Get user data
        user_data = df[df['UserID'] == user_id]
        if user_data.empty:
            logger.warning(f"User {user_id} not found")
            return 0.0, 'Unknown'
            
        # Get base category
        category = user_data['Category'].values[0]
        logger.info(f"Base category for user {user_id}: {category}")
        
        try:
            # Load and verify KMeans model
            with open(model_path, 'rb') as f:
                kmeans_model = pickle.load(f)
                
            if isinstance(kmeans_model, KMeans):
                # Prepare features for prediction
                features = user_data[['TotalSpending', 'NumEvents']].values.reshape(1, -1)
                cluster = kmeans_model.predict(features)[0]
                logger.info(f"ML model cluster prediction: {cluster}")
                
                # Adjust category based on ML insights
                if cluster == 1 and category != 'Star':
                    category = 'High'  # Upgrade to High if in high-value cluster
                    logger.info(f"Category upgraded to High based on ML prediction")
            else:
                logger.warning("Invalid KMeans model format, using base category")
                
        except Exception as e:
            logger.warning(f"ML prediction failed: {e}, using base category")
        
        # Define discount rates
        discount_rates = {
            'Low': 0.0,     # No discount
            'Mid': 0.10,    # 10% discount
            'High': 0.15,   # 15% discount
            'Star': 0.20    # 20% discount
        }
        
        discount = discount_rates.get(category, 0.0)
        logger.info(f"Final discount: {discount * 100}% for {category} category")
        return float(discount), category
        
    except Exception as e:
        logger.error(f"Error calculating discount: {str(e)}")
        return 0.0, 'Unknown'
