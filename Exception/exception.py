# try:
#     # Code that might raise an error
# except ExceptionType1:
#     # Handle this specific error
# except ExceptionType2:
#     # Handle another type
# else:
#     # Executes if no error occurs
# finally:
#     # Always executes (even if error occurs)

try:
    x = int("abc")
except Exception as e:
    print("Error:", e)

