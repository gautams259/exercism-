class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix=matrix_string.split('\n')
        #['9 8 7', ' 5 3 2 ', '6 6 7']
        self.rows=[]
        for i in self.matrix:
            r=i.split(' ')
            r=[int(i) for i in r]
            self.rows.append(r)

    def row(self, index): 
        return self.rows[index-1]

    def column(self, index):
        col=[]
        for i in range(0,len(self.rows[0])):
            c=[]
            for j in range(0,len(self.rows)):
                c.append(self.rows[j][i])
            #print(c,"col")
            col.append(c)
        return col[index-1]


def main():
    m="1 2 3\n4 6 7\n8 9 1"
    print m
    index = 2
    ob = Matrix(m)
    print(ob.row(index))
    print(ob.column(index))


if __name__ == '__main__':
    #main()
    pass
