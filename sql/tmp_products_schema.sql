CREATE TABLE IF NOT EXISTS tmp_products(
  "product_name" TEXT NOT NULL,
  "photo_url" TEXT,
  "barcode" TEXT NOT NULL,
  "price_cents" INTEGER NOT NULL,
  "sku" TEXT NOT NULL UNIQUE,
  "producer" TEXT
);