from sqlalchemy import create_engine

class Documents:

  @staticmethod
  def fetch_all():
    db_string = "postgresql://postgres:postgres@localhost:5432/recogito-test"
    db = create_engine(db_string)
    return db.execute("SELECT id, author, title, owner FROM document WHERE NOT title='Welcome to Recogito'").fetchall()
