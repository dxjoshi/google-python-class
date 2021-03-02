# Python checks code at runtime
#
# to import 're' module and can now use definition by fully qualified names, for example "re.findall"
import re

# another way to import, now can straightaway use the exit(0), without providing the module name 'sys'
from sys import exit

result = re.findall(r'^[a-zA-Z0-9.]+@[a-zA-Z]+\.[a-z]+$',
                    'abra.ca.dabra@gmail.com')

result = 'Apple '
result = result * 3     # equal to 3 times '+' operation
print(result)
# help(len)      help used to find documentation about modules/functions/methods

exit(0)

print('this shouldn\'t print')
