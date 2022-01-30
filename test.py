import os

sklad = os.listdir()
print(sklad)
for index, notatka in enumerate(sklad):
	print(f"Notatka nr {index + 1} to {notatka}")
