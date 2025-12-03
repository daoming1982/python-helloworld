from flask import Flask

# 创建 Flask 应用实例
app = Flask(__name__)

# 定义第一个路由：首页
@app.route("/")
def hello_world():
    # 返回 Hello World 字符串
    return "<p>Hello, World! - Codex Chocolate Test</p>"

# 启动服务器 (仅在直接运行此文件时执行)
if __name__ == '__main__':
    # debug=True 开启调试模式，代码修改后服务器会自动重启
    app.run(debug=True)