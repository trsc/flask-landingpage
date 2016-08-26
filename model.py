import peewee

db = peewee.SqliteDatabase("signups.db")

########################################################################
class Signup(peewee.Model):
    """
    ORM model of the Game Table
    """
    email       = peewee.CharField()
    signup_date   = peewee.DateTimeField()

    class Meta:
        database = db


def initdb():
    try:
        Signup.create_table(True)
    except peewee.OperationalError:
        print "Signup table already exists!"
