
command=""

if command !="exit":
    command=str(input(" select Start , Stop ,Quit:")).lower()
    if command=="start":
        print('Car Started🚗')
    elif  command=='stop':
        print("Car Stopped🛑")
    elif command=='help':
        print("""
              Start-To start the car 
              Stop-To stop the car 
              Quit-To quit 
              """)
    else:
        print("Sorry i dont Understand")
    