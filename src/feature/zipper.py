from tqdm import tqdm
import zipfile

def Zipper(name, password):
	count_pass = len(list(open(password, "rb")))
	is_found = False
	try:
		zip_file = zipfile.ZipFile(name)
	except:
		print('File zip/password Not Founds. Check The File And Try Again')
	finally:
		print("Total Password:", count_pass)
		with open(password, "rb") as wordlist:
			for word in tqdm(wordlist, total=count_pass, unit='word'):
				try:
					zip_file.extractall(pwd=word.strip())
				except:
					continue
				else:
					print("\a")
					print("Password Found:", word.decode().strip())
					is_found = True
					break
		if is_found == False:
			print("Password not found in the wordlist, try another one")