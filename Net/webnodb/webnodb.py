from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    # 获取当前时间和主机名
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()

    # 返回纯文本内容
    return f"""
    Your Name: Peizhe <br>
    Project Name: C1 <br>
    Version: V1.2 <br>
    Hostname: {hostname} <br>
    Current Date: {current_date} <br>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
