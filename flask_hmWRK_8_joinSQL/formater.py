def formater(sql, num=None):
    sql = sql[:num]
    a = '<br>'.join(map(lambda x: str(x[0]) + ' ' + str(x[1]) + " " + str(x[2]), sql))
    return a


def formater2(sql):
    a = '<br>'.join(map(lambda x: str(x[0]) + ' ' + str(x[1]), sql))
    return a
