def draw_formatted_text(surface, text_segments, rect, font, alignment = "left"):
    rect_width = rect.width
    current_line_width = 0
    current_word_width = 0
    full_text_block = []
    current_line = []
    current_word = []
    #text_segments is a always a list of lists. Each inner list will hold something like this. Either:
    #[(str, (255, 255, 255))] OR
    ##[(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), etc...]
    
    for segment in text_segments:
        #segment is always a list of tuples. It will hold either:
        #[(str, (255, 255, 255))] or
        #[(str, (255, 255, 255)), (str, (255, 255, 255)), (str, (255, 255, 255)), etc...]
        if len(segment) == 1:
            for string_and_color_tuple in segment:
                #data is now the value of (string, (255, 255, 255)) only once if there's only one tuple in segment
                data = string_and_color_tuple
                #text_width and text_height are now set to the height and width, in pixels, of the text that rests
                #inside of data[0], which is the first index in our segment's tuple.
                #So, data[0] right now = str in (str, (255, 255, 255))
                #Whereas data[1] would be (255, 255, 255)
                text_width, text_height = font.size(data[0])
                #Now we check if the text_width plus our current_line_width(default 0 before function is called),
                # is as wide, or less wide than our rectangle's width
                if text_width + current_line_width <= rect_width:
                    #And if it is, then we go ahead anbd increast current_line_width by the width of the text of the tuple in pixels.
                    current_line_width += text_width
                    #And then we make sure our tuple goes inside of current_line
                    current_line.append(data)
                    #Because data is the tuple we're looking at, remember?
                else:
                    #So, now we act for when the total of the word plus our line text width is wider than our containing rectangle. First, we need to add current_line to our full_text_block, which will hold the list of tuples that current_line is.
                    full_text_block.append(current_line)
                    #And then we clear outu current_line since it can't get any fuller if we don't. The if check will get skipped every time until we clear it so more tuples can be added
                    current_line = []
                    #And next, we need to do something with the tuple of data. Because it still exists. The tuple ran through the if else, and it didn't pass the if, so now it jumps down to the else, and if we just lear current_line, and do nothing with data, that tuple just moves on and is lost. So our full_text_block will only be partially correct in the end.
                    current_line.append(data)
                    #We add data back to current_line, which we already cleared, so the next time the loop runs, we're on a new line and the if check can pass again since the width shrank down again.
                    current_line_width = text_width
                    #And then, we make sure we reset current_line_width back to the width in pixels of the string inside the tuple we just put into current_line, so current line width knows to to check the proper length in the if check, when we add current_line_width to the next text's width, and see if that total is less than our rectangle width. And that's all we need to do if there's one tuple in the segment list for now.
                    #Now we clear current_line
                    current_line = []
        else:
            #We need to loop through segment yet again.
            for string_and_color_tuple in segment:
                #I use data to remind msyelf what we're dealing with, and it's easier than typing string_and_color_tuple each time. I just named it that so I knew exactly what I was dealing with.
                data = string_and_color_tuple
                #Getting the pixel width off the data string
                text_width, text_height = font.size(data[0])
                #So now we're going to take this loop and make sure we grab the pixel width of each word and add it to current_word_width
                current_word_width += text_width
                #Now we add all the data to our current_word list
                current_word.append(data)
                #So now we know what the entire width of the current word is.
                if current_word_width + current_line_width <= rect_width:
                    #And again, we're checking if all our current string pixel width will fit inside our rectangle surface.
                    #So now, if it will fit, we once more add our word to current_line
                    current_line_width += current_word_width
                    #Now we add our word to our tuple to our word
                    current_line.append(current_word)
                else:
                    #Now we handle if it's too large to add.
                    #our current line needs pushed to our text block
                    full_text_block.append(current_line)
                    #Now we clear out current line
                    current_line = []
                    #Now we make current_line_width be current_word_width
                    current_line_width = current_word_width
                    #Now we add our current word to our current_line, like we did when it was just one tuple in the list
                    current_line.append(current_word)
            current_word = []
            









                # #And remember, as we loop, now data is each tuple as it loops.
                # #So data = (str, (255, 255, 255))
                # data = string_and_color_tuple
                # #we could do a similar thing as we do above, but that would take a while depending on how many tuples are in segment, because we'd have to go through every single tuple and do that exact same thing we did above. Instead, we'll loop through all the data tuples there are. Now we can access the string itself, and then the color value.
                # for data_type in data:
                #     #While loopipng, we just make sure we're getting the right value so we can grab it's pixel width
                #     if isinstance(data_type, str):
                #         text_width, text_height = font.size(data_type)
                #         #Now we add the text width to current_word_width. We do this because if segment has multiple segments, it means that it's the same word, or the same letters all together, and we don't want to add them to current_line individually. If we did that, we could split the word up. Just imagine you've got a word like troubled. If you split it up into every letter, wanting them all a different color, then you could get to troub then led would start on the next line because of how we have the if check on length of segment written that way. So we have text_width, which we'll add to current_word_width. And once the whole loop is done, we'll add the entire segment to current_word, then add that list to current_line, and we'll already ahve the length of the word since we will add each character grouping's width to current_word_width arleady.
                #         current_word_width += text_width
                #         #And juust like before, now we add the string, whcih is data_type, since we're under an if that's making sure we're working with a string, to current_word
                #         current_word.append(data_type)
                # #We handle this differently, though. Because we WANT to fill up current_word completely FIRST
                # #Now that current_word is full, NOW we can check if our current_word_width plus current_line_width is shorter than our rectangle's width
                # if current_word_width + current_line_width <= rect_width:
                #     #If that checks out, we'll want to increase our current_line by the length of our current word's width
                #     current_line_width += current_word_width
                #     #Since we're not overlapping the edge of our rectangle, we can append our current_word list to current_line
                #     current_line.append(current_word)
                #     #So now, the next time the loop runs, it will give us the next tuple inside of the segment, and we do it all over again, creating a new current word list to push into current_line, and repeat that.
                # else:
                #     #But now, we handle what if our current_word width + our current line width is NOT shorter than our rectangle width.
                #     #If that's the case, then we do not want to add current_word to current_line, because current_line is too big. So then what we do is go ahead and push current_line into full_text_block
                #     full_text_block.append(current_line)
                #     #And now that we added the line to full text block, we don't want current line to hold any tuples.
                #     current_line = []
                #     #And now that we've done that, we need to make sure that we increase current_line_width is incrased by the width of our current word, because we're shoving current_word into the newly emptied current_line. This happens when the very last thing in the text segments isn't filling up more space than the rectangle, and then it stops the whole process.
                #     current_line_width = current_word_width
                #     #And now... our line is the length of one word again. We need to actually supply that word to current_line now.
                #     current_line.append(current_word)
                #     #And at this point, there's nothing left in the text segments, so this part of the function is finished, and we have our full full_text_block full of all the lists of string and color tuples inside their individual lists.