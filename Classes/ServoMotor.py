
# Classe para controle do Servo Motor
class ServoMotor:
    def __init__(self, pwm_pin, frequency=50):
        """
        Inicializa o servo motor.
        
        :param pwm_pin: O pino GPIO conectado ao servo.
        :param frequency: Frequência do sinal PWM (padrão: 50Hz).
        """
        self.pwm_pin = pwm_pin
        self.frequency = frequency
        pwm.init_channel(self.pwm_pin, self.frequency)
    
    def set_angle(self, duty_cycle):
        """
        Define o ângulo de rotação do servo via PWM.
        
        :param duty_cycle: Ciclo de trabalho (geralmente 5% a 10% para controle de ângulo).
        """
        pwm.set_duty_cycle(self.pwm_pin, duty_cycle)
    
    def stop(self):
        """Para o servo motor."""
        pwm.stop(self.pwm_pin)
    
    def cleanup(self):
        """Limpa os recursos do servo motor."""
        gpio.cleanup()
