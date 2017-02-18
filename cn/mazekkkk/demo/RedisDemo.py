import redis
conn = redis.Redis()
conn.set('hello','world')
conn.get('hello')
print(conn.get('hello'))