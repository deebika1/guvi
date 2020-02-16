# program which is used to convert celcius to fahernheit by using function
def temp(celcius):
# formula to convert celcius to faherenheit
 fahrenheit=(celcius*1.8)+32
# round off the fahrenheit value
 f1=round(faherenheit,2)
 return f1
# get the celcius form the user
celcius=float(input())
# call the function and the result is stored in res
res=temp(celcius)
print(res)
