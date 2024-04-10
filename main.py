from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    # 接收来自 PHP 服务器的请求
    request_data = request.get_json()

    # 处理请求数据
    message_from_php = request_data['message']
    processed_data = message_from_php.upper()  # 示例处理方式：将收到的消息转换为大写

    #判断使用的加密机或者服务方式并且运行相应的app.py文件
    #通用服务器密码机
    # 指定其他项目文件夹中的app.py路径
    if processed_data=="GVSM":
        app_py_path =r'..\GVSM\app.py'
        # 指定虚拟环境中Python解释器的路径
        python_interpreter_path = r"..\GVSM\Scripts\python.exe"
        # 使用subprocess模块运行app.py文件
        processed_data = "ok"
        process = subprocess.Popen([python_interpreter_path, app_py_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 获取标准输出和标准错误输出
        #stdout, stderr = process.communicate()
        # print("标准输出:", stdout.decode())
        # print("标准错误输出:", stderr.decode())
        print("ok")
    # 返回响应给 PHP 服务器
    response_data = {
        'processed_message': processed_data
    }
    return jsonify(response_data)

if __name__ == '__main__':
    # 仅监听特定的 IP 地址
    app.run(host='127.0.0.1', port=6000)  # 将 host 参数设置为特定的 IP 地址