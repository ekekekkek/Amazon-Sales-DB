import pandas as pd
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

def populate_related_tables():
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://amazon:amazon@localhost:5432/amazon")
    engine = create_engine(DATABASE_URL)
    
    print("Loading data from products table...")
    
    with engine.connect() as conn:
        # Get all products with user/review data
        result = conn.execute(text("""
            SELECT product_id, user_id, user_name, review_id, review_title, review_content
            FROM products 
            WHERE user_id IS NOT NULL AND user_id != ''
        """))
        
        products = result.fetchall()
        print(f"Found {len(products)} products with user/review data")
        
        # Extract unique users
        users = {}
        reviews = []
        
        for product in products:
            product_id = product[0]
            user_ids = product[1].split(',') if product[1] else []
            user_names = product[2].split(',') if product[2] else []
            review_ids = product[3].split(',') if product[3] else []
            review_titles = product[4].split(',') if product[4] else []
            review_contents = product[5].split(',') if product[5] else []
            
            # Process each user/review pair
            for i, user_id in enumerate(user_ids):
                user_id = user_id.strip()
                if user_id and user_id not in users:
                    user_name = user_names[i].strip() if i < len(user_names) else None
                    users[user_id] = {
                        'user_id': user_id,
                        'user_name': user_name
                    }
                
                # Add review if we have the data
                if i < len(review_ids) and review_ids[i].strip():
                    review_id = review_ids[i].strip()
                    review_title = review_titles[i].strip() if i < len(review_titles) else None
                    review_content = review_contents[i].strip() if i < len(review_contents) else None
                    
                    reviews.append({
                        'review_id': review_id,
                        'product_id': product_id,
                        'user_id': user_id,
                        'user_name': user_names[i].strip() if i < len(user_names) else None,
                        'review_title': review_title,
                        'review_content': review_content
                    })
        
        print(f"Extracted {len(users)} unique users")
        print(f"Extracted {len(reviews)} reviews")
        
        # Clear existing data
        conn.execute(text("DELETE FROM reviews"))
        conn.execute(text("DELETE FROM users"))
        
        # Insert users one by one to avoid duplicates
        if users:
            for user_data in users.values():
                try:
                    conn.execute(text("""
                        INSERT INTO users (user_id, user_name) 
                        VALUES (:user_id, :user_name)
                    """), user_data)
                except Exception as e:
                    print(f"Skipping duplicate user: {user_data['user_id']}")
            conn.commit()
            print(f"✅ Inserted users")
        
        # Insert reviews one by one to avoid duplicates
        if reviews:
            for review_data in reviews:
                try:
                    conn.execute(text("""
                        INSERT INTO reviews (review_id, product_id, user_id, user_name, review_title, review_content) 
                        VALUES (:review_id, :product_id, :user_id, :user_name, :review_title, :review_content)
                    """), review_data)
                except Exception as e:
                    print(f"Skipping duplicate review: {review_data['review_id']}")
            conn.commit()
            print(f"✅ Inserted reviews")
        
        # Verify counts
        result = conn.execute(text("SELECT COUNT(*) FROM users"))
        user_count = result.scalar()
        result = conn.execute(text("SELECT COUNT(*) FROM reviews"))
        review_count = result.scalar()
        
        print(f"\n📊 Final counts:")
        print(f"  Users: {user_count}")
        print(f"  Reviews: {review_count}")

if __name__ == "__main__":
    populate_related_tables()
