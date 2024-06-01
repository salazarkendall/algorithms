def pingpong(step, length):
  l1 = []
  l2 = []
  for i in range(step):
    l1.append(i+1)
  for i in range(1,step-1):
    l2.append(i+1)
  l2 = list(reversed(l2))
  l=[]
  while len(l) <= length:
    l.extend(l1)
    l.extend(l2)
  return l[:length]

def convert(s: str, numRows: int) -> str:
  list_pingpong = pingpong(numRows, len(s))
  rows = []
  for _ in range(numRows):
    rows.append([])

  for i, row in enumerate(list_pingpong):
    rows[row-1].append(s[i])

  word = []
  for element in rows:
    word.extend(element)

  res = ''
  for element in word:
    res = res+element
  return res
  
print(convert(convert(convert('PAYPALISHIRING', 3),3),3))