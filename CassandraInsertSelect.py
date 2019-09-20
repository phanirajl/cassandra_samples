#!/usr/bin/env python
from cassandra.cluster import Cluster
import uuid

#CREATE TABLE py_test.person (
#  id uuid,
#  first_name text,
#  last_name text,
#  PRIMARY KEY (id));

cluster = Cluster(['localhost'])

session = cluster.connect('py_test')

session.execute(
    """
    INSERT INTO person (id, first_name, last_name)
    VALUES (%(id)s, %(firstName)s, %(lastName)s)
    """,
    {'id': uuid.uuid4(), 'firstName': 'Jack', 'lastName': 'Burton'}
)

rows = session.execute('SELECT first_name, last_name FROM person')
for (first_name, last_name) in rows:
    print ("{0:s} {1:s}".format(first_name, last_name))
