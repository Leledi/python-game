class Entity:
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic

class Mobile(Entity):
	def __init__(self, x, y, graphic):
		Entity.__init__(self, x, y, graphic)
		self.score=0
		self.maxHp=10
		self.curHp=self.maxHp
		self.damage=2
		self.level=1
		self.status="alive"
		self.scoremax=5
	def attack(self,target):
		target.curHp-=self.damage
		if target.curHp<=0:
			target.status="dead"
			self.score+=target.level
		if self.score>= self.scoremax:
			self.level+=1
			self.damage+=2
			self.maxHp+=2
			self.curHp=self.maxHp
			self.scoremax+=5

class Player(Mobile):
	def __init__(self, x, y, graphic):
		Mobile.__init__(self, x, y, graphic)
	
	def move(self):
		direction=input()
		if direction=="w":
			if self.y!=0:
				self.y-=1

		elif direction=="s":
			if self.y!=World1.h-1:
				self.y+=1

		elif direction=="d":
			if self.x!=World1.w-1:
				self.x+=1

		elif direction=="a":
			if self.x!=0:
				self.x-=1

	def level_up(self):
		self.level+=1

class Enemy(Mobile):			
	def __init__(self, x, y, graphic):
		Mobile.__init__(self, x, y, graphic)
		
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


e = Player(5, 5, "X")

for y in range(10):
  for x in range(10):
    if e.x == x and e.y == y:
      print("[{}]".format(e.graphic), end="")
    else:
      print("[ ]", end="")

  print()



