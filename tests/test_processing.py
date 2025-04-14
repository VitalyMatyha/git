from src.processing import filter_by_state, sort_by_date

def test_filter_by_state(operations_data):
    result = filter_by_state(operations_data, "EXECUTED")
    assert all(op["state"] == "EXECUTED" for op in result)

def test_sort_by_date(operations_data):
    sorted_data = sort_by_date(operations_data)
    dates = [op["date"] for op in sorted_data]
    assert dates == sorted(dates, reverse=True)