def print_two(*args):
	arg1, arg2 = args
	print(f"first argument:{arg1},second argument:{arg2}")
def print_one(arg1):
   	print(f"only argument:{arg1}")

arg1 = "testing"
print_two('hello','hi')
print_one('hmmm')
print(arg1)