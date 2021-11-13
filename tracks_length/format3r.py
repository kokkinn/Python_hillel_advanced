from tracks_length.trc_ln_buis import execute_query


def form7t2(tracks_tbl, genres_tbl):                    #первый способ, с двумя запросами, все полностью сырое
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
def form7t(genre_tab):
    dic1 = {}                                       #тут - как вы посоветовали
    summ = 0
    for i in genre_tab:
        dic1[i[1]] = 0
        x = execute_query(f'SELECT Milliseconds FROM tracks WHERE GenreId = {i[0]}')
        for f in x:
            summ += f[0]
        dic1[i[1]] = summ
        summ = 0
    for key, value in dic1.items():
        dic1[key] = str(round(dic1[key] / 1000))
    x = '<br>'.join(' '.join((key, val)) for (key, val) in dic1.items())
    return x
