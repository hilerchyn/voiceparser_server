from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/voiceparser/api', methods=['POST', 'GET'])
def voiceparser_api():
    voice = request.files['voice_file']
    voice.save("D:\\work\\voiceparser\\python\\" + voice.filename)
    print("接收文件成功")
    return jsonify({"message": "##服务器端解析成功##"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
