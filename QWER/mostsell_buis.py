def formatR(qry1, qry2, num=None):
    qry2.sort(key=lambda x: x[2])
    a = 0

    qry2 = qry2[:num]
    dic1 = {}
    for i in qry2:
        dic1[qry1[a][1]] = str(i[1] * i[2]) + " " + str(i[2])
        a += 1
    dic2 = "<br>".join(" ".join((k, v)) for (k, v) in dic1.items())

    return dic2
