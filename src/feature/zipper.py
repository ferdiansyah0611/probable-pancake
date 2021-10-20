from tqdm import tqdm
import zipfile
from app import Application

class ZIP(Application):
	def __init__(self):
		name = str(input(super().logtime(False) + ' zip file = '))
		txt = str(input(super().logtime(False) + ' txt file = '))
		try:
			zip_file = zipfile.ZipFile(name)
			count_pass = len(list(open(txt, "rb")))
		except:
			print(super().logtime(), super().colored('File zip/txt Not Founds. Check The File And Try Again', 'red'))
			super().success()
		finally:
			print(super().logtime(), "Total Password:", count_pass)
			with open(txt, "rb") as wordlist:
				for word in tqdm(wordlist, total=count_pass, unit='word'):
					try:
						zip_file.extractall(pwd=word.strip())
					except:
						continue
					else:
						print("\a")
						print(super().logtime(), "Password Found:", word.decode().strip())
						super().success()
			print(super().logtime(), "Password not found in the wordlist, try another one")
			super().success()