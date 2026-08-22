def cart_total(items):
    """items: list of (qty, unit_price) tuples."""
    total = 0.0
    for qty, unit_price in items:
        total += qty * unit_price
    return total
