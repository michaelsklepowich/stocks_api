from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
from .stock import Stock
from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
)
from sqlalchemy import ForeignKey

from .meta import Base


class Portfolio(Base):
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    accounts = relationship('Account', back_populates='portfolios')
    stocks = relationship(Stock, back_populates='portfolios')

    @classmethod
    def new(cls, request, **kwargs):
        """ class method to create new portfolio based on key word argumetns provided in request
        """
        if request.dbsession is None:
            raise DBAPIError
        portfolio = cls(**kwargs)
        request.dbsession.add(portfolio)

        return request.dbsession.query(cls).filter(
            cls.name == kwargs['name']).one_or_none()

    @classmethod
    def one(cls, request=None, pk=None):
        """ class method to retrieve a portfolio from database by primary key
        """
        if request.dbsession is None:
            raise DBAPIError
        return request.dbsession.query(cls).get(pk)