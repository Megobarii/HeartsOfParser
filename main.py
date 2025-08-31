#todo: levels must be set better, a theater can't be all levels, and so on for all the others, uff will do it eventually.

#----------------------------THEATRE-----------------------------------#
class Theatre:
	def __init__(self):
		self.name = ""
		self.subordinates = []
		self.level = 0

	def add_subordinate(self, subordinate):
		if len(self.subordinates) < 5:
			if isinstance(subordinate, Theatre):
				print("Error! a Theater can't be subordinate of another theater!")
			else:
				self.subordinates.append(subordinate)
		else:
			print("Error! Max number of subordinate units!")

	def set_commander(self, commander):
		print("Error! a theater is commanded by nobody!")
		
	def set_name(self, name):
		self.name = name
		
	def set_level(self, level):
		if level < 0 or level > 6:
			print("there is something wrong with this unit's level!")
		else:
			self.level = level

#----------------------------ARMY GROUP--------------------------------#

class Armygroup:
	def __init__(self):
		self.name = ""
		self.commander = None
		self.subordinates = []
		self.level = 0
		
	def add_subordinate(self, subordinate):
		if len(self.subordinates) < 5:
			if isinstance(subordinate, (Theatre, Armygroup)):
				print("Error! Theatres or armygroups can't be subordinates of a armygroup")
			else: 
				self.subordinates.append(subordinate)
		else:
			print("Error! Max number of subordinate units!")
			
	def set_commander(self, commander):
		if isinstance(commander, (Armygroup, Army, Corps, Division, Regiment)):
			print("Error! an Armygroup can't be commanded by an armygroup, army, a Corps, a Division or a Regiment")
		else:
			self.commander = commander
			
	def set_name(self, name):
		self.name = name
		
	def set_level(self, level):
		if level < 0 or level > 6:
			print("there is something wrong with this unit's level!")
		else:
			self.level = level

#-----------------------------ARMY-------------------------------------#

class Army:
	def __init__(self):
		self.name = ""
		self.commander = None
		self.subordinates = []
		self.level = 0
		
	def add_subordinate(self, subordinate):
		if len(self.subordinates) < 5:
			if isinstance(subordinate, (Theatre, Armygroup, Army)):
				print("Error! Theatres, armygroups or armies can't be subordinates of a armies")
			else: 
				self.subordinates.append(subordinate)
		else:
			print("Error! Max number of subordinate units!")

	def set_commander(self, commander):
		if isinstance(commander, (Army, Corps, Division, Regiment)):
			print("Error! an army can't be commanded by an Army, a Corps, a Division or a Regiment")
		else:
			self.commander = commander
			
	def set_name(self, name):
		self.name = name
		
	def set_level(self, level):
		if level < 0 or level > 6:
			print("there is something wrong with this unit's level!")
		else:
			self.level = level

#----------------------------CORPS-------------------------------------#

class Corps:
	def __init__(self):
		self.name = ""
		self.commander = None
		self.subordinates = []
		self.level = 0
		
	def add_subordinate(self, subordinate):
		if len(self.subordinates) < 5:
			if isinstance(subordinate, (Theatre, Armygroup, Army, Corps)):
				print("Error! Theatres, armygroups, armies or Corps can't be subordinates of a corps")
			else: 
				self.subordinates.append(subordinate)
		else:
			print("Error! Max number of subordinate units!")

	def set_commander(self, commander):
		if isinstance(commander, (Corps, Division, Regiment)):
			print("Error! a corps can't be commanded by a Corps, a Division or a Regiment")
		else:
			self.commander = commander
	def set_name(self, name):
		self.name = name
		
	def set_level(self, level):
		if level < 0 or level > 6:
			print("there is something wrong with this unit's level!")
		else:
			self.level = level

#-------------------------DIVISION-------------------------------------#

class Division:
	def __init__(self):
		self.name = ""
		self.commander = None
		self.subordinates = []
		self.level = 0

	def add_subordinate(self, subordinate):
		if len(self.subordinates) < 5:
			if isinstance(subordinate, (Theatre, Armygroup, Army, Corps, Division)):
				print("Error! Theatres, armygroups, armies, Corps or Divisions can't be subordinates of a division")
			else: 
				self.subordinates.append(subordinate)
		else:
			print("Error! Max number of subordinate units!")

	def set_commander(self, commander):
		if isinstance(commander, (Division, Regiment)):
			print("Error! a Division can't be commanded by a Division or a Regiment")
		else:
			self.commander = commander
			
	def set_name(self, name):
		self.name = name
		
	def set_level(self, level):
		if level < 0 or level > 6:
			print("there is something wrong with this unit's level!")
		else:
			self.level = level

#--------------------------REGIMENT------------------------------------#

class Regiment:
	def __init__(self):
		self.name = ""
		self.commander = None
		self.subordinates = []
		self.level = 0

	def add_subordinate(self, subordinate):
		print("Error! a Regiment can't command anybody")

	def set_commander(self, commander):
		if isinstance(commander, Regiment):
			print("Error! a regiment can't be commanded by a Regiment")
		else:
			self.commander = commander
	def set_name(self, name):
		self.name = name
		
	def set_level(self, level):
		if level < 0 or level > 6:
			print("there is something wrong with this unit's level!")
		else:
			self.level = level

#---------------------------------------------------------------------#

def get_unit(line):
	line = line.strip()
	if line.startswith("armygroup"):
		return "armygroup"
	elif line.startswith("theatre"):
		return "theatre"
	elif line.startswith("army"):
		return "army"
	elif line.startswith("corps"):
		return "corps"
	elif line.startswith("division"):
		return "division"
	elif line.startswith("regiment"):
		return "regiment"
	return "nothing"


#def get_unit(line):
#	for i in range(len(line)):
#		if len(line[i:]) >= 4 and line[i:i+4] == "army":
#			return "army"
#		elif len(line[i:]) >= 5 and line[i:i+5] == "corps":
#			return "corps"
#		elif len(line[i:]) >= 7 and line[i:i+7] == "theatre":
#			return "theatre"
#		elif len(line[i:]) >= 8 and line[i:i+8] == "regiment":
#			return "regiment"
#		elif len(line[i:]) >= 8 and line[i:i+8] == "division":
#			return "division"
#		elif len(line[i:]) >= 9 and line[i:i+9] == "armygroup":
#			return "armygroup"
#	return "nothing"
#this returns a string, that must be catched in the main(or somewhere else), and create a object accordingly

def get_indent_level(line):
	level = 0
	for i in range(len(line)):
		if line[i] == " ":
			level = level + 1
		else:
			return level

#there is 6 indent level:
# 4  -> theatre
# 8  -> armygroup
# 12 -> army
# 16 -> corps
# 20 -> division
# 24 -> regiment
#


def get_name(line):
	for i in range(len(line)):
		if len(line[i:]) >= 5 and line[i:i+5] == "name=":
			return line[(i+5):].strip().strip('"')
	return "nothing" #fixed: now consistent with rest of code

def get_info(country):

	in_country = False
	designing_unit = False

	units = []

	#with open("savegame.txt") as file:
	with open("savegame.txt", encoding="ISO-8859-1") as file:
		for line in file:
			#for every line in the savegame file
			if line[:3] == country:
				#if line starts with "TAG" i'm in selected country info
				in_country = True
				
			# stop reading country info when ministers= is found
			if "ministers=" in line and in_country == True:
				in_country = False
				designing_unit = False  # also stop designing any ongoing unit
				continue  # skip this line
				
			if in_country == True:
				#if i am in selected country info, detect if there is a unit on this line
				detected_unit = get_unit(line)
				#if there is, detected_unit = "unit" if not, detected_unit = "nothing"
			else:
				detected_unit = "nothing"
				#if i'm not in selected country info, just put detected_unit = "nothing"
				
			if not detected_unit == "nothing":
				#if detected_unit is NOT =="nothing", it means i am inside selected country info, and there is a unit on this line, so i need to instantiate a object
				
				indent_level = get_indent_level(line)
				#get indent level where this unit is, to understand it's position in the hierarchy
				
				#below, detect if the unit starting on this line is a regiment, division, corps, army, armygroup or a theatre and instantiate a object
				if detected_unit == "regiment":
					current_unit = Regiment()
				elif detected_unit == "division":
					current_unit = Division()
				elif detected_unit == "corps":
					current_unit = Corps()
				elif detected_unit == "army":
					current_unit = Army()
				elif detected_unit == "armygroup":
					current_unit = Armygroup()
				elif detected_unit == "theatre":
					current_unit = Theatre()
					
				designing_unit = True #signal that from now until i have all information, i am gathering info about "current_unit"
				
			if designing_unit == True:
				#i'm designing unit and searching for it's name
				name = get_name(line)
				
				if not name == "nothing":
					# this unit's name line has been found and name saved in "name" variable, so assign it to current_unit
					current_unit.set_name(name)
					units_level = (indent_level // 4) - 1  # fixed: integer division
					current_unit.set_level(units_level)
					designing_unit = False #gathered necessary info, don't need to design any further
					#before going on, since i have all info, add to unit list
					units.append(current_unit)
					
					#set commander
					if not current_unit.level == 0:
						#this unit has a commander
						if len(units) > 1:
							#assuring the list is not empty and have more than just this element
							if units[-2].level < current_unit.level: 
								#previous unit is this unit's commander
								current_unit.set_commander(units[-2])
							if isinstance(current_unit, Regiment) and units[-2].level == current_unit.level and isinstance(units[-2], Regiment):
								#this unit is a regiment, and it's previous unit is a fellow regiment inside the same division, so it's an exception in format, and need a specific section for commander detection
								if len(units) < 6:
									print("there is problem with regiment's commander detection")#this shoudln't happend, but you never know ;)
								else:
									searching_commander = True
									prev = 3
									while searching_commander and prev <= 6: # fix: stop after 5 units above
										regiments_division = units[-prev]
										if isinstance(regiments_division, Division):
											current_unit.set_commander(regiments_division)
											searching_commander = False
										prev += 1
	return units
										
			
			

if __name__ == "__main__":
	country_input = input("country: ")
	units = get_info(country_input)
	#for unit in units:
	#	if not isinstance(unit, Theatre):
	#		print("unit: " + unit.name + " | unit's level: " + str(unit.level))
	#print("there are " + str(len(units)) +" units!")
	
	this_line = ""
	for unit in units:
		for i in range(unit.level):
			this_line = this_line + "  "
		this_line = this_line + unit.name
		print(this_line)
		this_line = ""


