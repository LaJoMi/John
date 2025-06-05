import sys


def allocate_seats(council_seats, committee_size):
    """Allocate seats in a committee using the modified Sainte-Lagu\u00eb method."""
    seats = {party: 0 for party in council_seats}
    for _ in range(committee_size):
        max_party = None
        max_value = -1
        for party, votes in council_seats.items():
            divisor = 1.4 if seats[party] == 0 else 2 * seats[party] + 1
            quotient = votes / divisor
            if quotient > max_value:
                max_value = quotient
                max_party = party
        seats[max_party] += 1
    return seats


def parse_council_seats():
    print("Ange partiernas mandat i kommunfullm\u00e4ktige. Avsluta med tom rad.")
    council_seats = {}
    while True:
        entry = input("Parti mandat (Parti:mandat): ").strip()
        if not entry:
            break
        try:
            party, seats = entry.split(':')
            council_seats[party.strip()] = int(seats)
        except ValueError:
            print("Fel format. Skriv Parti:mandat")
    return council_seats


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if argv:
        try:
            committee_size = int(argv[0])
        except ValueError:
            print("F\u00f6rsta argumentet ska vara antalet platser i n\u00e4mnden")
            return 1
        council_seats = {}
        for arg in argv[1:]:
            try:
                party, seats = arg.split(':')
                council_seats[party] = int(seats)
            except ValueError:
                print(f"Fel argument: {arg}. Ska vara Parti:mandat")
                return 1
    else:
        try:
            committee_size = int(input("Antal platser i n\u00e4mnden: "))
        except ValueError:
            print("Antal platser m\u00e5ste vara ett heltal")
            return 1
        council_seats = parse_council_seats()

    if not council_seats:
        print("Inga partier angivna")
        return 1

    result = allocate_seats(council_seats, committee_size)
    print("\nMandatf\u00f6rdelning i n\u00e4mnden:")
    for party, seats in sorted(result.items(), key=lambda x: -x[1]):
        print(f"{party}: {seats}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
