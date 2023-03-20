from sqlalchemy import Column, String, Text, func
from sqlalchemy.ext.hybrid import hybrid_property

from app.core.db import Base
from app.models.base import InvestmentMixin


class CharityProject(InvestmentMixin, Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    @hybrid_property
    def elapsed_time(self):
        return self.close_date - self.create_date

    @elapsed_time.expression
    def elapsed_time(cls):
        return func.julianday(cls.close_date) - func.julianday(cls.create_date)
