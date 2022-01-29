# BMI = (weight in KG / height in metres squared)

def gather_info():
	height = float(input('What is your height in metres? '))
	weight = float(input('What is your weight in KG? '))
	return (height, weight)


def calculate_bmi(height, weight):
	""""
	Return the Body Mass Index (BMI) for the
	given weight and height
	"""

	bmi = (weight / (height ** 2))
	return bmi

while True:
	height, weight = gather_info()
	bmi = calculate_bmi(height, weight)
	print(bmi)
	break



