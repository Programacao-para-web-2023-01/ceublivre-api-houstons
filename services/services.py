from core.schemas.chart import *
from core.database.database import db

def get_chart(key):
    chart = db.get(key)
    return chart

def get_user_chart(user):
    items = db.fetch({"user": user}).items
    return items


def update_chart_quantity(key, chart):
    try:
        db.update(chart, key)
        return chart
    except:
        return None
    

def delete_chart(key):
    chart = get_chart(key=key)
    if chart:
        db.delete(key)
        return True
    
    return False