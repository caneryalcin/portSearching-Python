# portSearching-Python

This project aims to check which port is open or closed according to your host name.When it is finished it shows amount of time that while searching for ports .

Add those libraries:

```
import sys
import subprocess
from  socket import *
from  datetime import  datetime
import subprocess as sp
```

## Note

>sp.call('clear',shell=True) works with terminal.If you use that code in PyCharm or in another IDE probably it'll cause error.
