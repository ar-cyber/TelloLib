# NOTE: BADLY SUPPORTED ON WINDOWS. NOT RECOMMENDED AS WINDOWS FIREWALL GETS IN THE WAY.
# TelloLib
An expansion of the djitellopy with shapes
## Usage:
```
import TelloLib

tello = TelloLib.Tello()

tello.attempt_connect() # Errors if the connection fails

tello.square(50) # returns a boolean if you want to use it


```
### Dependecies
Requires `djitellopy`.
