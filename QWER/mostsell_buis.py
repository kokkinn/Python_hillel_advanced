from QWER.conn import execute_query
from pprint import pprint

#
# #
# sql1 = execute_query("select Trackid, Name from tracks")
# sql2 = execute_query("select trackid, unitprice, quantity from invoice_items")
# #
# num = 4
def formatR(qry1, qry2, num=None):
    qry2.sort(key=lambda x: x[2])
    a = 0
    # qry2 = [list(x) for x in qry2]
    qry2 = qry2[:num]
    dic1 = {}
    for i in qry2:
        dic1[qry1[a][1]] = str(i[1] * i[2]) + " " + str(i[2])
        a += 1
    dic2 = "<br>".join(" ".join((k, v)) for (k, v) in dic1.items())

    # qry2 = tuple([tuple(x) for x in qry2])
    # u = " ".join(qry2)

    # x = "<br>".join(qry2)
    return dic2
#
# print(formatR(sql1, sql2, 4))

# print(formatR(sql1, sql2, num))
