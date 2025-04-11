class History():
  def __init__(self):
    self.recount()

  def recount(self):
    with open("history.txt", "r") as f:
      self.counts_unfiltered = f.read().split("\n")
    
    self.counts: dict = { "X" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0 }
    total = 0
    length = 0

    for count in self.counts_unfiltered:
      self.counts[count] += 1
      length += 1
      if count.isdigit():
        total += int(count)

    self.avg = round(total / length, 2)

    self.individual = f"""
1: {self.counts["1"]} Times
2: {self.counts["2"]} Times
3: {self.counts["3"]} Times
4: {self.counts["4"]} Times
5: {self.counts["5"]} Times
6: {self.counts["6"]} Times
"""

  def print(self):
    print(f"""
-----History-----

Average Score: {self.avg}
Failures: {self.counts["X"]}

Individual Counts: 
{self.individual}""")
    
  def add(self, num):
    with open("history.txt", "a") as f:
      f.write(f"\n{num}")
    self.recount()


if __name__ == "__main__":
  History().print()