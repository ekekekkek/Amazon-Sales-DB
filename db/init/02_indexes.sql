-- Indexes
CREATE INDEX IF NOT EXISTS idx_products_category_leaf ON public.products(category_leaf);
CREATE INDEX IF NOT EXISTS idx_products_rating ON public.products(rating);
CREATE INDEX IF NOT EXISTS idx_products_rating_count ON public.products(rating_count);
CREATE INDEX IF NOT EXISTS idx_reviews_product ON public.reviews(product_id);