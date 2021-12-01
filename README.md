# propsettings

This packages enables you to decorate class member variables as a Setting. A Setting is a type of property that allows defining characteristics of a variable that are taken into account by a user interface code to render that variable properly.

# Installation
```pip install propsettings```

# Usage
To register a member variable as a Setting you must use the method ```register_as_setting```, e.g.
```python
from propsettings.configurable import register_as_setting

class Example:
  def __init__():
    self._variable = 4

register_as_setting(Example, "_variable")
```

You can specify the label the UI will show for that variable with
```python
register_as_setting(Example, "_variable", label="Variable label")
```

When the variable you want to decorate is initialized with None you must also specify the data type
```python
class Example:
  def __init__():
    self._variable = None

register_as_setting(Example, "_variable", setting_value_type=str)
```

Sometimes is desirable to draw (in the user interface) your variable in a different way than the default. For example, the default way to show an integer value is with a text edit validated to only accept numeric values. However, maybe your variable only makes sense in the range [0 , 10]. In that case is better to have a slider than a text edit. That is when setting types come into play. A setting type is a type of annotation that gives more information about how to draw and validate a variable. For example:
```python
from propsettings.setting_types.range_setting_type import Range

register_as_setting(Example, "_variable", setting_type=Range(0, 10))
```

To get a list of an object settings you can use
```python
from propsettings.configurable import get_settings

e = Example()
settings = get_settings(e)
```

# How to draw UI
This package is for variable annotation only. In order to draw user interfaces that take into account this annotations to render the variables you annotate, you must use another library. For Qt aaplications there is [propsettings_qt](https://github.com/mnicolas94/propsettings_qt)
