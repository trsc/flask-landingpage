import peewee

#db = peewee.SqliteDatabase("/var/www/hellobudget.co/signups.db")
db = peewee.Proxy()

########################################################################
class Signup(peewee.Model):
    """
    ORM model of the Game Table
    """
    email       = peewee.CharField(unique=True)
    signup_date   = peewee.DateTimeField()

    class Meta:
        database = db


def initdb():
    try:
        Signup.create_table(True)
    except peewee.OperationalError:
        print "Signup table already exists!"
