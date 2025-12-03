from flask import Flask

# 1. 确保应用实例的变量名为 'app'
app = Flask(__name__)

# 定义第一个路由：首页
@app.route("/")
def hello_world():
    # 返回 Hello World 字符串
    return "<p>Hello, World! - Codex Chocolate Test</p>"

# 2. 移除或注释掉这里的运行代码块，由调试器负责启动
# if __name__ == '__main__':
#     # app.run(debug=True)
#     pass