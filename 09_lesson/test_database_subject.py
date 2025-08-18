from sqlalchemy import create_engine

from sqlalchemy.sql import text
from database1 import db



def test_add_new_subject():
    with db.connect() as connection:
        sql = text("insert into subject(subject_id, subject_title) values (:id, :title)")
        connection.execute(sql, {"id":18, "title": "Geo"})
        connection.commit()

        result = connection.execute(text("select * from subject where subject_id = :id"),{"id":18}).fetchone()
        assert result is not None
        assert result.subject_title == "Geo"


def test_update_subject_name():
    with db.connect() as connection:
        sql = text("update subject set subject_title = :title where subject_id = :id")
        connection.execute(sql, {"id":18, "title": "GeoG"})
        connection.commit()

        result = connection.execute(text("select * from subject where subject_id = :id"),{"id":18}).fetchone()
        assert result.subject_title == "GeoG"


def test_delete_subject():
    with db.connect() as connection:
        sql = text("delete from subject where subject_id = :id")
        connection.execute(sql, {"id": 18})
        connection.commit()

        result = connection.execute(text("select * from subject where subject_id = :id"), {"id":18}).fetchone()
        assert result is None



