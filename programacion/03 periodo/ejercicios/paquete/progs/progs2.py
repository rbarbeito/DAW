from sys import path
path.append('..\\package\\extra.zip')

print(path)

##import extra.iota
##print(extra.iota.FunI())


from sys import path

path.append('..\\packages')

import extra.good.best.sigma
from extra.good.best.tau import FunT

print(extra.good.best.sigma.FunS())
print(FunT())

