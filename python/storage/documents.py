from storage.db import DB
from sqlalchemy import create_engine

class Documents:

  @staticmethod
  def fetch_all():
    db = create_engine(DB.get_db_string())
    return db.execute("SELECT id, author, title, owner FROM document WHERE NOT title='Welcome to Recogito'").fetchall()
