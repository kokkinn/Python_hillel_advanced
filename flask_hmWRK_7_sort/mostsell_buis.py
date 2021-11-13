# from flask_hmWRK_6_trckLength.trc_ln_buis import execute_query
#
# sql1 = execute_query("select Trackid, Name from tracks")
# sql2 = execute_query("select trackid, unitprice, quantity from invoice_items")
# num = 4
#

def formatR(qry1, qry2, num=None):
    qry2.sort(key=lambda x: x[2])
    a = 0

    qry2 = qry2[:num]
    # dic1 = {}
    # for i in qry2:
    #     dic1[qry1[a][1]] = str(i[1] * i[2]) + " " + str(i[2])
    #     a += 1
    # dic2 = "<br>".join(" ".join((k, v)) for (k, v) in dic1.items())
    qr = [list(i) for i in qry2]
    a = 0
    for f in qr:
        f[0] = qry1[a][1]
        f[1] = f[1] * f[2]
        f[2] = f[2]
        a += 1

    x = "<br>".join(map(lambda x: str(x[0]) + ' ' + str(x[1]) + " " + str(x[2]), qr))
    return x
    # return dic2

# print(formatR(sql1, sql2, num))