from loguru import logger
from databases import Database


async def init_postgres(
    url: str
) -> Database:
    db = Database(
        url=url,
        min_size=1,
        max_size=2
    )
    await db.connect()
    logger.debug("Returning postgres connection")
    return db
