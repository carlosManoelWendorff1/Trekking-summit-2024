import time
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import pwm

# Inicialização da GPIO
gpio.init()

# Classe para controle do ESC (Motor)
class MotorESC:
    def __init__(self, pwm_pin, frequency=50):
        """
        Inicializa o motor ESC.
        
        :param pwm_pin: O pino GPIO conectado ao ESC.
        :param frequency: Frequência do sinal PWM (padrão: 50Hz).
        """
        self.pwm_pin = pwm_pin
        self.frequency = frequency
        pwm.init_channel(self.pwm_pin, self.frequency)
    
    def calibrate(self):
        """Calibra o ESC enviando sinais de PWM máximos e mínimos."""
        print("Calibrando ESC...")
        self.set_speed(10)  # Sinal máximo (full throttle)
        time.sleep(2)
        self.set_speed(5)   # Sinal mínimo (throttle zero)
        time.sleep(2)
        print("Calibração concluída.")
    
    def set_speed(self, duty_cycle):
        """
        Define a velocidade do motor via PWM.
        
        :param duty_cycle: Valor de ciclo de trabalho (5% - 10% para controle de velocidade).
        """
        pwm.set_duty_cycle(self.p_pwm_pin, duty_cycle)
    
    def stop(self):
        """Para o motor."""
        pwm.stop(self.pwm_pin)
    
    def cleanup(self):
        """Limpa os recursos do motor."""
        gpio.cleanup()
