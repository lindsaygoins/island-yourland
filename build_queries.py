from operator import and_, or_
from sqlalchemy.sql.expression import select, or_
from models import *
from datetime import datetime


def select_bugs(data):
    if data['filter_bugs'] == "all":
            query = select(Bug)
    else:
        month = datetime.now().month - 1
        query = select(Bug).where(or_(and_(Bug.monthstart <= month, month <= Bug.monthend), or_ (and_(Bug.monthstart > Bug.monthend, and_(Bug.monthstart >= month, month <= Bug.monthend)), and_(Bug.monthstart > Bug.monthend, and_(Bug.monthstart <= month, month >= Bug.monthend)))))

        time = datetime.now().hour
        query = query.where(or_(and_(Bug.hourstart <= time, time <= Bug.hourend), or_ (and_(Bug.hourstart > Bug.hourend, and_(Bug.hourstart >= time, time <= Bug.hourend)), and_(Bug.hourstart > Bug.hourend, and_(Bug.hourstart <= time, time >= Bug.hourend)))))
    
    if data['filter_collect'] == "lindsay":
        query = query.where(Bug.lindsay == '1')
    elif data['filter_collect'] == "not_lindsay":
        query = query.where(Bug.lindsay == '0')

    if data['sort'] == 'A':
        query = query.order_by(Bug.bugname.asc())
    elif data['sort'] == 'Z':
        query = query.order_by(Bug.bugname.desc())
    else:
        query = query.order_by(Bug.bugid.asc())
    return query
