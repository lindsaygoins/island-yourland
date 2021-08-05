from operator import and_, or_
from sqlalchemy.sql.expression import select, or_
from models import *
from datetime import datetime


def select_bugs(data):
    '''Builds the SELECT query for bugs based on user filters.'''

    if data['filter_bugs'] == "all":
            query = select(Bug)
    else:
        month = datetime.now().month - 1
        query = select(Bug).where(
        
        # If the current month is between either the regular season interval or the alternate season interval
        or_(
            or_(
                
                # If the start month is at the beginning of the year and the end month is at the end of the year and the current month is in between
                and_(Bug.monthstart <= month, month <= Bug.monthend), 
                    
                    or_(
                        # If the start month is at the end of the year & the end month is at the beginning

                        # If the current month is at the beginning of the year
                        and_(Bug.monthstart > Bug.monthend, and_(Bug.monthstart >= month, month <= Bug.monthend)),

                        # If the current month is at the end of the year
                        and_(Bug.monthstart > Bug.monthend, and_(Bug.monthstart <= month, month >= Bug.monthend))),
            or_(
                
                # If the alternate start month is at the beginning of the year and the alternate end month is at the end of the year and the current month is in between
                and_(Bug.altmonthstart <= month, month <= Bug.altmonthend),

                    or_ (
                        # If the alternate start month is at the end of the year & the alternate end month is at the beginning

                        # If the current month is at the beginning of the year
                        and_(Bug.altmonthstart > Bug.altmonthend, and_(Bug.altmonthstart >= month, month <= Bug.altmonthend)),

                        # If the current month is at the end of the year
                        and_(Bug.altmonthstart > Bug.altmonthend, and_(Bug.altmonthstart <= month, month >= Bug.altmonthend))),
                )       
                )
            )
        )

        time = datetime.now().hour
        query = query.where(
        
        # If the current hour is between either the regular time interval or the alternate time interval
        or_(
            or_(
                
                # If the start hour is at the beginning of the day and the end hour is at the end of the day and the current hour is in between
                and_(Bug.hourstart <= time, time <= Bug.hourend), 
                    
                    or_(
                        # If the start hour is at the end of the day & the end hour is at the beginning

                        # If the current hour is at the beginning of the day
                        and_(Bug.hourstart > Bug.hourend, and_(Bug.hourstart >= time, time <= Bug.hourend)),

                        # If the current hour is at the end of the day
                        and_(Bug.hourstart > Bug.hourend, and_(Bug.hourstart <= time, time >= Bug.hourend))),
            or_(
                
                # If the alternate start hour is at the beginning of the day and the alternate end hour is at the end of the day and the current hour is in between
                and_(Bug.althourstart <= time, time <= Bug.althourend),

                    or_ (
                        # If the alternate start hour is at the end of the day & the alternate end hour is at the beginning

                        # If the current hour is at the beginning of the day
                        and_(Bug.althourstart > Bug.althourend, and_(Bug.althourstart >= time, time <= Bug.althourend)),

                        # If the current hour is at the end of the day
                        and_(Bug.althourstart > Bug.althourend, and_(Bug.althourstart <= time, time >= Bug.althourend))),
                )       
                )
            )
        )

    # View bugs Lindsay has collected or not collected
    if data['filter_collect'] == "lindsay":
        query = query.where(Bug.lindsay == '1')
    elif data['filter_collect'] == "not_lindsay":
        query = query.where(Bug.lindsay == '0')

    # Sort by alphabet or ID
    if data['sort'] == 'A':
        query = query.order_by(Bug.bugname.asc())
    elif data['sort'] == 'Z':
        query = query.order_by(Bug.bugname.desc())
    else:
        query = query.order_by(Bug.bugid.asc())

    return query


def select_fish(data):
    '''Builds the SELECT query for fish based on user filters.'''

    if data['filter_fish'] == "all":
            query = select(Fish)
    else:
        month = datetime.now().month - 1
        query = select(Fish).where(
        
        # If the current month is between either the regular season interval or the alternate season interval
        or_(
            or_(
                
                # If the start month is at the beginning of the year and the end month is at the end of the year and the current month is in between
                and_(Fish.monthstart <= month, month <= Fish.monthend), 
                    
                    or_(
                        # If the start month is at the end of the year & the end month is at the beginning

                        # If the current month is at the beginning of the year
                        and_(Fish.monthstart > Fish.monthend, and_(Fish.monthstart >= month, month <= Fish.monthend)),

                        # If the current month is at the end of the year
                        and_(Fish.monthstart > Fish.monthend, and_(Fish.monthstart <= month, month >= Fish.monthend))),
            or_(
                
                # If the alternate start month is at the beginning of the year and the alternate end month is at the end of the year and the current month is in between
                and_(Fish.altmonthstart <= month, month <= Fish.altmonthend),

                    or_ (
                        # If the alternate start month is at the end of the year & the alternate end month is at the beginning

                        # If the current month is at the beginning of the year
                        and_(Fish.altmonthstart > Fish.altmonthend, and_(Fish.altmonthstart >= month, month <= Fish.altmonthend)),

                        # If the current month is at the end of the year
                        and_(Fish.altmonthstart > Fish.altmonthend, and_(Fish.altmonthstart <= month, month >= Fish.altmonthend))),
                )       
                )
            )
        )

        time = datetime.now().hour
        query = query.where(
        
        # If the current hour is between either the regular time interval or the alternate time interval
        or_(
            or_(
                
                # If the start hour is at the beginning of the day and the end hour is at the end of the day and the current hour is in between
                and_(Fish.hourstart <= time, time <= Fish.hourend), 
                    
                    or_(
                        # If the start hour is at the end of the day & the end hour is at the beginning

                        # If the current hour is at the beginning of the day
                        and_(Fish.hourstart > Fish.hourend, and_(Fish.hourstart >= time, time <= Fish.hourend)),

                        # If the current hour is at the end of the day
                        and_(Fish.hourstart > Fish.hourend, and_(Fish.hourstart <= time, time >= Fish.hourend))),
            or_(
                
                # If the alternate start hour is at the beginning of the day and the alternate end hour is at the end of the day and the current hour is in between
                and_(Fish.althourstart <= time, time <= Fish.althourend),

                    or_ (
                        # If the alternate start hour is at the end of the day & the alternate end hour is at the beginning

                        # If the current hour is at the beginning of the day
                        and_(Fish.althourstart > Fish.althourend, and_(Fish.althourstart >= time, time <= Fish.althourend)),

                        # If the current hour is at the end of the day
                        and_(Fish.althourstart > Fish.althourend, and_(Fish.althourstart <= time, time >= Fish.althourend))),
                )       
                )
            )
        )

    # View fish Lindsay has collected or not collected
    if data['filter_collect'] == "lindsay":
        query = query.where(Fish.lindsay == '1')
    elif data['filter_collect'] == "not_lindsay":
        query = query.where(Fish.lindsay == '0')

    # Sort by alphabet or ID
    if data['sort'] == 'A':
        query = query.order_by(Fish.fishname.asc())
    elif data['sort'] == 'Z':
        query = query.order_by(Fish.fishname.desc())
    else:
        query = query.order_by(Fish.fishid.asc())

    return query
