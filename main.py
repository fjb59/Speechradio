from talk import talker
from  listen import voxListener
sayer =talker()
hearer = voxListener()
hearer.listen()
sayer.testMessage(144.725)
sayer.speak()

