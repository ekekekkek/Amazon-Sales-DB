-- Indexes
CREATE INDEX IF NOT EXISTS idx_products_category ON public.products(category);
CREATE INDEX IF NOT EXISTS idx_products_rating ON public.products(rating);
CREATE INDEX IF NOT EXISTS idx_products_rating_count ON public.products(rating_count);
CREATE INDEX IF NOT EXISTS idx_reviews_product ON public.reviews(product_id);