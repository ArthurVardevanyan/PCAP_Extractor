import pymysql


def MYSQL_Login(login):
    try:
        return pymysql.connect(login[0], login[1], login[2], login[3])
    except:
        print("Wrong Credentials")


def MYSQL_Data_Import(data, db):  # Import Data from MYSQL databse into Program
    # Super Secure Username & Password
    cursor = db.cursor()
    cursor.execute("SELECT * FROM " + data + ";")
    result = cursor.fetchall()
    listResult = [list(item) for item in result]
    cursor.close()
    db.commit()
    db.close()
    return listResult


def MYSQL_DB_ED(Edata, db):  # Writes the data to the MYSQL database from the program

    cursor = db.cursor()
    try:
        cursor.execute("drop table edata;")
    except:
        print("No Table")

    data = map(lambda col: {'Address': col[0],
                            'Packets': col[1],
                            'Bytes': col[2],
                            'Tx_Packets': col[3],
                            'Tx_Bytes': col[4],
                            'Rx_Packets': col[5],
                            'Rx_Bytes': col[6],
                            'First_Seen': col[7],
                            'Last_Seen': col[8],
                            "Organization": col[9],
                            "Country": col[10],
                            "Region": col[11],
                            "City": col[12],
                            },
               Edata[0: len(Edata)])

    cursor.execute("CREATE TABLE edata( Address VARCHAR(20), Packets BIGINT, Bytes BIGINT, Tx_Packets BIGINT, Tx_Bytes BIGINT, Rx_Packets  BIGINT, Rx_Bytes BIGINT, First_Seen VARCHAR(20), Last_Seen VARCHAR(20), Organization LONGTEXT, Country VARCHAR(20), Region LONGTEXT, City VARCHAR(20), PRIMARY KEY (Address));")
    query = """INSERT INTO edata (Address, Packets, Bytes, Tx_Packets, Tx_Bytes, Rx_Packets, Rx_Bytes, First_Seen, Last_Seen, Organization, Country, Region, City) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    for row in data:
        values = (row['Address'], row['Packets'], row['Bytes'], row['Tx_Packets'], row['Tx_Bytes'], row['Rx_Packets'],
                  row['Rx_Bytes'], row['First_Seen'], row['Last_Seen'], row['Organization'], row['Country'], row['Region'], row['City'])
        cursor.execute(query, values)
    cursor.close()
    db.commit()
    db.close()


def MYSQL_DB_CD(CData, db):

    cursor = db.cursor()
    try:
        cursor.execute("drop table cdata;")
    except:
        print("No Table")

    data = map(lambda col: {'Address_A': col[0],
                            'Address_B': col[1],
                            'Packets_A_B': col[2],
                            'Bytes_A_B': col[3],
                            'Packets_B_A': col[4],
                            'Bytes_B_A': col[5],
                            'Packets': col[6],
                            'Bytes': col[7],
                            'First_Seen': col[8],
                            'Last_Seen': col[9],
                            },
               CData[0: len(CData)])
    cursor.execute("CREATE TABLE cdata(Address_A VARCHAR(20),  Address_B VARCHAR(20),  Packets_A_B BIGINT,  Bytes_A_B BIGINT,  Packets_B_A BIGINT,  Bytes_B_A BIGINT,  Packets BIGINT,  Bytes BIGINT, First_Seen VARCHAR(20), Last_Seen VARCHAR(20));")
    query = """INSERT INTO cdata ( Address_A, Address_B, Packets_A_B, Bytes_A_B, Packets_B_A, Bytes_B_A, Packets, Bytes, First_Seen, Last_Seen) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    for row in data:
        values = (row['Address_A'], row['Address_B'], row['Packets_A_B'], row['Bytes_A_B'], row['Packets_B_A'],
                  row['Bytes_B_A'], row['Packets'], row['Bytes'], row['First_Seen'], row['Last_Seen'])
        cursor.execute(query, values)
    cursor.close()
    db.commit()
    db.close()
