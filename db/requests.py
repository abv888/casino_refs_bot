from sqlalchemy import select, update, func, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.attributes import flag_modified

from .models import User

async def add_user(
        session: AsyncSession,
        user: User
):
    session.add(user)
    await session.commit()


async def get_user_by_id(
        session: AsyncSession,
        user_id: int
):
    query = (
        select(
            User
        )
        .where(
            User.telegram_id == user_id
        )
    )
    result = await session.execute(query)
    return result.scalar()

async def get_all_users(
        session: AsyncSession
):
    query = (
        select(
            User
        )
    )
    result = await session.execute(query)
    return result.scalars()

async def set_localization_for_user(
        session: AsyncSession,
        user_id: int,
        localization: str
):
    query = (
        update(
            User
        )
        .where(
            User.telegram_id == user_id
        )
        .values(
            localization=localization
        )
    )
    await session.execute(query)
    await session.commit()

async def get_localization_for_user(
        session: AsyncSession,
        user_id: int
):
    query = (
        select(
            User
        )
        .where(
            User.telegram_id == user_id
        )
    )
    result = await session.execute(query)
    return result.scalar().localization