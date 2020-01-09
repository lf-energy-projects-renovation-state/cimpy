from cimpy.cgmes_v2_4_15.EquipmentContainer import EquipmentContainer


class Substation(EquipmentContainer):
	'''
	A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.

	:DCConverterUnit:  Default: "many"
	:Region: The SubGeographicalRegion containing the substation. Default: None
	:VoltageLevels: The voltage levels within this substation. Default: "many"
		'''

	cgmesProfile = EquipmentContainer.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'DCConverterUnit': [cgmesProfile.EQ.value, ],
						'Region': [cgmesProfile.EQ.value, ],
						'VoltageLevels': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class EquipmentContainer: \n' + EquipmentContainer.__doc__ 

	def __init__(self, DCConverterUnit = "many", Region = None, VoltageLevels = "many",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCConverterUnit = DCConverterUnit
		self.Region = Region
		self.VoltageLevels = VoltageLevels
		
	def __str__(self):
		str = 'class=Substation\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str