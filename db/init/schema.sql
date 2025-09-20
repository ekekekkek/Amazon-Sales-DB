CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Products
CREATE TABLE public.products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    category_path TEXT,
    category_leaf TEXT,
    discounted_price NUMERIC(12,2),
    actual_price NUMERIC(12,2) NOT NULL,
    discount_percentage NUMERIC(5,2),
    rating NUMERIC(3,2),
    rating_count INTEGER,
    about_product TEXT,
    img_link TEXT,
    product_link TEXT,
);

-- Reviews
CREATE TABLE public.reviews (
    review_id TEXT PRIMARY KEY,
    product_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    user_name TEXT NOT NULL,
    review_title TEXT NOT NULL,
)

-- Users
CREATE TABLE public.users (
    user_id TEXT PRIMARY KEY,
    user_name TEXT NOT NULL,
);