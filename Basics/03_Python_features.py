import dataclasses from dataclass

#
#   Documentation in python
# 

@dataclass
class Square :
  x: int
  def Area(self):
    return self.x * self.x
