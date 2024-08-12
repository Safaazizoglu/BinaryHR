import pandas as pd


class Mass:

    def __init__(self):
        self.selectz = ""
        self.zamsL = []
        self.zamsT = []
        self.tamsL = []
        self.tamsT = []
        self.mass1T = []
        self.mass1L = []
        self.mass2T = []
        self.mass2L = []
        self.mass3T = []
        self.mass3L = []
        self.mass4T = []
        self.mass4L = []
        self.mass5T = []
        self.mass5L = []
        self.mass6T = []
        self.mass6L = []
        self.mass7T = []
        self.mass7L = []
        self.mass8T = []
        self.mass8L = []
        self.mass9T = []
        self.mass9L = []
        self.mass10T = []
        self.mass10L = []
        self.mass11T = []
        self.mass11L = []
        self.mass12T = []
        self.mass12L = []

    def opencsv(self):

        pd.read_csv(self.selectz+".csv")

    def zams(self):
        self.zamsT = pd.read_csv(self.selectz+".csv", usecols=["ZamsT"]).squeeze("columns")
        self.zamsT = list(self.zamsT)
        self.zamsL = pd.read_csv(self.selectz+".csv", usecols=["ZamsL"]).squeeze("columns")
        self.zamsL = list(self.zamsL)

    def tams(self):
        self.tamsT = pd.read_csv(self.selectz + ".csv", usecols=["TamsT"]).squeeze("columns")
        self.tamsT = list(self.tamsT)
        self.tamsL = pd.read_csv(self.selectz + ".csv", usecols=["TamsL"]).squeeze("columns")
        self.tamsL = list(self.tamsL)

    def masstracker(self):
        self.mass1T = pd.read_csv(self.selectz + ".csv", usecols=["08T"]).squeeze("columns")
        self.mass1T = list(self.mass1T)
        self.mass1L = pd.read_csv(self.selectz + ".csv", usecols=["08L"]).squeeze("columns")
        self.mass1L = list(self.mass1L)
        self.mass2T = pd.read_csv(self.selectz + ".csv", usecols=["1T"]).squeeze("columns")
        self.mass2T = list(self.mass2T)
        self.mass2L = pd.read_csv(self.selectz + ".csv", usecols=["1L"]).squeeze("columns")
        self.mass2L = list(self.mass2L)
        self.mass3T = pd.read_csv(self.selectz + ".csv", usecols=["1.2T"]).squeeze("columns")
        self.mass3T = list(self.mass3T)
        self.mass3L = pd.read_csv(self.selectz + ".csv", usecols=["1.2L"]).squeeze("columns")
        self.mass3L = list(self.mass3L)
        self.mass4T = pd.read_csv(self.selectz + ".csv", usecols=["1.4T"]).squeeze("columns")
        self.mass4T = list(self.mass4T)
        self.mass4L = pd.read_csv(self.selectz + ".csv", usecols=["1.4L"]).squeeze("columns")
        self.mass4L = list(self.mass4L)
        self.mass5T = pd.read_csv(self.selectz + ".csv", usecols=["1.6T"]).squeeze("columns")
        self.mass5T = list(self.mass5T)
        self.mass5L = pd.read_csv(self.selectz + ".csv", usecols=["1.6L"]).squeeze("columns")
        self.mass5L = list(self.mass5L)
        self.mass6T = pd.read_csv(self.selectz + ".csv", usecols=["1.8T"]).squeeze("columns")
        self.mass6T = list(self.mass6T)
        self.mass6L = pd.read_csv(self.selectz + ".csv", usecols=["1.8L"]).squeeze("columns")
        self.mass6L = list(self.mass6L)
        self.mass7T = pd.read_csv(self.selectz + ".csv", usecols=["2T"]).squeeze("columns")
        self.mass7T = list(self.mass7T)
        self.mass7L = pd.read_csv(self.selectz + ".csv", usecols=["2L"]).squeeze("columns")
        self.mass7L = list(self.mass7L)
        self.mass8T = pd.read_csv(self.selectz + ".csv", usecols=["2.2T"]).squeeze("columns")
        self.mass8T = list(self.mass8T)
        self.mass8L = pd.read_csv(self.selectz + ".csv", usecols=["2.2L"]).squeeze("columns")
        self.mass8L = list(self.mass8L)
        self.mass9T = pd.read_csv(self.selectz + ".csv", usecols=["2.5T"]).squeeze("columns")
        self.mass9T = list(self.mass9T)
        self.mass9L = pd.read_csv(self.selectz + ".csv", usecols=["2.5L"]).squeeze("columns")
        self.mass9L = list(self.mass9L)
        self.mass10T = pd.read_csv(self.selectz + ".csv", usecols=["3T"]).squeeze("columns")
        self.mass10T = list(self.mass10T)
        self.mass10L = pd.read_csv(self.selectz + ".csv", usecols=["3L"]).squeeze("columns")
        self.mass10L = list(self.mass10L)
        self.mass11T = pd.read_csv(self.selectz + ".csv", usecols=["4T"]).squeeze("columns")
        self.mass11T = list(self.mass11T)
        self.mass11L = pd.read_csv(self.selectz + ".csv", usecols=["4L"]).squeeze("columns")
        self.mass11L = list(self.mass11L)
        self.mass12T = pd.read_csv(self.selectz + ".csv", usecols=["4.5T"]).squeeze("columns")
        self.mass12T = list(self.mass12T)
        self.mass12L = pd.read_csv(self.selectz + ".csv", usecols=["4.5L"]).squeeze("columns")
        self.mass12L = list(self.mass12L)
