#exception: distrub the normal flow of  program
#exception handling: exception handling is a mechanism used to handle 
#runtime error so that the program does not crash unexpectedly
#try : the code that may generate an exception is written inside try
#except: this block exceutes only when an exception occurs.
#else: else block executes only when no exception occurs 
#finally: finally block always executes, no matter what happen

try:
    num = int(input("enter number:"))
    x = 100/num 
    print(x)
except ValueError:
    print("prefer current value")

except ZeroDivisionError:
    print("cannot divide by zero")

except:
    print("some error occured")



file = None
try:
    file = open("data.txt")

except FileExistsError:
    print("file not found")

finally:
    if file:
        file.close()

        print("file closed")


try:
    print("hello")
finally:
    print("end")

# except not run without try
# else  not run without except 
# try and finall run without except and else

# type of error in  except 
# value error : wrong value 
# type error : wrong data type
#Name error : variable not found 
# indexerror : invalid index 
#key error : invalid dictionarykey
# zero division error : divide by zero 

# FileNotFoundError 
# ImportError 
# ImportError 
# PermissionError 
# Runtime Error 
# Memory Error 

try:
    num  = "pranjali"
    print(num)

except ValueError:
    print("wrong value")





