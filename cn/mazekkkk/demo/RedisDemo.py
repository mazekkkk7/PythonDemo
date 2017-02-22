import threading

import redis
import time

conn = redis.Redis()

# conn.delete('hello')
# conn.set('hello','world')
# conn.get('hello')
# print(conn.get('hello'))
#!---------------------------------------------------------------------------------------------------------------
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

def publisher(n):
    time.sleep(1)
    for i in xrange(n):
        conn.publish('channel',i)
        time.sleep(1)
def run_pubsub():
    threading.Thread(target=publisher,args=(5,)).start()
    pubsub = conn.pubsub()
    pubsub.subscribe(['channel'])
    count = 0
    for item in pubsub.listen():
        print item
        count += 1
        if count == 6:
            pubsub.unsubscribe()
        if count == 7:
            break

run_pubsub();