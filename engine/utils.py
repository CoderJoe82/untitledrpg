def draw_formatted_text(surface, text_segments, rect, font):
    PUNCTUATION = [',', '.', '?', '!']
    x, y = rect.left, rect.top
    space_width = font.size(' ')[0]
    for text, color in text_segments:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if i > 0:
                y += font.get_linesize()
                x = rect.left
            words = line.split(' ')
            for j, word in enumerate(words):
                if not word: 
                    continue

                word_surface = font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= rect.right:
                    x = rect.left
                    y += font.get_linesize()
                surface.blit(word_surface, (x, y))
                x += word_width
                if j < len(words) - 1 and words[j + 1] not in PUNCTUATION:
                    x += space_width

    return y + font.get_linesize()

class Button:
    def __init__(self):
        pass