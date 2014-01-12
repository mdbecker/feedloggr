
import datetime

from flask import Blueprint, render_template

from .utils import get_news

######################################################################

feedloggr = Blueprint(
    'feedloggr',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/feedloggr',
)

@feedloggr.route('/')
@feedloggr.route('/<int:year>-<int:month>-<int:day>')
def index(year=None, month=None, day=None):
    """News index, show news for selected date (unspecified or yyyy-mm-dd)."""
    try:
        date = datetime.date(year, month, day)
    except (ValueError, TypeError):
        date = datetime.date.today()
    news = get_news(date)
    delta = datetime.timedelta(days=1)
    context = {
        'news': news,
        'today': date,
        'next_day': str(date + delta),
        'prev_day': str(date - delta),
    }
    return render_template('index.html', **context)

