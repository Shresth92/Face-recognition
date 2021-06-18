def whatsapp():
    import pywhatkit
    import time
    
    hour = time.asctime()[11:13]
    hour = int(hour)
    tim = time.asctime()[14:16]
    timing = int(tim)
    timing += 1
    
    pywhatkit.sendwhatmsg("+91XXXXXXXXXX", "Hello, This is XYZ", hour, timing)
