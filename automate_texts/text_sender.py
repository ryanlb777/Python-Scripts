from clockwork import clockwork
import time

api = clockwork.API('')
 
print("Starting Program")

message = clockwork.SMS(
    to = 'phone number',
    message = 'Hello I hope your day is as good as mines..........................')

response = api.send(message)

if response.success:
	print(response.id)
else:
	print(response.error_code)
	print(response.error_message)

print("Complete!")