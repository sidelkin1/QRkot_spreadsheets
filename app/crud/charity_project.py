from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDInvestment
from app.models import CharityProject


class CRUDCharityProject(CRUDInvestment):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return db_project_id.scalars().first()

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> List[CharityProject]:
        projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested.is_(True)
            ).order_by(CharityProject.elapsed_time)
        )
        projects = projects.scalars().all()
        return projects


charity_project_crud = CRUDCharityProject(CharityProject)
