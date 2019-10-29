class SepParser:
    def __init__(self, sep=','):
        self.sep = sep 

    def parse_line(self, line, types):
        contents = line.split(self.sep)
        res = [t(c) for t, c in zip(types, contents)]
        return res
    
    def parse_file(self, fp, types, header=False):
        contents = []
        passed_header = False
        for line in fp:
            if not header or passed_header:
                contents.append(self.parse_line(line, types))
        return contents

    
