import sqlite3
import config
from flask import Flask, g, request

# todo: logger = logging.getLogger()
app = Flask(__name__)
app.config.from_object("config")


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(config.DATABASE)
        g._database.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    cur = get_db()
    sql_filter = {
        "offset": request.args.get("offset", default=0, type=int),
        "limit": request.args.get("limit", default=100, type=int),
        "producer": request.args.get("producer", default="%", type=str),
    }
    resp = {
        **sql_filter,
        "count": None,
        "items": None,
    }
    with cur:
        rows = cur.execute(config.select_products, sql_filter).fetchall()
        resp["items"] = [dict(row) for row in rows]
        resp["count"] = (
            cur.execute(config.count_where_products, sql_filter).fetchone()[0] or 0
        )
    return resp


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
