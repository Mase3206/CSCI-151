#!/usr/bin/env python3

import person, stdio


p1 = person.Person('Trish', 'Olson', 25)
p2 = person.Person('Joe', 'Smith', 45)

stdio.writeln(p1)
stdio.writeln(p2)


stdio.writeln()

# Trish has a birthday
p1.birthday()
stdio.writef('Happy birthday, %s!\n', p1.firstname)

# Trish gets married
p1.lastname = 'Duce'
stdio.writef('Happy marriage, %s!\n', p1.firstname)


stdio.writeln()

stdio.writeln(p1)
stdio.writeln(p2)