class Entity:
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic

class Mobile(Entity):
	def __init__(self, x, y, graphic, maxHp, damage, level):
		Entity.__init__(self, x, y, graphic)
		self.maxHp=maxHp
		self.curHp=maxHp
		self.damage=damage
		self.level=level

	def attack(self,target):
		target.curHp-=self.damage

class Player(Mobile):
	def __init__(self, x, y, graphic, maxHp, damage, level):
		Entity.__init__(self, x, y, graphic, maxHp, damage, level)

	def move(self, direction):
		def move(self, direction):
			if direction=="w":
				if self.y==0:
					pass
				else:
					self.y-=1

			elif direction=="s":
				if self.y==World1.h-1:
					pass
				else:
					self.y+=1

			elif direction=="d":
				if self.x==World1.w-1:
					pass
				else:
					self.x+=1

			elif direction=="a":
				if self.x==0:
					pass
				else:
					self.x-=1

class Enemy(Mobile):			
	def __init__(self, x, y, graphic, maxHp, damage, level):
		Entity.__init__(self, x, y, graphic, maxHp, damage, level)
	def move(self):
		direc=randint(0,4)
		if direc==0:
			if self.y!=0:
				self.y-=1
		elif direc==1:
			if self.y!=World1.h-1:
				self.y+=1
		elif direc==2:
			if self.x!=World1.w-1:
				self.x+=1

		elif direc==3:
			if self.x!=0:
				self.x-=1


e = Entity(5, 5, "X")

for y in range(10):
  for x in range(10):
    if e.x == x and e.y == y:
      print("[{}]".format(e.graphic), end="")
    else:
      print("[ ]", end="")

  print()