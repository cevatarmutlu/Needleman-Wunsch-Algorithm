class MyFasta:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.__file = ''
        self.line_list = []
        self.__create_list()

    def __open_fasta(self):
        path = 'sekanslar/' + self.file_name + '.fasta'
        return open(path, 'r')

    def __create_list(self):
        f = self.__open_fasta()

        for line in f.readlines():
            line = self.__is_line(line)
            if line != '':
                self.line_list.append(line)

    def __is_line(self, line):
        if line == '\n':
            return ''
        elif line[0] == '>':
            return ''
        else:
            line = line[1:]
            line = line.splitlines()[0]
            return line

    def get_list(self):
        return self.line_list


