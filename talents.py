#!/usr/bin/env python

def main():
  with open('talents.raw', 'r') as f:
    sections = f.read().split('<section begin=')[2:-1]

  headers = ('Name', 'Job', 'Rank', 'Type', 'Description', 'Cooldown')
  cols_count = len(headers)
  table = []
  for section in sections:
    parts = section.split('\n')[2:8]
    parts[0] = parts[0].split("'''")[1]
    parts[1] = parts[1].strip("|'[]")
    for i in range(2, 6):
      parts[i] = parts[i].strip('|')
    table.append(parts)
  table.sort(key=lambda part: (part[1], int(part[2]), part[0]))
  lens = []
  for i in range(cols_count):
    lens.append(max(len(headers[i]), max([len(p[i]) for p in table])))

  print('| ' + ' | '.join([headers[i].ljust(lens[i]) for i in range(cols_count)]) + ' |')
  print('|' + '|'.join(['-' * (lens[i] + 2)for i in range(cols_count)]) + '|')
  for parts in table:
    print('| ' + ' | '.join([parts[i].ljust(lens[i]) for i in range(cols_count)]) + ' |')


if __name__ == '__main__':
  main()
