##Using Amazon Sales DB from Kaggle. CSV contains:

product_id - Product ID 
product_name - Name of the Product 
category - Category of the Product 
discounted_price - Discounted Price of the Product 
actual_price - Actual Price of the Product 
discount_percentage - Percentage of Discount for the Product 
rating - Rating of the Product 
rating_count - Number of people who voted for the Amazon rating 
about_product - Description about the Product 
user_id - ID of the user who wrote review for the Product 
user_name - Name of the user who wrote review for the Product 
review_id - ID of the user review 
review_title - Short review 
review_content - Long review 
img_link - Image Link of the Product 
product_link - Official Website Link of the Product

##Repo layout

amazon-sql-api/
  README.md
  .env.example
  db/
    docker-compose.yml
    init/
      01_schema.sql
      02_indexes.sql
  backend/
    requirements.txt
    app/
      __init__.py
      main.py
      db.py
      models.py
      schemas.py
      routers/
        products.py
        reviews.py
        users.py
    scripts/
      load_csv.py
  data/
    amazon.csv   # put your raw CSV here
