
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
from tbay import Item, Bid, User

engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


def get_winner():
    item_id = session.query(Item.id).first()
    item = session.query(Item.name).filter(Item.id == item_id).first()
    winner = session.query(Bid.bidder_id, Bid.price).filter(Bid.item_id == item_id).order_by(Bid.price.desc()).first()
    winner_name = session.query(User.username).filter(User.id == winner[0]).first()
    msg = "{0} won the aution for the {1} with a bid of {2}.".format(
        winner_name[0], item[0], winner[1])
    return msg


print get_winner()