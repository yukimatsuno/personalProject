# SQLite DBを操作するためのモジュールをインポート
import sqlite3

# 指定されたパスにあるSQLite DBファイルに接続する
# connect()関数は、データベースに接続するためのConnectionオブジェクトを返す
conn = sqlite3.connect('/path/to/file.sqlite')

# 接続されたDB上でSQLクエリを実行するためのカーソルオブジェクトを作成する
# cursor()メソッドはカーソルオブジェクトを返す
# カーソルオブジェクトを使用して、DB上でクエリを実行し、結果を取得することができる
db = conn.cursor()

# クエリ例
def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    # 「？」は引数「name」のプレイスホルダー　
    query = """
        SELECT COUNT(*)
        FROM directors
        WHERE name LIKE ?
    """
    db.execute(query, (f"%{name}%",))
    count = db.fetchone()
    return count[0]


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    # 「？」は引数「name」のプレイスホルダー　
    query = """
        SELECT title
        FROM movies
        WHERE minutes > ?
        ORDER BY title
    """
    db.execute(query, (min_length,))
    movies = db.fetchall()
    return [movie[0] for movie in movies]