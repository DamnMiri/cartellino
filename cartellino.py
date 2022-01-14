import sys
import datetime

def isd(val):
	return val.strip().isdigit()

if __name__ == "__main__":
	ingr = input("Orario di ingresso:")
	if ":" in ingr:
		ingrs = ingr.split(":")
	elif "." in ingr:
		ingrs = ingr.split(".")
	else:
		print("Formato orario non valido")
		sys.exit()
	ora = ingrs[0]
	minuti = ingrs[1]
	if not isd(ora) and isd(minuti):
		print("Formato orario non valido")
		sys.exit()
	ora = int(ora)
	minuti = int(minuti)
	td_ingr = datetime.timedelta(hours=ora, minutes=minuti)

	giorn = input("Ore giornata:")
	if isd(giorn):
		giorn = int(giorn)
	else:
		print("Ore giornata non valide")
		sys.exit()
	if not (giorn == 6 or giorn == 9) :
		print("Ore giornata non valide")
		sys.exit()
	if giorn == 9:
		td_giorn = datetime.timedelta(hours=int(giorn), minutes=30)
	else:
		td_giorn = datetime.timedelta(hours=int(giorn))

	pausa = input("Minuti di pausa:")
	if not isd(pausa):
		print("Minuti di pausa non validi")
		sys.exit()

	td_pausa = datetime.timedelta(minutes=int(pausa))

	min_exit = td_ingr + td_giorn +td_pausa
	print(f"L'orario minimo di uscita è: {str(min_exit)[:-3]}")