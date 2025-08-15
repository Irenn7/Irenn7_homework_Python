import pytest
from sqlalchemy import create_engine, text
from database import engine

db_connection_string = 'postgresql://postgres:RoyaL@localhost:5432/postgres'
db = create_engine(db_connection_string)


# Создадим новый предмет
def test_add_new_subject():
    connection = db.connect()
    sql = text("insert into subject(subject_id, subject_title)value (:id, :title)")
    connection.execute(sql, {"id":18, "title": "Geo"})
    connection.commit()

    # Проверяем наличие записи в таблице subjects
    result = connection.execute(text("select * from subject where subject_id = :id"),{"id:18"}).fetchone()
    assert result is not None
    assert result == "Geo"

def test_update_subject_name():
    with engine.connect() as connection:
     # обновить название предмета
        sql = text("update subject set subject_title = :title where subject_id = :id")
        connection.execute(sql, {"id":18, "title": "GeoG"})
        connection.commit()

# проверим, что запись обновилась
result = connection.execute(text("select * from subject where subject_id = :id"),{"id:18"}).fetchone()
assert result.subject_title == "GeoG"

def test_delete_subject():
    # Удалим запись
    with engine.connect() as connection:
        sql = text("delete from subject where subject_id = :id")
        connection.execute(sql, {"id": 18, "title": "GeoG"})
        connection.commit()

    # проверим, что запись удалена
    result = connection.execute(text("select * from subject where subject_id = :id"), {"id:18"}).fetchone()
    assert result is None
