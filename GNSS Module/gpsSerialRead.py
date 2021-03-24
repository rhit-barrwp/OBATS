import serial
import pynmea2
import pprint as pp
with serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1) as ser:
    # read 10 lines from the serial output
    print("Serial bus is open: " + str(ser.is_open))
    for i in range(20):
        print("---")
        line = ser.readline().decode('ascii', errors='replace')
        print(line.strip())
        msg = pynmea2.parse(ser.readline().decode('ascii', errors='replace'))
        fields = {k: getattr(msg, k) for k in msg.name_to_idx}
        pp.pprint(fields)