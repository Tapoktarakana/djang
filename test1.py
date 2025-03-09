from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='women_women';")
