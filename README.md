# John

Det här förvaret innehåller ett enkelt Python-program (`seat_allocation.py`) som beräknar hur många platser varje parti får i en nämnd baserat på mandatfördelningen i kommunfullmäktige.

## Användning

Kör programmet med Python 3:

```bash
python3 seat_allocation.py
```

Programmet frågar först efter hur många platser nämnden ska ha och sedan efter hur många mandat varje parti har i kommunfullmäktige. När du skrivit in alla partier avslutar du med en tom rad. Programmet skriver därefter ut hur platserna fördelas i nämnden med hjälp av den modifierade Sainte-Laguë-metoden.

Du kan även ange alla värden direkt som argument:

```bash
python3 seat_allocation.py <platser> Parti1:mandat Parti2:mandat ...
```

Exempel:

```bash
python3 seat_allocation.py 5 A:20 B:10 C:5
```

