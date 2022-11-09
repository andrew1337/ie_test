import sqlite3
import config
from pathlib import Path
import subprocess


def load_data_to_temp(database: str, data: Path) -> None:
    # sqlite3 db.sqlite
    #   .mode csv
    #   .separator "," "\n"
    #   .import --skip 1 data/data.csv tmp_products
    # faster way: https://odo.pydata.org/en/latest/perf.html#csv-sqlite3-57m-31s
    subprocess.check_output(
        [
            "sqlite3",
            database,
            "-cmd",
            ".mode csv",
            '.separator "," "\\n"',
            f".import --skip 1 {data} tmp_products",
        ],
    )


def main():
    with sqlite3.connect(config.DATABASE) as con:
        con.execute(config.products_schema)
        count = con.execute(config.count_products).fetchone()[0]
        print(f"initial products {count=}")
        con.execute(config.drop_tmp_products)
        con.execute(config.tmp_products_schema)
        load_data_to_temp(config.DATABASE, config.DATA)
        con.execute(config.update_products_from_tmp)
        count = con.execute(config.count_products).fetchone()[0]
        print(f"products {count=}")


if __name__ == "__main__":
    main()
