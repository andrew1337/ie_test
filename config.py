from pathlib import Path


def read_file(file: Path) -> str:
    with open(file, "r") as sql:
        return sql.read()


DATABASE = "db.sqlite"
DATA = Path("data/data.csv")

products_schema = read_file(Path("sql/products_schema.sql"))
tmp_products_schema = read_file(Path("sql/tmp_products_schema.sql"))
update_products_from_tmp = read_file(Path("sql/update_products_from_tmp.sql"))
drop_tmp_products = read_file(Path("sql/drop_tmp_products.sql"))
select_products = read_file(Path("sql/select_products.sql"))
count_products = read_file(Path("sql/count_products.sql"))
count_where_products = read_file(Path("sql/count_where_products.sql"))
