def f(x,y) -> float:
  return x + y - (x*y/100)
# Main Formula to calculate all Resis

def calcDamage((pen ,res ,penres ,dmg) -> float:
    #PEN is the % of the attack that ignores PEN
    #Resultant Damage = DMG*(1-((Resis/100)*(1-(Pen * (1-PenResis/100) /100)
    return dmg * (1- ((res/100) * (1 - (pen * (1 - penres/100) / 100))))
