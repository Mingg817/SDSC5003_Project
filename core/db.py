from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings


# 配置 MySQL 的连接 URL

engine = create_engine(
    url=settings.DATABASE_URL,
    pool_size=10,  # 最大连接数
    max_overflow=20,  # 超出连接池大小的额外连接数
    pool_timeout=30,  # 等待连接的超时时间（秒）
    pool_pre_ping=True,  # 检查连接是否有效，无效则重连
    echo=True,  # 开启 SQL 查询日志（调试用）
)

# 创建 SessionLocal 类，用于生成数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

