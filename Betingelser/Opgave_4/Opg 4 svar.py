import datetime

x = datetime.datetime.now()
navn = input("hvad er dit navn? ")
år = int(input("Hvilket år er du født? "))
maaned = int(input("Hvilken måned er du født i? "))
dag = int(input("Hvilken dag er du født? "))

år_antal = x.year - år
maaned_antal = x.month - maaned
day_antal = x.day - dag

if maaned_antal < 0 or day_antal > 0:
    print(f"Du hedder {navn} og du er {år_antal - 1}")
else:
    print(f"Du hedder {navn} og du er {år_antal}")
