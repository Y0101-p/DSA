class Spreadsheet:

    def __init__(self, rows: int):
        self.list=[[0]*rows for _ in range(26)]
        self.rows=rows
 
    def setCell(self, cell: str, value: int) -> None:
        s=ord(cell[0])-65
        num=int(cell[1:])-1
        self.list[s][num]=value
    def resetCell(self, cell: str) -> None:
        s=ord(cell[0])-65
        num=int(cell[1:])-1
        self.list[s][num]=0
    def getValue(self, formula: str) -> int:
        def returnvalue(a:str)-> int:
            if a[0].isnumeric():
                return int(a)
            else:
                s=ord(a[0])-65
                num=int(a[1:])-1
                try:
                    return self.list[s][num]
                except IndexError:
                    return 0   
        x,y=formula.split('+')
        x=x[1:]
        return returnvalue(x)+returnvalue(y)