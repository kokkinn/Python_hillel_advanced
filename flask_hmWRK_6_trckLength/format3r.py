def form7t(tracks_tbl, genres_tbl):
    dic1 = {}
    for genid in range(1, len(genres_tbl) + 1):
        for tuplee in tracks_tbl:
            if tuplee[0] == genid:
                if genres_tbl[genid - 1][1] not in dic1:
                    dic1[genres_tbl[genid - 1][1]] = tuplee[1]
                else:
                    dic1[genres_tbl[genid - 1][1]] += tuplee[1]
    for key, value in dic1.items():
        dic1[key] = str(round(dic1[key] / 1000))
    x = '<br>'.join(' '.join((key, val)) for (key, val) in dic1.items())
    return x


