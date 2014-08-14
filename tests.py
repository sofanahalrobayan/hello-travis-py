def test1():
	#our awesome test
	return True

def test2():
	#our other awesome test
	return True


if __name__ == "__main__":
	
	result = 0
	result = result if test1() else 1
	result = result if test2() else 1
	
	exit(result)