import pygame
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'  # Помещаем окно игры в центр экрана
pygame.display.init()  # Инициализируем модуль pygame.display

def load_image(name, color_key=None):  # Функция для загрузки изображения
    fullname = os.path.join('data', name)  # Путь к файлу изображения
    try:
        image = pygame.image.load(fullname)  # Загружаем изображение
    except pygame.error as message:
        print('Не удаётся загрузить:', name)  # Выводим сообщение об ошибке
        raise SystemExit(message)  # Завершаем работу программы
    image = image.convert_alpha()  # Преобразуем изображение в формат RGBA
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))  # Определяем цвет ключа изображения
        image.set_colorkey(color_key)  # Устанавливаем цвет ключа изображения
    return image

class Mountain(pygame.sprite.Sprite):  # Класс для создания объекта горы
    pygame.display.set_mode()  # Инициализируем модуль pygame.display
    image = load_image("mountains.png")  # Загружаем изображение горы
    background_width = image.get_width()  # Получаем ширину изображения горы

    def __init__(self):
        super().__init__(all_sprites)  # Создаем объект горы
        self.image = Mountain.image  # Устанавливаем изображение горы
        self.rect = self.image.get_rect()  # Получаем прямоугольник изображения горы
        # Вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # Располагаем горы внизу
        self.rect.bottom = height  # Вычисляем высоту расположения гор

class Landing(pygame.sprite.Sprite):  # Класс для создания объекта посадки
    image = load_image("pt.png")  # Загружаем изображение объекта посадки

    def __init__(self, pos):
        super().__init__(all_sprites)  # Создаем объект посадки
        self.image = Landing.image  # Устанавливаем изображение объекта посадки
        self.rect = self.image.get_rect()  # Получаем прямоугольник изображения объекта посадки
        # Вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]  # Задаем координату X объекта посадки
        self.rect.y = pos[1]  # Задаем координату Y объекта посадки

    def update(self):
        # Если ещё в небе
        if not pygame.sprite.collide_mask(self, mountain):  # Проверяем столкновение объекта посадки с горами
            self.rect = self.rect.move(0, 1)  # Перемещаем объект посадки вверх

size = width, height = Mountain.background_width, 400  # Задаем размеры экрана игры
screen = pygame.display.set_mode(size)  # Инициализируем экран игры
clock = pygame.time.Clock()  # Инициализируем таймер игры
all_sprites = pygame.sprite.Group()  # Создаем группу объектов игры
mountain = Mountain()  # Создаем объект горы

running = True  # Флаг, определяющий, запущена ли игра
while running:
    screen.fill((0, 0, 0))  # Заполняем экран игры черным цветом

    all_sprites.draw(screen)  # Рисуем все объекты игры на экране
    all_sprites.update()  # Обновляем положение всех объектов игры

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если нажата кнопка выхода из игры
            running = False  # Изменяем значение флага running

        if event.type == pygame.MOUSEBUTTONDOWN: # Если нажата кнопка мыши
            Landing(event.pos)
    # Ограничивает скорость игры до 50 кадров в секунду
    clock.tick(50)
    pygame.display.flip()
# Завершает работу с библиотекой Pygame
pygame.quit()





