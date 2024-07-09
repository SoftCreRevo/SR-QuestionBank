import sanic.response

from Sanic.models.Quest import Quest


# OCS脚本的题库延迟测试功能
async def OCS_test_delay(request):
    # TODO 功能待补充
    q_data = request.json

# 题目的精准搜索
async def get_quest_precision(request):
    q_data = request.json
    quest = Quest(q_data['title'], q_data['options'], q_data['type'], 1, '无')
    findResult = await quest.get_by_title_type_options(request.app.ctx.db, q_data['title'], q_data['type'], q_data['options'])
    if findResult:
        count = 1
        print("查询成功！\n题目：{0}\n类型：{1}".format(findResult.title,findResult.type))
        for item in findResult.options.split("\n"):
            print("选项{0}：".format(count)+item)
            count += 1
        print("答案："+findResult.answer)
        return sanic.response.text(findResult.json())
    else:
        print("查询失败！\n添加题目到题库中！..............")
        if await quest.addOne(request.app.ctx.db):
            print("添加成功！")
            # 将状态码置零以确保状态正确
            quest.code = 0
            return sanic.response.text(quest.json())
