from flask import Flask,request
import socket
from datetime import datetime
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)


db = client["flask_app_db"]  # 数据库名称
collection = db["project_info"]  # 集合名称

@app.route('/')
def hello_world():
    # 获取当前时间和主机名
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    client_ip = request.remote_addr  # 获取访问者的 IP 地址
    
    collection.insert_one({"client_ip": client_ip,"date": current_date})
    recent_records = list(collection.find().sort("_id", -1).limit(10))

    records_table = "<table border='1'>"
    records_table += "<tr><th>IP Address</th><th>Access Time</th></tr>"
    for record in recent_records:
        records_table += f"<tr><td>{record['client_ip']}</td><td>{record['date']}</td></tr>"
    records_table += "</table>"
    # 返回纯文本内容
    return f"""
    Your Name: Peizhe <br>
    Project Name: C1 <br>
    Version: V2.2 <br>
    Hostname: {hostname} <br>
    Current Date: {current_date} <br>
    Recent Access Records:<br>
    {records_table}
    """
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
