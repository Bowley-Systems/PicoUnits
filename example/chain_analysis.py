
from picounits import Q, expects, VOLTAGE, CURRENT, RESISTANCE
 
@expects(VOLTAGE)
def ohm_law(i: Q, r: Q) -> Q:
  return i * r


result = ohm_law(10 * CURRENT, 5 * RESISTANCE)

result.info()
