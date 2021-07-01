from unittest import TestCase
from propsettings.configurable import *
from propsettings.setting import Setting


class TestConfigurable(TestCase):

	def test_register_as_setting(self):
		class Configurable:
			def __init__(self, a=1, s='a'):
				self.a = a
				self.s = s
		register_as_setting(Configurable, 'a')
		settings = inspect.getmembers(Configurable, lambda x: isinstance(x, Setting))
		self.assertEqual(len(settings), 1)
		register_as_setting(Configurable, 's', 'Argument S')
		settings = inspect.getmembers(Configurable, lambda x: isinstance(x, Setting))
		self.assertEqual(len(settings), 2)
		self.assertEqual(settings[0][1].label, 'A')
		self.assertEqual(settings[1][1].label, 'Argument S')

	def test_read_settings(self):
		class Configurable:
			def __init__(self, a=1, s='a'):
				self.a = a
				self.s = s
		register_as_setting(Configurable, 'a')
		register_as_setting(Configurable, 's', 'Argument S')
		c = Configurable(3, 'qwe')
		props = get_settings(c)
		self.assertEqual(len(props), 2)
		self.assertEqual(props[0].fget(c), 3)
		self.assertEqual(props[1].fget(c), 'qwe')
		self.assertEqual(props[0].label, 'A')
		self.assertEqual(props[1].label, 'Argument S')

	def test_read_dict_settings(self):
		class A:
			def __init__(self, a=1, s='a'):
				self.a = a
				self.s = s
		register_as_setting(A, 'a')
		register_as_setting(A, 's', 'Argument S')

		class B:
			def __init__(self):
				self.b = 42

		class C:
			def __init__(self, c=2):
				self.c = c
				self.settinga = A(4, 'b')
				self.settingb = B()

		register_as_setting(C, 'c')
		register_as_setting(C, 'settinga')
		register_as_setting(C, 'settingb')
		c = C()
		d = get_dict_settings(c)
		expected = {
			'C': 2,
			f'Settinga({self.__module__}.A)': {
				'A': 4,
				'Argument S': 'b'
			},
			f'Settingb({self.__module__}.B)': {}
		}
		self.assertEqual(expected, d)
