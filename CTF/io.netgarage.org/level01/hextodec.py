import sys
def hextodecimal(digit):
	return int(digit, 16)

if __name__ == "__main__":
	hexstring = sys.argv[1]
	print(hextodecimal(hexstring))
