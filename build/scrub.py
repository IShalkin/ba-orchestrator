# Author and book attributions are removed from generated cards. This explicit, ordered list is applied
# by build_references.py to every name and field value, and by verify_references.py before comparing.
# Eponymous method names (Porter's Five Forces, Kotter, Lewin, Ansoff, Ishikawa, Kano, ...) are names
# of the methods themselves and are kept.
SCRUB = [
    (" (van Lamsweerde)", ""),
    ("Cockburn's ", ""),
    (" (Cockburn Style)", ""),
    (" according to Wiegers", ""),
    (" (Wiegers)", ""),
    ("Wiegers prioritization matrix", "Prioritization matrix"),
    (" (Gilb/Robertson)", ""),
    ("CMMI / BABOK Maturity Assessments", "CMMI Maturity Assessments"),
    (" (BABOK)", ""),
    (" (Tom Gilb's method)", ""),
    (" (Tom Gilb)", ""),
    (" (Gilb)", ""),
]


def scrub(text):
    for old, new in SCRUB:
        text = text.replace(old, new)
    return text
