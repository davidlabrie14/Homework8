##python script to run tmp36raw

import sys
import os
import time

def main():
	X = int(sys.argv[1])
	i = 0
	for i in range(X):
		(os.system("./tmp36raw"))
		time.sleep(1)
	
if __name__=='__main__':
	main()
