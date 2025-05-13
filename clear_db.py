from sqlalchemy import text
from db import SessionLocal

db = SessionLocal()
try:
    for table_name in [
        "grades",
        "subjects",
        "teachers",
        "students",
        "groups",
    ]:  # Порядок важливий!
        db.execute(text(f"DELETE FROM {table_name}"))
    db.commit()
    print("All tables deleted.")
except Exception as e:
    db.rollback()
    print(f"Error deleting data: {e}")
finally:
    db.close()
