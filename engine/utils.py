def draw_multi_line_colored_text(surface, text_segments, rect, font):
    x, y = rect.left, rect.top
    space_width = font.size(' ')[0]
    for text, color in text_segments:
        if "\n" in text:
            num_newlines = text.count("\n")
            y += num_newlines * font.get_linesize()
            x = rect.left
            text = text.lstrip("\n")

        words = text.split(' ')
        for word in words:
            if not word: continue

            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= rect.right:
                x = rect.left
                y += font.get_linesize()

            surface.blit(word_surface, (x, y))
            
            x += word_width + space_width

    return y + font.get_linesize()