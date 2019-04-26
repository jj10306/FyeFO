from flask_table import Table, Col

class UserTable(Table):
    name = Col("name")
