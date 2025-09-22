from datetime import date

# Startdatum: 6. Juni 1984
start_date = date(1984, 6, 6)

# Heutiges Datum
today = date.today()

# Differenz in Tagen
days_passed = (today - start_date).days
print(f"Seit dem 6. Juni 1984 sind {days_passed} Tage vergangen.")