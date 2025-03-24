E-commerce Category-Based Discount System

This Flask application implements a dynamic discount system using machine learning for user categorization and personalized pricing.

Features
	•	User Categorization: Categorizes users based on their spending habits using an ML model.
	•	Dynamic Discount Calculation: Discounts are applied based on user category.
	•	Caching: Caches product data for better performance.
	•	Logging: Provides detailed logs for debugging and monitoring.
	•	Database Integration: Connects to MS SQL Server for product data management.

Setup
	1.	Clone the repository:

git clone https://github.com/yourusername/repository-name.git


	2.	Install dependencies:

pip install -r requirements.txt


	3.	Configure database settings in config.py.
	4.	Run the application:

python run.py



Project Structure

/app            # Application code
  /models       # Database models and business logic
  /routes       # Flask routes for handling requests
  /logger       # Logging configuration
  /utils        # Helper functions (e.g., ML model interaction)
/data           # Data files and ML models
/templates      # HTML templates
/logs           # Log files
config.py       # Database and app configuration
run.py          # Application startup

Technologies Used
	•	Flask: Web framework
	•	SQLAlchemy: ORM for database interaction
	•	pyodbc: Database connection to MS SQL Server
	•	KMeans: Machine Learning model for user categorization
	•	pandas: Data processing
	•	Logging: Python logging module
