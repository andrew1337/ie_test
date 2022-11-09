INSERT INTO
    products(
        product_name,
        photo_url,
        barcode,
        price_cents,
        sku,
        producer
    )
SELECT
    tmp_products.product_name,
    tmp_products.photo_url,
    tmp_products.barcode,
    tmp_products.price_cents,
    tmp_products.sku,
    tmp_products.producer
FROM
    tmp_products
WHERE NOT EXISTS (
    SELECT 1 FROM products WHERE products.sku = tmp_products.sku
);
