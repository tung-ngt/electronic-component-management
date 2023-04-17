from .utils.connect_to_db import get_connection

def create_tables():
    # Create a connection to the database
    conn, cursor = get_connection('./data/database.db')
    
    with conn:
        # create the manufacturer table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS manufacturer (
                id VARCHAR(255) PRIMARY KEY, 
                name VARCHAR(255) NOT NULL,
                country VARCHAR(255) NOT NULL, 
                image_path VARCHAR(255) NOT NULL
                );
            """
        )

        # Create table for capacitor with same value as component but with capacitance
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS capacitor (
                part_number VARCHAR(255) PRIMARY KEY,
                mnf_id VARCHAR(255) NOT NULL, 
                price REAL NOT NULL, 
                inventory_date DATE NOT NULL, 
                guarantee INT NOT NULL,
                sub_category VARCHAR(255) NOT NULL,
                stock BIGINT NOT NULL,
                image_path VARCHAR(255) NOT NULL,
                capacitance REAL NOT NULL,
                FOREIGN KEY (mnf_id) REFERENCES manufacturer(id));
            """
        )


        # Create table for resistor with same value as component but with resistance
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS resistor(
                part_number VARCHAR(255) PRIMARY KEY,
                mnf_id VARCHAR(255) NOT NULL, 
                price REAL NOT NULL, 
                inventory_date DATE NOT NULL, 
                guarantee INT NOT NULL, 
                sub_category VARCHAR(255) NOT NULL,
                stock BIGINT NOT NULL,
                image_path VARCHAR(255) NOT NULL,
                resistance REAL NOT NULL,
                FOREIGN KEY (mnf_id) REFERENCES manufacturer(id));
            """
        )

        # Create table for inductor with same value as component but with inductance
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS inductor(
                part_number VARCHAR(255) PRIMARY KEY,
                mnf_id VARCHAR(255) NOT NULL, 
                price REAL NOT NULL, 
                inventory_date DATE NOT NULL, 
                guarantee INT NOT NULL,
                sub_category VARCHAR(255) NOT NULL,
                stock BIGINT NOT NULL,
                image_path VARCHAR(255) NOT NULL,
                inductance REAL NOT NULL,
                FOREIGN KEY (mnf_id) REFERENCES manufacturer(id));
            """
        )

        # Create table for sensor with same value as component but with sensor_type
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sensor(
                part_number VARCHAR(255) PRIMARY KEY,
                mnf_id VARCHAR(255) NOT NULL, 
                price REAL NOT NULL, 
                inventory_date DATE NOT NULL, 
                guarantee INT NOT NULL,
                sub_category VARCHAR(255) NOT NULL,
                stock BIGINT NOT NULL,
                image_path VARCHAR(255) NOT NULL,
                sensor_type VARCHAR(255) NOT NULL,
                FOREIGN KEY (mnf_id) REFERENCES manufacturer(id));
            """
        )

        # Create table for IC with same value as component but with class
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS IC(
                part_number VARCHAR(255) PRIMARY KEY,
                mnf_id VARCHAR(255) NOT NULL, 
                price REAL NOT NULL,
                inventory_date DATE NOT NULL,
                guarantee INT NOT NULL,
                sub_category VARCHAR(255) NOT NULL,
                stock BIGINT NOT NULL,
                image_path VARCHAR(255) NOT NULL,
                clock REAL NOT NULL,
                FOREIGN KEY (mnf_id) REFERENCES manufacturer(id));
            """
        )
        # Create customer table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS customer(
                id VARCHAR(255) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                phone_number VARCHAR(255) NOT NULL
            );
            """
        )
        # Create order table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS orders(
                order_id VARCHAR(255) PRIMARY KEY,
                customer_id VARCHAR(255) NOT NULL,
                items JSON NOT NULL,
                date DATE NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customer(id)
            );
            """
        )