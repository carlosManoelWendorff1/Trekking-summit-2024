import time
from Classes.MotorEsc import MotorESC
from Classes.ServoMotor import ServoMotor
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import pwm


gpio.init()

try:
      # Inicializa o ESC e o Servo
      motor = MotorESC(pwm_pin=port.PA6)
      servo = ServoMotor(pwm_pin=port.PA7)
      # Calibra o ESC
      motor.calibrate()
      # Controle de motor e servo
      while True:
          # Acelera o motor (7.5% = meia velocidade)
          motor.set_speed(7.5)
          time.sleep(5)
          # Vira o servo para a direita (10% de duty cycle)
          servo.set_angle(10)
          time.sleep(2)
          # Retorna o servo ao centro (7.5%)
          servo.set_angle(7.5)
          time.sleep(2)
          # Vira o servo para a esquerda (5% de duty cycle)
          servo.set_angle(5)
          time.sleep(2)
          # Para o motor
          motor.set_speed(5)
          time.sleep(5)
except KeyboardInterrupt:
    # Para o motor e o servo se houver interrupção
    motor.stop()
    servo.stop()
    print("Parando motor e servo...")
finally:
    # Limpa os recursos GPIO
    motor.cleanup()
    servo.cleanup()