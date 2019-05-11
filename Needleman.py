class Needleman:
    def __init__(self, match, mis_match, gap):
        self.dna1 = ''
        self.dna2 = ''
        self.match = match
        self.mis_match = mis_match
        self.gap = gap
        self.gap_list = []
        self.l_val_list = []
        self.u_val_list = []
        self.length = 0

    def set_dna(self, dna1, dna2):
        self.dna1 = dna1
        self.dna2 = dna2
        self.length = len(dna1) + 1

    def __create_list(self, arr):
        temp_row = [x * self.gap for x in range(self.length)]
        arr.append(temp_row)
        for i in range(1, self.length):
            arr.append([arr[i - 1][0] + self.gap])

    def __comp_l_val_list(self):
        # l_val_list' in kalan değerlerini tamamlıyor
        for i in range(1, len(self.l_val_list)):
            for j in range(1, len(self.l_val_list[0])):
                left_value = self.l_val_list[i][0] + self.gap * j
                self.l_val_list[i].append(left_value)

    def __comp_u_val_list(self):
        # u_val_list' in kalan değerlerini tamamlıyor
        for i in range(1, len(self.u_val_list)):
            for j in range(1, len(self.u_val_list[0])):
                up_value = self.gap_list[0][j] + self.gap * i
                self.u_val_list[i].append(up_value)

    def gap_list_create(self):
        self.__create_list(self.gap_list)

    def l_val_list_create(self):
        self.__create_list(self.l_val_list)
        self.__comp_l_val_list()

    def u_val_list_create(self):
        self.__create_list(self.u_val_list)
        self.__comp_u_val_list()

    def calculate(self):
        for i in range(1, self.length):
            for j in range(1, self.length):
                left_value = self.l_val_list[i][j]
                up_value = self.u_val_list[i][j]
                if self.dna2[i - 1] == self.dna1[j - 1]:
                    match_val = self.match
                else:
                    match_val = self.mis_match
                val = left_value + up_value + match_val + self.gap_list[i - 1][j - 1]
                self.gap_list[i].append(val)

    def get_score(self):
        return self.gap_list[self.length - 1][self.length - 1]


