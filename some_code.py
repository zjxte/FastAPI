# while True:   
#     try:
#         conn = pymssql.connect(server='DXCH4TSTEST2A', user='SSRS', password='Ts4test@', database='atlasone')
#         cursor = conn.cursor()
#         print("Database connection was succesful!")    
#         break
#     except Exception as e:
#         print("Connecting to database failed - ", e)
#         time.sleep(2)
