import itertools
import db
from faker import Faker
from models.base import BasicTable



if __name__ == "__main__":

    fake = Faker()
    rec = ((fake.name(),"the "+fake.job()+" of "+fake.city()) for i in itertools.repeat(1))
    batch = 1000

    with db.session_context() as sess:
        for i in range(batch):
            (name,full) = next(rec)
            sess.add(BasicTable(name=name, fullname=full))

