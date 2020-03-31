import enum
import datetime as dt


# Time scale lambdas to reset the date times
_TIME_SCALE_RESET = {
    'YEAR': lambda date: dt.datetime(year=date.year, month=1, day=1, hour=0, minute=0, second=0),
    'MONTH': lambda date: dt.datetime(year=date.year, month=date.month, day=1, hour=0, minute=0, second=0),
    'DAY': lambda date: dt.datetime(year=date.year, month=date.month, day=date.day, hour=0, minute=0, second=0),
    'HOUR': lambda date: dt.datetime(year=date.year, month=date.month, day=date.day, hour=date.hour, minute=0, second=0),
    'MINUTE': lambda date: dt.datetime(year=date.year, month=date.month, day=date.day, hour=date.hour, minute=date.minute, second=0),
    'SECOND': lambda date: dt.datetime(year=date.year, month=date.month, day=date.day, hour=date.hour, minute=date.minute, second=date.second)
}


class TimeScale(enum.Enum):
    """TimeScale - Enum to represent the different time scales
    :extends Enum:
    """

    YEAR = 0
    MONTH = 1
    DAY = 2
    HOUR = 3
    MINUTE = 4
    SECOND = 5


def reset_time_by_scale(scale: TimeScale, date: dt.datetime) -> dt.datetime:
    """Reset datetime's not necessary fields for the given scale
    :param scale TimeScale:     the scale to use
    :param date dt.datetime:    the date to reset
    :return dt.datetime:        the reset datetime
    """
    return _TIME_SCALE_RESET[scale.name](date)


def compare_time_by_scale(scale: TimeScale, d1: dt.datetime, d2: dt.datetime) -> bool:
    """Compare two datetimes on a given scale
    :param scale TimeScale: the scale to use
    :param d1 dt.datetime:  the first date to compare
    :param d2 dt.datetime:  the second date to compare
    :return bool:           true if they are equal on the scale
    """
    return reset_time_by_scale(scale, d1) == reset_time_by_scale(scale, d2)
