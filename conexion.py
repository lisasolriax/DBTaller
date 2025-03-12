def conectar():
    return mysql.connector.connect(
        host="localhost",      
        user="root",            
        password="solriax234", 
        database="dbtaller"     
    )