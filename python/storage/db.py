import configparser

class DB:

  @staticmethod
  def get_db_string():
    config = configparser.ConfigParser()
    config.read('./config.ini')

    db = config['DB'].get('db_type')
    user = config['DB'].get('username')
    pw = config['DB'].get('password')
    host = config['DB'].get('host')
    port = config['DB'].get('port')
    name = config['DB'].get('db_name')

    return "{0}://{1}:{2}@{3}:{4}/{5}".format(db, user, pw, host, port, name)
