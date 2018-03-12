import os
import time
import codecs


class ShowDirs:
    def __init__(self, mode):
        self.dir = os.path.curdir + "/"
        self.writefile(mode)

    def writefile(self, mode):
        n = 1
        if(mode == "list"):
            with open("arquivos-neste-diretorio.txt", "w", encoding="utf-8") as textfile:
                for directory in os.listdir(self.dir):
                    textfile.write(
                        str(n).ljust(5, " ") +
                        directory.ljust(70, " ") +
                        str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getmtime(self.dir + directory)))) + "\r\n")
                    n = n + 1
        elif(mode == "csv"):
            with open("arquivos-neste-diretorio.csv", "w", encoding="utf-8") as textfile:
                for directory in os.listdir(self.dir):
                    textfile.write(
                        str(n) + "," +
                        directory + "," +
                        str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getmtime(self.dir + directory)))) + "\r\n")
                    n = n + 1
        else:
            pass
