import pandas as pd
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def load_data():
    # Get database URL from environment
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://amazon:amazon@localhost:5432/amazon")
    
    print("Loading Amazon sales data...")
    print(f"Database URL: {DATABASE_URL}")
    
    # Read CSV file
    df = pd.read_csv('../data/amazon.csv')
    print(f"Loaded {len(df)} records from CSV")
    
    # Create database engine
    engine = create_engine(DATABASE_URL)
    
    # Load data into products table
    df.to_sql('products', engine, if_exists='replace', index=False)
    print("✅ Data loaded successfully!")
    
    # Verify data was loaded
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM products"))
        count = result.fetchone()[0]
        print(f"📊 {count} products now in database")

if __name__ == "__main__":
    load_data()