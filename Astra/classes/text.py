class Text:
    def __init__(self, font, text, width):
        self.font = font
        self.width = width
        self.text = text
        self.lines = []

        words = self.text.split()

        line = words[0]

        for word in words[1:]:
            test_line = line + ' ' + word

            if self.font.size(test_line)[0] > self.width:
                self.lines.append(line)

                line = word
            else:
                line = test_line

        self.lines.append(line)

    def draw(self, surface, x, y):
        for i, line in enumerate(self.lines):
            text_surface = self.font.render(line, True, (255, 255, 255))
            surface.blit(text_surface, (x, y + i * self.font.get_height()))