
import machine
import utime
sensor_pir1 = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
sensor_pir2 = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)
print("Raspberry Mini Project by team V2")
def pir_handler(pin):
 utime.sleep_ms(100)
 if pin.value():
     if pin is sensor_pir1:
         print("ALARM! Motion detected in bedroom!")
     elif pin is sensor_pir2:
         print("ALARM! Motion detected in living room!")
     for i in range(50):
         led.toggle()
         buzzer.toggle()
         utime.sleep_ms(100)
sensor_pir1.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
sensor_pir2.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
while True:
     led.toggle()
     utime.sleep(5)
