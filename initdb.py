from sqlalchemy import Column, Integer, String, DateTime
from dbsetting import Engine
from dbsetting import Base

class Memo(Base):
    """
    メモ内容を保存するテーブル
    """ 
    __tablename__ = 'memo'
    __table_args__ = {
        'comment': 'メモ内容のマスターテーブル'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column('title', String(30), nullable=False)
    content = Column('content', String(140), nullable=False)
    created_at = Column('created_at', DateTime, nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(bind=Engine)