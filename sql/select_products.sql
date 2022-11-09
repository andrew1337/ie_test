SELECT
    *
FROM
     products
WHERE
	producer LIKE :producer
LIMIT
    :limit
OFFSET
    :offset;