# NOTE: BADLY SUPPORTED ON WINDOWS. NOT RECOMMENDED AS WINDOWS FIREWALL GETS IN THE WAY.
# TelloLib
An expansion of the djitellopy with shapes
## Usage:
```py
import TelloLib

tello = TelloLib.Tello()

tello.connect() # Errors if the connection fails

tello.square(50) # returns a boolean if you want to use it
tello.get_battery_level() # You can still use the existing djitellopy functions.

```
### Dependecies
Requires `djitellopy`.
