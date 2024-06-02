# HomeAssistantPyscriptHelpers
Helper Modules for Home Assistant Pyscript users


## Light Helper
Instead of adding devices and areas to an 'all lights' group, this module finds all lights and switches and assumes they're tied to a light unless specifically excluded.  This is helpful because when you add and remove lights from your system, they will automatically be included in any actions directed towards all lights.


This is written as a module for Home Assistant Pyscript, so you'll need to place it in your `pyscript/modules` folder.

### Usage Example:

```python
from light_helper import LightHelper

@service
def all_lights_off():
  light_helper = LightHelper()
  light_helper.all_lights_off()

```
