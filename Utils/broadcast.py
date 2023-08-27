import os.path
import pickle
class Broadcast():


    def __init__(self):

        mainDir = "C:\databse"

        if not os.path.exists(mainDir):
            os.mkdir(mainDir)

        self.confFolder = mainDir



    def saveMap(self, data=False):
        temp = self.__generic_2("storage_map.pickle", data)
        if temp == "":
            return False
        return temp


    def waysMap(self, data=False):
        temp = self.__generic_2("storage_ways.pickle", data)
        if temp == "":
            return False
        return temp

    def __generic_2(self, path, data=False, folder=False):

        if folder == False:
            folder = self.confFolder

        if data != False:

            with open(folder + "/" + path, "wb") as file:
                pickle.dump(data, file)
            file.close()
            return str(data)

        else:
            try:
                with open(folder + "/" + path, "rb") as file:
                    content = pickle.load(file)
                file.close()
                return content
            except:
                return ""