#***********************************************************************************************
def calculate():
  cost_comp = float(input(''))
  qty_comp = int(input(''))
  
  cost_chair = float(input(''))
  qty_chair = int(input(''))
  
  cost_table = float(input(''))
  qty_table = int(input(''))
  
  total = (cost_comp * qty_comp) + (cost_chair * qty_chair) + (cost_table * qty_table)
  return int(total)

print(calculate())

print()

#***********************************************************************************************

def year(yr):
  y=yr.split(':')
  for i in y:
    i.strip()
    return int(y[0])
    
yr=input("")

print(year(yr))
#***********************************************************************************************