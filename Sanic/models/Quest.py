import json


class Quest:
    def __init__(self, title, options, type, code, answer):
        self.title = title
        self.options = options
        self.type = type
        self.code = code
        self.answer = answer

    # 输出json
    def json(self):
        dist = {
            "title": self.title,
            "options": self.options,
            "type": self.type,
            "code": self.code,
            "answer": self.answer
        }
        return json.dumps(dist)

    # 这个方法可以用来将类的实例保存到数据库
    async def addOne(self, db):
        collection = db.quest
        return await collection.insert_one({
            "title": self.title,
            "options": self.options,
            "type": self.type,
            "code": self.code,
            "answer": self.answer,
        })

    # 通过题目查询
    @staticmethod
    async def get_by_title(db, title):
        collection = db.quest
        document = await collection.find_one({"title": title})
        if document:
            return Quest(document["title"], document["options"], document["type"], document["code"], document["answer"])
        return None

    # 通过题目，类型，答案精确查询
    @staticmethod
    async def get_by_title_type_options(db, title, type, options):
        collection = db.quest
        document = await collection.find_one({"title": title, "type": type, "options": options})
        if document:
            return Quest(document["title"], document["options"], document["type"], document["code"], document["answer"])
        return None