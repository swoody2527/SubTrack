from unittest import result
import subtrack as st
import pytest
from datetime import datetime


def test_calc_next():
    date = "2022-01-10"
    result_date = "2022-07-10"
    test_date = datetime.strptime(date, '%Y-%m-%d').date()
    result = datetime.strptime(result_date, '%Y-%m-%d').date()
    assert (st.calc_next(test_date, 6)) == result

def test_add():
    with pytest.raises(ValueError):
        assert st.add("Netflix", "4.99", "01/01/2022" "notaninteger")
        assert st.add("Netflix", "not_a_number", "20/01/2022", "1")
        assert st.add("Netflix", "4.99", "01-01-2022" "1")
        assert st.add("Netflix", "4.99", "04/25/2022" "1")

    try:
        st.add("Netflix", "4.99", "01/01/2022", "1")
    except Exception:
        assert False, "add was given correct date but raised an exception"


def test_format_view_dates():
    assert st.format_view_dates("2022-01-01") == "01/01/2022"
    with pytest.raises(ValueError):
        assert st.format_view_dates("2022-01")
        assert st.format_view_dates("not_a_date")
    with pytest.raises(ValueError):
        assert st.format_view_dates("2022-word-01")

