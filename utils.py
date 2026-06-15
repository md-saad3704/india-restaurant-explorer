# Helper utility functions

def format_currency(value):
    """
    Format currency values.
    """

    return f"₹{int(value):,}"


def format_number(value):
    """
    Format large numbers.
    """

    return f"{value:,}"