print('start')
import socket
def web_page():
    if led.value() == 1:
        gpio_state = 'ON'
    else:
        gpio_state = 'OFF'
    
    html = """
        <html>
        <head>
            <title>
                pgg ngenngen
            </title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="icon" href="data:,">
        </head>
          <body>
              <h1>pgg ngenngen</h1> 
          <p>GPIO state: """ + gpio_state + """</p>
          <p><a href="/?car=forward"><button>F</button></a></p>
          <p><a href="/?car=left"><button>L</button></a></p>
          <p><a href="/?car=right"><button>R</button></a></p>
          </body>
    </html>"""
    return html
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

print('end')
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' %str(addr))
    request = conn.recv(1024)
    request = str(request)
    print ('Content = %s' %request)
    car_forward =  request.find('/?car=forward')
    car_left = request.find('/?car=left')
    car_right = request.find('/?car=right')
    print(car_forward)
    print(car_left)
    print(car_right)
    if car_forward == 6:
        print('car forward')
        motor1.value(1)
        motor2.value(1)
    if car_left == 6:
        print('car left')
        motor1.value(0)
        motor2.value(1)
    if car_right == 6:
        print('car right')
        motor1.value(1)
        motor2.value(0)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()