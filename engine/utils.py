import pygame

import pygame

def draw_formatted_text(surface, text_segments, rect, font, alignment="left", vert_alignment="top"): # NEW: Added vert_alignment
    all_words = []
    for segment_list in text_segments:
        for text, color in segment_list:
            words = text.split(' ')
            for i, word in enumerate(words):
                if "\n" in word:
                    parts = word.split('\n')
                    for j, part in enumerate(parts):
                        if part:
                            all_words.append((part, color))
                        if j < len(parts) - 1:
                            all_words.append(('\n', color))
                else:
                    all_words.append((word, color))
                
                if i < len(words) - 1:
                    all_words.append((' ', color))

    all_lines = []
    current_line = []
    current_line_width = 0
    space_width, _ = font.size(' ')

    for word, color in all_words:
        if word == '\n':
            all_lines.append(current_line)
            current_line = []
            current_line_width = 0
            continue
        
        word_width, _ = font.size(word)
        
        if current_line_width + word_width <= rect.width:
            current_line.append((word, color))
            current_line_width += word_width
        else:
            all_lines.append(current_line)
            current_line = [(word, color)]
            current_line_width = word_width

    all_lines.append(current_line)
    font_height = font.get_height()
    
    total_text_height = len(all_lines) * font_height

    current_y = rect.top
    if vert_alignment == "center":
        current_y = rect.centery - (total_text_height / 2)
    elif vert_alignment == "bottom":
        current_y = rect.bottom - total_text_height

    for line in all_lines:
        line_width = 0
        for word, color in line:
            line_width += font.size(word)[0]

        current_x = rect.left
        if alignment == "center":
            current_x = rect.centerx - (line_width / 2)
        elif alignment == "right":
            current_x = rect.right - line_width
            
        for word, color in line:
            rendered_text = font.render(word, True, color)
            surface.blit(rendered_text, (current_x, current_y))
            current_x += rendered_text.get_width()
            
        current_y += font_height