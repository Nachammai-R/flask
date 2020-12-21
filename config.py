# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:pnQ1hsf5yvG0L8lUUiMY@finaldb.cwrfhv27jae7.us-east-1.rds.amazonaws.com:3306/flaskapp'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'Zgcuhdl6gyuXST/uvIu4O2cq48lwQoXwEt/VXlq7'

