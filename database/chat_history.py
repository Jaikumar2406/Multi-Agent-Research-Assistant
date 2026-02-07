from .get_db_connection import get_db_connection

def get_chat_history(thread_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT role, content FROM chat_history WHERE thread_id=%s ORDER BY id",
        (thread_id,)
    )

    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows
