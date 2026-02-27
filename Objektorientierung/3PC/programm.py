from pc import PC
import platform


mein = PC()

mein.set_prozessor(platform.processor())
print(mein.get_prozessor())