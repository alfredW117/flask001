import psycopg2
def obtener_conexion():
    conn = psycopg2.connect(host='ec2-54-211-177-159.compute-1.amazonaws.com', port=5432, database='deknsbnj96nntp', user='pteruwyudmayqr', password='57eee1504c786de6cc0e993a2dad48aca0dbdfbeb115b0d0e66c34dea1c16899')
    if conn is None:
        print('Error connecting')
    else:
        print('Connection established')
    return conn

"""if __name__ == '__main__':
obtener_conexion()"""
