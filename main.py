# todo: levels must be set better, a theatre can't be all levels, and so on for all the others

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
			print("Error! an Armygroup can't be commanded by an armygroup, army, corps, division or regiment")
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
				print("Error! Theatres, armygroups or armies can't be subordinates of an army")
			else:
				self.subordinates.append(subordinate)
		else:
			print("Error! Max number of subordinate units!")

	def set_commander(self, commander):
		if isinstance(commander, (Army, Corps, Division, Regiment)):
			print("Error! an army can't be commanded by an army, corps, division or regiment")
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
				print("Error! Theatres, armygroups, armies or corps can't be subordinates of a corps")
			else:
				self.subordinates.append(subordinate)
		else:
			print("Error! Max number of subordinate units!")

	def set_commander(self, commander):
		if isinstance(commander, (Corps, Division, Regiment)):
			print("Error! a corps can't be commanded by a corps, division or regiment")
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
				print("Error! invalid subordinate for division")
			else:
				self.subordinates.append(subordinate)
		else:
			print("Error! Max number of subordinate units!")

	def set_commander(self, commander):
		if isinstance(commander, (Division, Regiment)):
			print("Error! a Division can't be commanded by a Division or Regiment")
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
			print("Error! a regiment can't be commanded by a regiment")
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


def get_indent_level(line):
	level = 0
	for i in range(len(line)):
		if line[i] == " ":
			level += 1
		else:
			return level


def get_name(line):
	for i in range(len(line)):
		if len(line[i:]) >= 5 and line[i:i+5] == "name=":
			return line[i+5:].strip().strip('"')

	return "nothing"


def get_info(country):

	in_country = False
	designing_unit = False
	units = []

	with open("savegame.txt", encoding="ISO-8859-1") as file:
		for line in file:

			if line[:3] == country:
				in_country = True

			if "ministers=" in line and in_country:
				in_country = False
				designing_unit = False
				continue

			if in_country:
				detected_unit = get_unit(line)
			else:
				detected_unit = "nothing"

			if detected_unit != "nothing":

				indent_level = get_indent_level(line)

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

				designing_unit = True

			if designing_unit:

				name = get_name(line)

				if name != "nothing":
					current_unit.set_name(name)

					units_level = (indent_level // 4) - 1
					current_unit.set_level(units_level)

					designing_unit = False
					units.append(current_unit)

					if current_unit.level != 0 and len(units) > 1:

						if units[-2].level < current_unit.level:
							current_unit.set_commander(units[-2])

						if isinstance(current_unit, Regiment) and isinstance(units[-2], Regiment):
							if len(units) >= 6:
								searching_commander = True
								prev = 3

								while searching_commander and prev <= 6:
									candidate = units[-prev]

									if isinstance(candidate, Division):
										current_unit.set_commander(candidate)
										searching_commander = False

									prev += 1

	return units


if __name__ == "__main__":

	country_input = input("country: ")
	units = get_info(country_input)

	this_line = ""

	for unit in units:
		this_line += "  " * unit.level + unit.name
		print(this_line)
		this_line = ""

