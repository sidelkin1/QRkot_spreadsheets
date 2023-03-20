from sqlalchemy.ext.asyncio import AsyncSession


async def make_investment(source, crud, session: AsyncSession):
    targets = await crud.get_all_opened_for_investment(session)
    if not targets:
        return source
    free_amount = source.full_amount
    for target in targets:
        need_amount = min(
            target.full_amount - target.invested_amount,
            free_amount
        )
        crud.update_invested_amount(
            target, need_amount, session
        )
        source = crud.update_invested_amount(
            source, need_amount, session
        )
        if source.fully_invested:
            break
        free_amount -= need_amount
    await session.commit()
    await session.refresh(source)
    return source
