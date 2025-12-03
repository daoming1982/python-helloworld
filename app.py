from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash # 用于密码加密

app = Flask(__name__)

# --- 数据库配置 ---
# 使用 SQLite 数据库，文件名为 'codex.db'，存放在项目根目录
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///codex.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- 数据库模型 (Models) ---
# 定义一个用户表
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    def set_password(self, password):
        """用 werkzeug 对密码进行哈希加密并存储"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """验证密码"""
        return check_password_hash(self.password_hash, password)

# --- 路由 (Routes) ---

# 基础测试路由 (首页)
@app.route("/")
def hello_world():
    return render_template("index.html")

# 数据展示路由
@app.route("/data")
def show_data():
    # ... (您的模拟数据代码保持不变) ...
    cocoa_batches = [
        {"id": "YNC-001", "origin": "云南普洱", "fermentation_days": 6, "weight": 150.5, "status": "已烘烤"},
        {"id": "YNC-002", "origin": "云南西双版纳", "fermentation_days": 7, "weight": 120.0, "status": "待发酵"},
    ]
    return render_template("data_table.html", batches=cocoa_batches)

# 登录路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            # 登录成功，重定向到数据页
            return redirect(url_for('show_data'))
        else:
            # 登录失败，重新显示登录页并显示错误信息
            error = '无效的用户名或密码'
            return render_template('login.html', error_message=error)
            
    return render_template('login.html')

# 注册路由 (方便测试，后续可删除)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # 检查用户是否已存在
        if User.query.filter_by(username=username).first():
            return render_template('login.html', error_message='用户已存在')
            
        # 创建新用户并加密密码
        new_user = User(username=username)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login')) # 注册成功后跳转到登录页
        
    # 为了方便，注册和登录共用一个模板，但实际应用中应该有单独的注册页
    return render_template('login.html')