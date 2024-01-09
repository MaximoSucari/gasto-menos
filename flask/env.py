def change_sqlite_settings():
    __import__("pysqlite3")
    import sys

    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")


change_sqlite_settings()