import time
import sys
print('Samarth\n1AY24AI097')
indent = 0     
indent_increasing = True
try:
    while True:
        print(' ' * indent + '*' * 10)
        time.sleep(0.1)  
        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit() 
