from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core.db import Base
from app.models.base import InvestmentMixin


class Donation(InvestmentMixin, Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
