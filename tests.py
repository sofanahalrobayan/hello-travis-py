def test1():
	print("test 1 passed cause we so cool")
	return True

def test2():
	print("naaaah")
	return False


if __name__ == "__main__":
	
	result = 0
	result = result if test1() else 1
	result = result if test2() else 1
	
	exit(result)