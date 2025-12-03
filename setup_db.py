import os
from app import app, db, User

# -----------------------------------------------------------
# 目的：在不依赖Shell命令的情况下，直接创建数据库和测试用户
# -----------------------------------------------------------

# 确保在应用的上下文中运行
with app.app_context():
    print("--- 正在初始化 Codex 数据库 ---")
    
    # 1. 创建数据库文件和表结构
    db.create_all()
    print("✔ 数据库表结构已创建或已存在。")
    
    # 2. 创建一个测试用户 (如果不存在)
    if not User.query.filter_by(username='daoming').first():
        test_user = User(username='daoming')
        test_user.set_password('codex123') # 测试密码：codex123
        db.session.add(test_user)
        db.session.commit()
        print("✔ 测试用户 'daoming' 已创建，密码是 'codex123'。")
    else:
        print("✔ 测试用户已存在，跳过创建。")

print("--- 数据库初始化完成 ---")