'''
*  Copyright (C) 2014 Ekironji <ekironjisolutions@gmail.com>
*
*  This file is part of serial libraries examples for UDOO
*
*  Serial libraries examples for UDOO is free software: you can redistribute it and/or modify
*  it under the terms of the GNU General Public License as published by
*  the Free Software Foundation, either version 3 of the License, or
*  (at your option) any later version.
*
*  This libraries are distributed in the hope that it will be useful,
*  but WITHOUT ANY WARRANTY; without even the implied warranty of
*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*  GNU General Public License for more details.
*
*  You should have received a copy of the GNU General Public License
*  along with this program.  If not, see <http://www.gnu.org/licenses/>.
*
'''

import serial
import time

ser = serial.Serial('/dev/ttymxc3',115200,timeout=1)
ser.flushOutput()

print 'Serial connected'

ser.write("1")		# write to Arduino to turn ON the LED

time.sleep(1) 		# delay for 1 second

ser.write("0")		# write to Arduino to turn OFF the LED

time.sleep(1) 		# delay for 1 second
