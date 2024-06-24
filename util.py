def generate_output(snake_cords, head_cords, apple_cords, game_width, game_height):
    output = []

    # Flattened 2D grid representation
    for j in range(head_cords[1] - 250, head_cords[1] + 300, 50):
        for i in range(head_cords[0] - 250, head_cords[0] + 300, 50):
            if (i, j) in snake_cords or i < 0 or i > game_width or j < 0 or j > game_height:
                output.append(1)
            else:
                output.append(0)
                
    # Append apple's relative x-coordinate to the snake's head
    output.append((head_cords[0] - apple_cords[0]) / 50)
    
    # Append apple's relative y-coordinate to the snake's head
    output.append((head_cords[1] - apple_cords[1]) / 50)

    return output

def print_grid(output):
    for row in range(11):
        for col in range(11):
            print(output[row * 11 + col], end=' ')
        print()