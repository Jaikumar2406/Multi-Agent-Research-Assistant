from .get_db_connection import get_db_connection

def save_message(thread_id, role, content):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO chat_history (thread_id, role, content) VALUES (%s, %s, %s)",
        (thread_id, role, content)
    )

    conn.commit()
    cur.close()
    conn.close()
