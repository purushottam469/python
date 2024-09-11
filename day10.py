# try and except:

# a= 5

# try:
#     if not isinstance(a,str):
#          raise ValueError("a is not type of error")
    
# except Exception as e:
    
#     print("error",e)

# finally:
#      print("finaly executed")

# def test_func(a,b):
#      return a+b
     
     
         
class electronic:
        os="window"
        ram="none"
        hard_disk="none"

try:
  laptop=electronic("wndows-10") 

except TypeError as e:
     print("error:",e)

finally:
     print("hello world")