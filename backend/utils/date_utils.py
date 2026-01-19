from datetime import date, timedelta


def get_last_7_days(reference_date: date):
    """
    Returns a list of last 7 dates including reference_date
    """
    return [reference_date - timedelta(days=i) for i in range(6, -1, -1)]
