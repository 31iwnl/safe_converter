def safe_float(val):
    try:
        return float(val)
    except Exception:
        return None

def f_to_c(f):
    if f is None:
        return ''
    return round((f - 32) * 5.0 / 9.0, 2)

def inch_to_mm(inch):
    if inch is None:
        return ''
    return round(inch * 25.4, 2)

def mph_to_mps(mph):
    if mph is None:
        return ''
    return round(mph * 0.44704, 2)

def mile_to_km(mile):
    if mile is None:
        return ''
    return round(mile * 1.60934, 2)
