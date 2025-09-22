import pandas as pd
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

def populate_reviews():
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
        
        # Clear existing reviews
        conn.execute(text("DELETE FROM reviews"))
        
        # Extract reviews with unique review_ids
        reviews = []
        seen_review_ids = set()
        
        for product in products:
            product_id = product[0]
            user_ids = product[1].split(',') if product[1] else []
            user_names = product[2].split(',') if product[2] else []
            review_ids = product[3].split(',') if product[3] else [] # split review IDs
            review_titles = product[4].split(',') if product[4] else [] # split review titles
            review_contents = product[5].split(',') if product[5] else [] # split review contents
            
            # Process each user/review pair
            for i, user_id in enumerate(user_ids):
                user_id = user_id.strip()
                
                # Add review if we have the data and it's unique
                if i < len(review_ids) and review_ids[i].strip():
                    review_id = review_ids[i].strip()
                    
                    # Only add if we haven't seen this review_id before
                    if review_id not in seen_review_ids:
                        review_title = review_titles[i].strip() if i < len(review_titles) else None
                        review_content = review_contents[i].strip() if i < len(review_contents) else None
                        user_name = user_names[i].strip() if i < len(user_names) else None
                        
                        reviews.append({
                            'review_id': review_id,
                            'product_id': product_id,
                            'user_id': user_id,
                            'user_name': user_name,
                            'review_title': review_title,
                            'review_content': review_content
                        })
                        seen_review_ids.add(review_id)
        
        print(f"Extracted {len(reviews)} unique reviews")
        
        # Insert reviews in batches
        if reviews:
            reviews_df = pd.DataFrame(reviews)
            reviews_df.to_sql('reviews', conn, if_exists='append', index=False)
            conn.commit()
            print(f"✅ Inserted {len(reviews)} reviews")
        
        # Verify count
        result = conn.execute(text("SELECT COUNT(*) FROM reviews"))
        review_count = result.scalar()
        
        print(f"\n📊 Final count:")
        print(f"  Reviews: {review_count}")

if __name__ == "__main__":
    populate_reviews()
