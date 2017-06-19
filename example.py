# How to use

from fanfousdk import Fan, Config


# 1. Subclass the ``Config`` class and offer your configs
class MyConfig(Config):
    consumer_key = 'xxxx'
    consumer_secret = 'xxxx'


# 2. Instancialize the ``Fan`` class
me = Fan(MyConfig())
# 3. call methods of ``fan``
me.update_status('你好啊，李银河！')
