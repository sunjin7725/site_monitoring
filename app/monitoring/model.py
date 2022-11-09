import pandas as pd

from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from common.utils import to_sql


@dataclass
class Content:
    category: str
    title: str
    rgsr_dt: str
    frst_rgsr_dtl_dttm: str = field(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    last_rgsr_dtl_dttm: str = field(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def __init__(self, category, title, rgsr_dt):
        self.category = category
        self.title = title
        self.rgsr_dt = rgsr_dt

    def to_dict(self):
        return {
            'CATEGORY': self.category,
            'TITLE': self.title,
            'RGSR_DT': self.rgsr_dt,
            'FRST_RGSR_DTL_DTTM': self.frst_rgsr_dtl_dttm,
            'LAST_RGSR_DTL_DTTM': self.last_rgsr_dtl_dttm
        }


@dataclass
class ContentTable:
    content_list: List[Content]

    def __init__(self):
        self.content_list = []

    def add(self, content):
        self.content_list.append(content)

    def to_sql(self):
        to_sql(
            df=pd.DataFrame([i.to_dict() for i in self.content_list]),
            table='monitoring'
        )
