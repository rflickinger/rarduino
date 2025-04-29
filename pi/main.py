import time
from db import get_connection, init_db, insert_temp
from arduino_comm import read_temp_from_serial

def main():
    conn = get_connection()
    init_db(conn)

    try:
        while True:
            temp = read_temp_from_serial()
            if temp is not None:
                print(f"Read temp: {temp}")
                insert_temp(conn, temp)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        conn.close()

if __name__ == '__main__':
    main()