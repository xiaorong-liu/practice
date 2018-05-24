from rediscluster import StrictRedisCluster


# gitignore忽略文件
if __name__ == '__main__':
    try:
        # 构建所有的节点，Redis会使⽤CRC16算法，将键和值写到某个节点上
        startup_nodes = [
            {'host': '192.168.47.141', 'port': '7000'},
            {'host': '192.168.47.141', 'port': '7001'},
            {'host': '192.168.47.141', 'port': '7002'},
        ]
        # 构建StrictRedisCluster对象
        src = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
        # 设置键为name、值为 itheima 的数据
        result = src.set('name', 'itheima')
        print(result)
        # 获取键为name
        name = src.get('name')
        print(name)
    except Exception as e:
        print(e)


