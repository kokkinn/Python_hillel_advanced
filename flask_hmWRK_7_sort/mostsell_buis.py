def formatR(qry1, qry2, num=None):
    qry2.sort(key=lambda zx: zx[2])
    a = 0
    qry2 = qry2[:num]

    # dic1 = {}
    # for i in qry2:
    #     dic1[qry1[a][1]] = str(i[1] * i[2]) + " " + str(i[2])         #другой способ
    #     a += 1
    # dic2 = "<br>".join(" ".join((k, v)) for (k, v) in dic1.items())

    qr = [list(i) for i in qry2]
    for f in qr:
        f[0] = qry1[a][1]
        f[1] = f[1] * f[2]
        f[2] = f[2]
        a += 1

    x = "<br>".join(map(lambda y: str(y[0]) + ' ' + str(y[1]) + " " + str(y[2]), qr))
    return x
