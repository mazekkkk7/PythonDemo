#-*- coding:utf-8 -*-
import threading

import redis
import time

conn = redis.Redis()

# conn.delete('hello')
# conn.set('hello','world')
# conn.get('hello')
# print(conn.get('hello'))
# !---------------------------------------------------------------------------------------------------------------

# conn.delete('number')
# print conn.incr('number')
# print conn.incr('number',15)
# print conn.decr('number',5)

# conn.delete('RedisStr')
# print conn.append('RedisStr','hello ')
# print conn.append('RedisStr','world!')
# print conn.substr('RedisStr',3,7)
# print conn.setrange('RedisStr',0,'H')
# print conn.setrange('RedisStr',6,'W')
# print conn.get('RedisStr')
# print conn.setrange('RedisStr',11,',how are you?')
# print conn.get('RedisStr')

# conn.delete('Bit')
# print conn.setbit('Bit',2,1)
# print conn.setbit('Bit',7,1)
# print conn.get('BitStr')

# conn.delete('ListExercise')
# print conn.rpush('ListExercise','last')
# print conn.lpush('ListExercise','first')
# print conn.rpush('ListExercise','new last')
# print conn.lrange('ListExercise',0,-1)
# print conn.lpop('ListExercise')
# print conn.lpop('ListExercise')
# print conn.lrange('ListExercise',0,-1)
# print conn.rpush('ListExercise','a','b','c')
# print conn.lrange('ListExercise',0,-1)
# print conn.ltrim('ListExercise',2,-1)
# print conn.lrange('ListExercise',0,-1)

# conn.delete('ListBlock')
# conn.delete('ListBlock2')
# print conn.rpush('ListBlock','item1')
# print conn.rpush('ListBlock','item2')
# print conn.rpush('ListBlock2','item3')
# print conn.brpoplpush('ListBlock2','ListBlock',1)
# print conn.brpoplpush('ListBlock2','ListBlock',1)
# print conn.lrange('ListBlock',0,-1)
# print conn.brpoplpush('ListBlock','ListBlock2',1)
# print conn.blpop(['ListBlock','ListBlock2'],1)
# print conn.blpop(['ListBlock','ListBlock2'],1)
# print conn.blpop(['ListBlock','ListBlock2'],1)
# print conn.blpop(['ListBlock','ListBlock2'],1)

# conn.delete('Set')
# conn.delete('Set2')
# print conn.sadd('Set','a','b','c')
# print conn.srem('Set','c','d')
# print conn.srem('Set','c','d')
# print conn.scard('Set')
# print conn.smembers('Set')
# print conn.smove('Set','Set2','a')
# print conn.smove('Set','Set2','c')
# print conn.smembers('Set2')

# conn.delete('Set3')
# conn.delete('Set4')
# print conn.sadd('Skey','a','b','c','d')
# print conn.sadd('Skey2','c','d','e','f')
# print conn.sdiff('Skey','Skey2')
# print conn.sinter('Skey','Skey2')
# print conn.sunion('Skey','Skey2')

# conn.delete('Hash')
# print conn.hmset('Hash',{'k1':'v1','k2':'v2','k3':'v3'})
# print conn.hmget('Hash',{'k2','k3'})
# print conn.hlen('Hash')
# print conn.hdel('Hash','k1','k3')

# conn.delete('Hash2')
# print conn.hmset('Hash2',{'short':'hello','long':1000*'1'})
# print conn.hkeys('Hash2')
# print conn.hvals('Hash2')
# print conn.hexists('Hash2','num')
# print conn.hincrby('Hash2','num')
# print conn.hexists('Hash2','num')

# conn.delete('ZSet')
# print conn.zadd('ZSet','a','3','b','2','c','1')
# print conn.zcard('ZSet')
# print conn.zincrby('ZSet','c',3)
# print conn.zscore('ZSet','b')
# print conn.zrank('ZSet','c')
# print conn.zcount('ZSet',0,3)
# print conn.zrem('ZSet','b')
# print conn.zrange('ZSet',0,-1,withscores=True)

# conn.delete('ZSet2')
# conn.delete('ZSet3')
# conn.delete('ZSet4')
# conn.delete('ZSet5')
# conn.delete('ZSet6')
# conn.delete('ZSet7')
# print conn.zadd('ZSet2','a',1,'b',2,'c',3)
# print conn.zadd('ZSet3','b',4,'c',1,'d',0)
# print conn.zinterstore('ZSet4',['ZSet2','ZSet3'])
# print conn.zrange('ZSet4',0,-1,withscores=True)
# print conn.zunionstore('ZSet5',['ZSet2','ZSet3'],aggregate='min')
# print conn.zrange('ZSet5',0,-1,withscores=True)
# print conn.sadd('ZSet6','a','d')
# print conn.zunionstore('ZSet7',['ZSet2','ZSet3','ZSet6'])
# print conn.zrange('ZSet7',0,-1,withscores=True)

# def publisher(n):
#     time.sleep(1)
#     for i in xrange(n):
#         conn.publish('channel', i)
#         time.sleep(1)
#

# def run_pubsub():
#     threading.Thread(target=publisher, args=(5,)).start()
#     pubsub = conn.pubsub()
#     pubsub.subscribe(['channel'])
#     count = 0
#     for item in pubsub.listen():
#         print item
#         count += 1
#         if count == 6:
#             pubsub.unsubscribe()
#         if count == 7:
#             break
#
# run_pubsub()

# conn.delete('sort-input')
# conn.delete('field')
# print conn.rpush('sort-input',23,15,110,7)
# print conn.sort('sort-input')
# print conn.sort('sort-input',alpha=True)
# print conn.hset('d-7','field',5)
# print conn.hset('d-15','field',1)
# print conn.hset('d-23','field',9)
# print conn.hset('d-110','field',3)
# print conn.sort('sort-input',by='d-*->field')
# print conn.sort('sort-input',by='d-*->field',get='d-*->field')

# 这个def demo有点问题，没有按书上预期的运行
# def notrans():
#     print conn.incr('notrans:')
#     time.sleep(.1)
#     conn.incr('notrans:',-1)
# if 1:
#     for i in xrange(3):
#         threading.Thread(target=notrans).start()
#         time.sleep(.5)

# 这个def是正常的
# def trans():
#     pipline = conn.pipeline();
#     pipline.incr('trans:')
#     time.sleep(.1)
#     pipline.incr('trans:',-1)
#     print pipline.execute()[0]
# if 1:
#     for i in xrange(3):
#         threading.Thread(target=trans).start()
#         time.sleep(.5)

# 键的过期时间
# conn.delete('key')
# print conn.set('key','value')
# print conn.get('key')
# print conn.expire('key',2)
# time.sleep(2)
# print conn.get('key')
# print conn.set('key','value2')
# print conn.expire('key',100)
# print conn.ttl('key')

# 日志处理函数
# def process_logs(conn,path,callback):
#     current_file, offset = conn.mget('progress:file','progress:position')
#     pipe = conn.pipeline()

#更新正在处理的日志文件的名字和偏移量
# def update_progress():
#     pipe.mset({
#         'progress:file':fname
#         'progress:position':offset
#     })
#     pipe.execute()

# 有序遍历日志文件
# for fname in sorted(os.listdir(path)):
#     if fname < current_file:
#         continue
#     inp = open(os.path.join(path,fname),'rb')
#     if fname == current_file:
#         inp.seek(int(offset,10))
#     else:
#         offset = 0
#
#     current_file = None
#
#     for lno, line in enumerate(inp):
#         callback(pipe,line)
#         offset += int(offset) + len(line)
#
#         if not(lno+1) % 100:
#             update_progress()
#     update_progress()
#     inp.close()

# 检查硬盘写入函数
# def wait_for_sync(mconn,sconn):
#     identifier = str(uuid.uuid4())
#     mconn.zadd('sync:wait',identifier,time.time())
#
#     while not sconn.info()['master_link_status'] != 'up'
#         time.sleep(.001)
#
#     while not sconn.zscore('sync:wait',identifier):
#         time.sleep(.001)
#
#     deadline = time.time() + 1.01
#     while time.time() < deadline:
#         if sconn.info()['aof_pending_bio_fsync'] == 0:
#             break
#         time.sleep(.001)
#
#     mconn.zrem('sync:wait',identifier)
#     mconn.zremrangebyscore('sync:wait',0,time.time()-900)

# 商品上架函数
# def list_item(conn,itemid,sellerid,price):
#     inventory = "inventory:%s" %sellerid
#     item = "%s.%s" %(itemid,sellerid)
#     end = time.time() + 5
#     pipe = conn.pipeline()
#
#     while time.time() < end:
#         try:
#             pipe.watch(inventory)
#             if not pipe.sismember(inventory,itemid):
#                 pipe.unwatch()
#                 return None
#
#             pipe.multi()
#             pipe.zadd("market:",item,price)
#             pipe.srem(inventory,itemid)
#             pipe.execute()
#             return True
#         except redis.exception.WatchError:
#             pass
#     return False

# 商品购买函数
# def purchase_item(conn,buyerid,itemid,sellerid,lprice):
#     buyer = "users:%s"%buyerid
#     seller = "users:%s"%sellerid
#     item = "%s,%s"%(itemid,sellerid)
#     inventory = "inventory:%s"%buyerid
#     end = time.time() + 10
#     pipe = conn.pipeline()
#
#     while time.time() < end:
#         try:
#             # 监控这一条数据
#             pipe.watch("market:",buyer)
#
#             price = pipe.zscore("market:",item)
#             funds = int(pipe.hget(buyer,"funds"))
#             if price != lprice or price > funds:
#                 pipe.unwatch()
#                 return None
#             pipe.multi()
#             pipe.hincrby(seller,"funds",int(price))
#             pipe.hincrby(buyer,"funds",int(-price))
#             pipe.sadd(inventory,itemid)
#             pipe.zrem("market:",item)
#             pipe.execute()
#             return True
#         except redis.exceptions.WatchError:
#             pass
#
#     return False

# 函数是第一张给出的例子未实现
# def update_token(conn,token,user,item=None):
#     pass

# 使用流水线来处理与Redis的交互次数提升效率
# def update_token_pipeline(conn,token,user,item=None):
#     timestamp = time.time()
#     pipe = conn.pipeline(False)
#     pipe.hset('login:',token,user)
#     pipe.zadd('recent:',token,timestamp)
#     if item:
#         pipe.zadd('viewed:' + token,item,timestamp)
#         pipe.zremrangebyrank('viewed:' + token,0,-26)
#         pipe.zincrby('viewed:',item,-1)
#     pipe.execute()

# 批量测试函数
# def benchmark_update_token(conn,duration):
#     for function in (update_token,update_token_pipeline):
#         count = 0
#         start = time.time()
#         end = start + duration
#         while time.time() < end:
#             count+=1
#             function(conn,'token','user','item')
#         delta = time.time() - start
#         print function.__name__,count,delta,count/delta
# SEVERITY = {
#     logging.DEBUG: 'debug',
#     logging.INFO: 'info',
#     logging.WARNING: 'warning',
#     logging.ERROR: 'error',
#     logging.CRITICAL: 'critical',
# }
# SERVERITY.update((name,name) for name in SEVERITY.values())
# 记录最新日志
# def log_recent(conn,name,message,serverity=logging.INFO,pipe=None):
#     serverity = str(SEVERITY.get(serverity,serverity)).lower()
#     destination = 'recent:%s:%s'%(name,serverity)
#     message = time.asctime() + ' ' + message
#     pipe = pipe or conn.pipeline()
#     pipe.lpush(destination,message)
#     pipe.ltrim(destination,0,99)
#     pipe.execute()
# 常见日志
# def log_common(conn,name,message,serverity=logging.INFO,timeout=5):
#     serverity = str(SEVERITY.get(serverity,serverity)).lower()
#     destination = 'common:%s:%s'%(name,serverity)
#     start_key = destination + ' :start'
#     pipe = conn.pipeline()
#     end = time.time() + timeout
#     while time.time() < end:
#         try:
#             pipe.watch(start_key)
#             now = datetime.utcnow().timetuple()
#             hour_start = datetime(*now[:4]).isoformat()
#
#             existing = pipe.get(start_key)
#             pipe.multi()
#             if existing and existing < hour_start:
#                 pipe.rename(destination,destination + ' :last')
#                 pipe.rename(start_key,destination + ' :pstart')
#                 pipe.set(start_key,hour_start)
#             elif not existing:
#                 pipe.set(start_key,hour_start)
#             pipe.zincrby(destination,message)
#             log_recent(pipe,name,message,serverity,pipe)
#             return
#         except redis.exceptions.WatchError:
#             continue
# 更新计数器
# PRECISION = [1,5,60,300,3600,18000,86400]
# def update_counter(conn,name,count=1,now=None):
#     now = now or time.time()
#     pipe = conn.pipeline()
#     for prec in PRECISION:
#         pnow = int(now / prec) * prec
#         hash = '%s:%s' %(prec,name)
#         pipe.zadd('know:',hash,0)
#         pipe.hincrby('count:' + hash,pnow,count)
#     pipe.execute()

