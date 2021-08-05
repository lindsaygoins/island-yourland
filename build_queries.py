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


def select_sea_creatures(data):
    '''Builds the SELECT query for sea creatures based on user filters.'''

    if data['filter_sea_creatures'] == "all":
            query = select(Seacreature)
    else:
        month = datetime.now().month - 1
        query = select(Seacreature).where(
        
        # If the current month is between either the regular season interval or the alternate season interval
        or_(
            or_(
                
                # If the start month is at the beginning of the year and the end month is at the end of the year and the current month is in between
                and_(Seacreature.monthstart <= month, month <= Seacreature.monthend), 
                    
                    or_(
                        # If the start month is at the end of the year & the end month is at the beginning

                        # If the current month is at the beginning of the year
                        and_(Seacreature.monthstart > Seacreature.monthend, and_(Seacreature.monthstart >= month, month <= Seacreature.monthend)),

                        # If the current month is at the end of the year
                        and_(Seacreature.monthstart > Seacreature.monthend, and_(Seacreature.monthstart <= month, month >= Seacreature.monthend))),
            or_(
                
                # If the alternate start month is at the beginning of the year and the alternate end month is at the end of the year and the current month is in between
                and_(Seacreature.altmonthstart <= month, month <= Seacreature.altmonthend),

                    or_ (
                        # If the alternate start month is at the end of the year & the alternate end month is at the beginning

                        # If the current month is at the beginning of the year
                        and_(Seacreature.altmonthstart > Seacreature.altmonthend, and_(Seacreature.altmonthstart >= month, month <= Seacreature.altmonthend)),

                        # If the current month is at the end of the year
                        and_(Seacreature.altmonthstart > Seacreature.altmonthend, and_(Seacreature.altmonthstart <= month, month >= Seacreature.altmonthend))),
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
                and_(Seacreature.hourstart <= time, time <= Seacreature.hourend), 
                    
                    or_(
                        # If the start hour is at the end of the day & the end hour is at the beginning

                        # If the current hour is at the beginning of the day
                        and_(Seacreature.hourstart > Seacreature.hourend, and_(Seacreature.hourstart >= time, time <= Seacreature.hourend)),

                        # If the current hour is at the end of the day
                        and_(Seacreature.hourstart > Seacreature.hourend, and_(Seacreature.hourstart <= time, time >= Seacreature.hourend))),
            or_(
                
                # If the alternate start hour is at the beginning of the day and the alternate end hour is at the end of the day and the current hour is in between
                and_(Seacreature.althourstart <= time, time <= Seacreature.althourend),

                    or_ (
                        # If the alternate start hour is at the end of the day & the alternate end hour is at the beginning

                        # If the current hour is at the beginning of the day
                        and_(Seacreature.althourstart > Seacreature.althourend, and_(Seacreature.althourstart >= time, time <= Seacreature.althourend)),

                        # If the current hour is at the end of the day
                        and_(Seacreature.althourstart > Seacreature.althourend, and_(Seacreature.althourstart <= time, time >= Seacreature.althourend))),
                )       
                )
            )
        )

    # View sea creatures Lindsay has collected or not collected
    if data['filter_collect'] == "lindsay":
        query = query.where(Seacreature.lindsay == '1')
    elif data['filter_collect'] == "not_lindsay":
        query = query.where(Seacreature.lindsay == '0')

    # Sort by alphabet or ID
    if data['sort'] == 'A':
        query = query.order_by(Seacreature.seacreaturename.asc())
    elif data['sort'] == 'Z':
        query = query.order_by(Seacreature.seacreaturename.desc())
    else:
        query = query.order_by(Seacreature.seacreatureid.asc())

    return query
