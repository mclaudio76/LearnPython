class SqlQuery:
    
    def __init__(self,sqlbase, connection):
        self.sqlbase = sqlbase
        self.connection = connection 
        self.parameters = list()
        self.pValues    = list()
    
    def addConstraint(self, columnName, operator, value, omitConstraintValue=None):
        self.parameters.append( (columnName, operator, value, omitConstraintValue))

    def prepare(self):
        self.sqlbase += ' WHERE 1=1 '
        for t in self.parameters:
            columnName, operator, value, omitConstraintValue  = t
            if value != omitConstraintValue:
                self.sqlbase += "AND "+columnName+" "+operator+" %s"
                self.pValues.append(value)
        actualParams = tuple(self.pValues)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.sqlbase, actualParams)

    def query(self):
        return self.cursor.fetchall()
