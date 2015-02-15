from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tbay import User, Item, Bid


engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

john = User(username="jsmith",password="pwd1")
jane = User(username="jdoe", password="pwd2")
bob = User(username="bkelly", password="pwd3")
session.add_all([john, jane, bob])
session.commit()

baseball=Item(name="baseball",description='Carlton Fisk homerun ball', owner_id=jane.id)
session.add_all([baseball])
session.commit()

bid1 = Bid(price='140.00', bidder_id=john.id, item_id=baseball.id)
bid2 = Bid(price='180.00', bidder_id=bob.id, item_id=baseball.id)
bid3 = Bid(price='220.00', bidder_id=john.id, item_id=baseball.id)
bid4 = Bid(price='250.00', bidder_id=bob.id, item_id=baseball.id)
session.add_all([bid1, bid2, bid3, bid4])
session.commit()