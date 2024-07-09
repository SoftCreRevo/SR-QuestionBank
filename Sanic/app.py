from motor.motor_asyncio import AsyncIOMotorClient
from sanic import Sanic

from Sanic.config import Config
from Sanic.routes.quest_http import get_quest_precision

app = Sanic("QuestionBank_Sanic")

# 在应用的配置中设置数据库连接
app.config.DB_URI = "mongodb://{0}:{1}@{2}".format(Config.Mongodb.username, Config.Mongodb.password, Config.Mongodb.db_host)
app.config.DB_NAME = "request"

# 导入路由
app.add_route(get_quest_precision, '/q/precision', methods=['POST'])


# 初始化数据库客户端
@app.listener("before_server_start")
async def init_db(app, loop):
    app.ctx.db = AsyncIOMotorClient(app.config.DB_URI, io_loop=loop)[app.config.DB_NAME]

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
