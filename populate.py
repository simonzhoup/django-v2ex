import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'v2exproject.settings')
import django
django.setup()

from v2ex.models import Category,Topic,Tag, UserProfile,User
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

def populate_post():
    '''填充帖子'''
    import requests
    import json
    url = "https://www.v2ex.com/api/topics/latest.json"
    r = requests.get(url).text
    datas = json.loads(r)
    for data in datas:
        title = data['title']
        body = data['content_rendered']
        node_name = data['node']['title']
        try:
            tag = Tag.objects.get(name=node_name)
            if tag:
                try:
                    t = Topic(title=title,body=body,tag=tag,author=random.choice(User.objects.all()))
                    t.save()
                except:
                    pass
        except:
            pass
    return 'Done'
#
def populate_users(num=20):
    '''填充用户'''
    from random import seed
    import forgery_py
    import hashlib
    seed()
    for i in range(num):
        user = User(username=forgery_py.internet.user_name(True),
                    password=forgery_py.lorem_ipsum.word(),
                    email=forgery_py.internet.email_address())
        user.save()
        user.set_password(user.password)
        user.save()
        avater_hash = hashlib.md5(user.email.encode('utf-8')).hexdigest()
        up = UserProfile(avatar_hash=avater_hash,
                         user=user)
        up.save()


if __name__ == '__main__':
    # populate_t()
    # populate_users()
    populate_post()