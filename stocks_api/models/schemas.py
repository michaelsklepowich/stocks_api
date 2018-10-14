from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from . import Portfolio, Stock


class PortfolioSchema(ModelSchema):
    class Meta:
        model = Portfolio


class StockSchema(ModelSchema):
    class Meta:
        model = Stock