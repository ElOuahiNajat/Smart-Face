import cv2
import numpy as np
import mysql.connector
from mysql.connector import Error

def connect_to_database(host, database, user, password):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
    return None

def fetch_images_from_database(connection, table_name):
    images = []
    ids_names = []
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT id, nom, IMAGE FROM {table_name}")  # Updated column name to 'IMAGE'
        for person_id, nom, image_data in cursor.fetchall():
            nparr = np.frombuffer(image_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            images.append(img)
            ids_names.append((person_id, nom))
    except Error as e:
        print(f"Error fetching images from the database: {e}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
    return images, ids_names
