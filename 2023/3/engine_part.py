import string


class EnginePart:
    def __init__(self, partno, rownum, colstart, schemrow, prevrow, nextrow):
        self.partno = partno
        self.partnum = int(partno)
        self.rownum = rownum
        self.colstart = colstart
        self.colend = self.colstart + len(partno) - 1
        self.schemrow = schemrow
        self.prevrow = prevrow
        self.nextrow = nextrow
        self.part = False

    def check_if_part(self) -> bool:
        if self.schemrow[self.colstart-1] != '.':
            self.part = True
            # print(self.partno, " is valid")
            return True
        if self.schemrow[self.colend+1] != '.':
            self.part = True
            # print(self.partno, " is valid")
            return True
        for col in self.prevrow[self.colstart-1:self.colend+2]:  # Look up
            if col not in string.digits and col != '.':
                self.part = True
                # print(self.partno, " is valid")
                return True
        for col in self.nextrow[self.colstart-1:self.colend+2]:  # Look down
            if col not in string.digits and col != '.':
                self.part = True
                # print(self.partno, " is valid")
                return True
        # print(self.partno, " is not a valid part.\n-----")
        self.part = False
        return False
