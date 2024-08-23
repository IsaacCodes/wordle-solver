#Stores number of guesses something took
with open("history.txt", "r") as f:
  txt = f.read()
  counts = txt.split("\n")
  counts = [int(item) for item in counts if item != "X" and item != ""]

#Functions to store these
def avg():
  global counts
  nums = list(filter(lambda n: n != "X", counts.copy()))
  return round(sum(nums) / len(nums), 2)

def individual():
  global counts
  indiv = f"""
  1: {counts.count(1)} Times
  2: {counts.count(2)} Times
  3: {counts.count(3)} Times
  4: {counts.count(4)} Times
  5: {counts.count(5)} Times
  6: {counts.count(6)} Times
  """
  return indiv

def failures():
  global counts
  return counts.count("X")

def add(num):
  global txt
  txt += f"{num}\n"
  with open("history.txt", "w") as f:
    f.write(txt)

  counts.append(num)