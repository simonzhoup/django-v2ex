import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'v2exproject.settings')
import django
django.setup()

from v2ex.models import Category,Topic,Tag
# import requests
# import json
# from time import sleep

#
# def populate_c():
#     '''填充tag'''
#     cs = ['技术','创意','好玩','Apple','酷工作','交易','城市','问与答','最热','全部','节点关注']
#     for t in cs:
#         c = Category(name=t,info='')
#         c.save()
#     return 'Done'

def populate_t():
    '''填充节点'''
    data = {
        '技术':['程序员','Python','iDev','Android','Linux','node.js','云计算','宽带症候群'],
        '创意':['分享创造','设计','奇思妙想'],
        '好玩':['分享发现','电子游戏','电影','剧集','音乐','旅游','午夜俱乐部'],
        'Apple':['macOS','iPhone','iPad','MBP','iMac','WATCH','Apple'],
        '酷工作':['酷工作','求职','职场话题','外包'],
        '交易':['二手交易','物物交换','免费赠送','域名','团购','安全提示'],
        '城市':['北京','上海','深圳','广州','杭州','成都','昆明','纽约','杉矶'],
        '问与答':['问与答'],
        # '全部':['分享发现','分享创造','问与答','酷工作','程序员','职场话题','奇思妙想','优惠信息']
    }
    for t in data.keys():
        c = Category.objects.get_or_create(name=t)[0]
        for n in data[t]:
            t = Tag.objects.get_or_create(name=n)[0]
            t.category = c
            t.save()
    return 'Done'

# def populate_post():
#     '''填充帖子'''
#     url = "https://www.v2ex.com/api/topics/latest.json"
#     r = requests.get(url).text
#     datas = json.loads(r)
#     for data in datas:
#         title = data['title']
#         content = data['content_rendered']
#         node_name = data['node']['title']
#         node = Node.query.filter_by(name=node_name).first()
#         if node:
#             p = Post(title=title,content=content,node=node,author=random.choice(User.query.all()))
#             db.session.add(p)
#             db.session.commit()
#     return 'Done'
#
# def populate_users(num=20):
#     '''填充用户'''
#     for i in range(num):
#         url = 'https://randomuser.me/api/'
#         r = requests.get(url).text
#         data = json.loads(r)
#         username = data['results'][0]['login']['username']
#         password = data['results'][0]['login']['password']
#         email = data['results'][0]['email']
#         avatar = data['results'][0]['picture']['large']
#         user = User(username=username,password=password,email=email,avatar=avatar)
#         db.session.add(user)
#         db.session.commit()
#         sleep(2)
#     return 'Done'

if __name__ == '__main__':
    populate_t()