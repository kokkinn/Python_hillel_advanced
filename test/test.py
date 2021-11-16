import os
import time

# делаем папку
os.mkdir("C:\\Users\\kokki\\Desktop\\wefwfwweg")
# создаем путь для сохранения
savepath = "C:\\Users\\kokki\\Desktop\\wefwfwweg"
filename = 'file.txt'
completepath = os.path.join(savepath, filename)
# создаем файл
filedo = open(completepath, "x")
# пишем
filedo.write("My name isnt George")
filedo.close()
time.sleep(5)
# удаляем
os.remove("C:\\Users\\kokki\\Desktop\\wefwfwweg\\file.txt")
os.rmdir("C:\\Users\\kokki\\Desktop\\wefwfwweg")


os.mkdir("C:\\Users\\kokki\\Desktop\\DIR1")
os.mkdir("C:\\Users\\kokki\\Desktop\\DIR2")
fileopen = open("C:\\Users\\kokki\\Desktop\\DIR1\\FILE100", "x")
fileopen.close()
os.rename("C:\\Users\\kokki\\Desktop\\DIR1\\FILE100", "C:\\Users\\kokki\\Desktop\\DIR2\\FILE100")