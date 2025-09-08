import pygame
    
def draw_formatted_text(surface, text_segments, rect, font, color, alignment = "left"):
    all_lines = []
    current_line = []
    current_line_width = 0
    current_word_width = 0
    rect_width = rect.width

    #We need to loop through the text_segments = a list of lists
    for segment in text_segments:
        #segment = a list of tuples
        if len(segment) == 1:
            single_tuple = segment[0]
            text_width, text_height = font.size(segment[0][0])
            if text_width + current_line_width <= rect_width:
                current_line_width += text_width
                current_line.append(single_tuple)
            else:
                all_lines.append(current_line)
                current_line = []
                current_line_width = text_width
                current_line.append(single_tuple)
        else:
            for text_tuple in segment:
                tt = text_tuple
                text_width, text_height = font.size(tt[0])
                current_word_width += text_width
            if current_word_width + current_line_width <= rect_width:
                current_line_width += current_word_width
                current_line.append(segment)
                current_word_width = 0
            else:
                all_lines.append(current_line)
                current_line = []
                current_line_width = current_word_width
                current_line.append(segment)
                current_word_width = 0

    current_x = rect.left
    current_y = rect.top
    font_height = font.get_height()
    for text_line in all_lines:
        text_line_width = 0
        for item in text_line:
            if isinstance(item, list):
                split_word = item
                for tuple_parts in split_word:
                    text_width, text_height = font.size(tuple_parts[0])
                    text_line_width += text_width
            else:
                text_width, text_height = font.size(item[0])
                text_line_width += text_width
        if alignment == "left":
            current_x = rect.left
        elif alignment == "center":
            current_x = rect.centerx - (text_line_width / 2)
        for item in text_line:
            if isinstance(item, list):
                font_tuple = item
                for data in font_tuple:
                    rendered_text = font.render(data[0], True, data[1])
                    surface.blit(rendered_text, (current_x, current_y))
                    current_x += rendered_text.get_width()
            else:
                rendered_text = font.render(item[0], True, item[1])
                surface.blit(rendered_text, (current_x, current_y))
                current_x += rendered_text.get_width()
        current_y += font_height
            

#######################################################################                     
#--- No multi-colored words or symbols---
#
# [  <---- all_lines
#     [(str, (255, 255, 255)) <---- font_tuple, (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))], <---- text_line
#     [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#     [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#     [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)),(str, (255, 255, 255)), (str, (255, 255, 255))],
# ]
# #--- random multi-colored words or symbols mixed with mono colored words
# [ <---- all_lines
#     [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#     [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#     [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#     [ <---- text_line
#         [(str, (255, 255, 255)) <---- font_tuple, (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))] <---- split_word,
#         [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))], 
#         [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#     ], <---- also text_line
#     [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#     [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#     [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#     [
#         [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#         [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#         [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#         [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))]
#     ],
#     [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))],
#     [(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255))]
# ]
################### THE ABOVE IS WHAT ALL_LINES WILL BE HOLDING IN IT'S LIST #########################








# -------------- WHAT I WANT THIS FUNCTION TO DO -----------------
# 1.) allow me to make any amount of letters be any color I want
#     no matter what arrangement. The follow are examples
#     - Hello! <--- to make that blue
#     - He <--- make that blue and then llo <--- Make that red
#       so that Hello comes out with red and blue colors.
#     I want to be able to do that without any spaces between
#     letters if they're part of a single word. The input example
#     that will be passed into the function as text_segments
#     is labeled above with example_text_data
# 2.) allow me to position the text wherever I want. I want to
#     be able to take the text segments I provide and put them
#     exactly where I have them like in the welcome screen welcome
#     message. And also I want to be able to use the function to
#     provide horizontally and vertically aligned text, so that
#     I can put the text on my buttons like they are set up to be
#     ln my current buttons in the other screens. Especially the
#     ones set up in race selection phase.