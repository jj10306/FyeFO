from flask_table import Table, Col

class StudentTable(Table):
    name = Col("Name")
    reason = Col("Reason")

