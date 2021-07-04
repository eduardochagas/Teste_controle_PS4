import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 150)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 500
HEIGHT = 600

FPS = 60

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.joysticks = []


        self.running = True
        self.loop()


    def loop(self):

        while self.running:
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            num = pygame.joystick.get_count()
            print(num)
            if num >= 1 or num <= 4:
                for item in range(num):
                    pygame.joystick.init()
                    joystick = pygame.joystick.Joystick(num-1)
                    self.joysticks.append(joystick)


            for joystick in self.joysticks:

                if joystick.get_name() == "Wireless Controller":

                    self.showMessageController(joystick.get_name(), 32, 20, 10, RED)

                        # self.showMessageController(str(joystick.get_instance_id()), 20, 60, GREEN)
                    # print(joystick.get_instance_id())

                    ###############################################
                    # Cada botão do controle possui um número no pygame, por isso inserimos
                    # o número correspondente ao botão pressionado, dentro do método: get_button().
                    #
                    if joystick.get_button(0):# == True:
                        self.showMessageController('o botão Xis foi apertado !!!', 25, 20, 50, GREEN)

                    if joystick.get_button(1):# == True:
                        self.showMessageController('o botão Bolinha foi apertado !!!', 25, 20, 50, GREEN)

                    if joystick.get_button(2):
                        self.showMessageController('o botão Triângulo foi apertado !!!', 25, 20, 50, GREEN)

                    if joystick.get_button(3):
                        self.showMessageController('O botão Quadrado foi pressionado !!!', 25, 20, 50, GREEN)

                    if joystick.get_button(4):
                        self.showMessageController('o botão L1 foi apertado !!!', 25, 20, 40, GREEN)

                    if joystick.get_button(5):
                        self.showMessageController('o botão R1 foi apertado !!!', 25, 20, 40, GREEN)

                    if joystick.get_button(6):
                        self.showMessageController('o botão GATILHO ESQUERDO (L2) foi apertado !!!', 25, 20, 40, GREEN)

                    if joystick.get_button(7):
                        self.showMessageController('o botão GATILHO DIREITO (R2) foi apertado !!!', 25, 20, 40, GREEN)

                    if joystick.get_button(8):
                        self.showMessageController('o botão SHARE foi apertado !!!', 25, 20, 40, GREEN)

                    if joystick.get_button(9):
                        self.showMessageController('o botão OPTIONS foi apertado !!!', 25, 20, 40, GREEN)

                    if joystick.get_button(10):
                        self.showMessageController('o botão ALAVANCA ESQUERDA foi pressionado !!!', 25, 20, 40, GREEN)

                    if joystick.get_button(11):
                        self.showMessageController('o botão ALAVANCA DIREITA foi pressionado !!!', 25, 20, 40, GREEN)

                    if joystick.get_button(12):
                        self.showMessageController('o botão PS (Playstation) foi pressionado !!!', 25, 20, 40, GREEN)

                    ##################################
                    # imprime os valores do EIXO HORIZONTAL da ALAVANCA ESQUERDA do controle.
                    print(joystick.get_axis(0))
                    ##################################
                    # imprime os valores do EIXO VERTICAL da ALAVANCA ESQUERDA do controle.
                    print(joystick.get_axis(1))


            pygame.display.update()
            self.clock.tick(FPS)

    def showMessageController(self, text, size, posX, posY, color):
        self.font_name = pygame.font.get_default_font()
        self.font = pygame.font.Font(self.font_name, size)
        self.font_render = self.font.render(text, False, color)
        self.rect = self.font_render.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.screen.blit(self.font_render, (self.rect.x, self.rect.y))






if __name__ == '__main__':
    Main()
