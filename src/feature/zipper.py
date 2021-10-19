from tqdm import tqdm
import zipfile

def ZIP(success, colored, logtime):
	name = str(input(logtime(False) + ' zip file = '))
	txt = str(input(logtime(False) + ' txt file = '))
	try:
		zip_file = zipfile.ZipFile(name)
		count_pass = len(list(open(txt, "rb")))
	except:
		print(logtime(), colored('File zip/txt Not Founds. Check The File And Try Again', 'red'))
		success()
	finally:
		print(logtime(), "Total Password:", count_pass)
		with open(txt, "rb") as wordlist:
			for word in tqdm(wordlist, total=count_pass, unit='word'):
				try:
					zip_file.extractall(pwd=word.strip())
				except:
					continue
				else:
					print("\a")
					print(logtime(), "Password Found:", word.decode().strip())
					success()
		print(logtime(), "Password not found in the wordlist, try another one")
		success()