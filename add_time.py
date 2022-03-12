def add_time(start, duration, day=None):
  pfx = start.split()[1]
  hours, mins = [int(x) for x in start.split()[0].split(':')]
  ahours, amins = [int(x) for x in duration.split(':')]
  rhours = hours + ahours
  rmins = mins + amins
  if rmins // 60 != 0:
    rhours += rmins // 60
    rmins = rmins % 60
  if hours == 12:
    c = rhours // 12 - 1
  else:
    c = rhours // 12

  d = 0
  for _ in range(c):
    if pfx == 'AM':
      pfx = 'PM'
    elif pfx == 'PM':
      pfx = 'AM'
      d += 1

  if rhours % 12 == 0:
    rhours = 12
  else:
    rhours %= 12
  rhours = str(rhours)
  rmins = str(rmins).zfill(2)
  p1 = f"{rhours}:{rmins} {pfx}"
  if d == 1:
    p3 = f'(next day)'
  elif d > 1:
    p3 = f"({d} days later)"
  week = {'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3,
          'thursday': 4, 'friday': 5, 'saturday': 6, 0: 'sunday', 1: 'monday',
          2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday'}
  if day:
    day = day.lower()
    if week[day] + d >= 7:
      p2 = week[(week[day] + d) % 7].title()
    else:
      p2 = week[week[day] + d].title()

  if d and day:
    return f"{p1}, {p2} {p3}"
  elif d:
    return f"{p1} {p3}"
  elif day:
    return f"{p1}, {p2}"
  else:
    return p1
