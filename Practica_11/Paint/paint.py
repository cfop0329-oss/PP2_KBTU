import pygame
import math

def main():
    pygame.init()
    # Screen setup
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PyGame Extended Paint Program")
    clock = pygame.time.Clock()
    
    # Persistent surface to hold the drawn artwork
    canvas = pygame.Surface((800, 600))
    canvas.fill((0, 0, 0)) # Black background
    
    # Drawing variables
    radius = 15
    # Added modes: 'square', 'rtriangle' (right triangle), 'etriangle' (equilateral), 'rhombus'
    mode = 'draw'       
    color = (0, 0, 255) # Start with Blue
    
    drawing = False
    start_pos = (0, 0)
    current_pos = (0, 0)
    last_pos = None

    # Font for UI
    font = pygame.font.SysFont(None, 24)

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # --- Mode Selection ---
                if event.key == pygame.K_d:
                    mode = 'draw'
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                elif event.key == pygame.K_r:
                    mode = 'rect'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_s:       # NEW: Square
                    mode = 'square'
                elif event.key == pygame.K_t:       # NEW: Right Triangle
                    mode = 'rtriangle'
                elif event.key == pygame.K_q:       # NEW: Equilateral Triangle
                    mode = 'etriangle'
                elif event.key == pygame.K_b:       # NEW: Rhombus
                    mode = 'rhombus'
                
                # --- Color Selection ---
                if event.key == pygame.K_1 :
                    color = (255, 0, 0)     # Red
                elif event.key == pygame.K_2:
                    color = (0, 255, 0)     # Green
                elif event.key == pygame.K_3:
                    color = (0, 0, 255)     # Blue
                elif event.key == pygame.K_4:
                    color = (255, 255, 0)   # Yellow
                elif event.key == pygame.K_5:
                    color = (255, 255, 255) # White

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click to start drawing
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos
                elif event.button == 4: # Scroll Up: Increase brush/line thickness
                    radius = min(200, radius + 2)
                elif event.button == 5: # Scroll Down: Decrease brush/line thickness
                    radius = max(1, radius - 2)
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    # Finalize shape onto the main canvas when releasing left click
                    
                    if mode == 'rect':
                        rect = pygame.Rect(start_pos[0], start_pos[1], current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])
                        rect.normalize()
                        pygame.draw.rect(canvas, color, rect, radius)
                        
                    elif mode == 'circle':
                        dx = current_pos[0] - start_pos[0]
                        dy = current_pos[1] - start_pos[1]
                        dist = int((dx**2 + dy**2)**0.5)
                        if dist > 0:
                            # Prevent crash if radius > dist
                            draw_width = radius if radius < dist else 0
                            pygame.draw.circle(canvas, color, start_pos, dist, draw_width)

                    elif mode == 'square':
                        # Calculate side length based on the smaller dimension of the drag
                        side = min(abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
                        # Determine direction (quadrant) to draw the square correctly
                        dir_x = 1 if current_pos[0] >= start_pos[0] else -1
                        dir_y = 1 if current_pos[1] >= start_pos[1] else -1
                        
                        end_x = start_pos[0] + (side * dir_x)
                        end_y = start_pos[1] + (side * dir_y)
                        
                        square_rect = pygame.Rect(start_pos[0], start_pos[1], end_x - start_pos[0], end_y - start_pos[1])
                        pygame.draw.rect(canvas, color, square_rect, radius)

                    elif mode == 'rtriangle': # Right Triangle
                        # Points: Start, End-X aligned, End-Y aligned
                        p1 = start_pos
                        p2 = (current_pos[0], start_pos[1]) # Horizontal leg
                        p3 = (current_pos[0], current_pos[1]) # Hypotenuse end
                        
                        # Draw polygon (filled=0 means outline only)
                        pygame.draw.polygon(canvas, color, [p1, p2, p3], radius)

                    elif mode == 'etriangle': # Equilateral Triangle
                        # Calculate height and width based on drag distance
                        dx = current_pos[0] - start_pos[0]
                        dy = current_pos[1] - start_pos[1]
                        
                        # Use distance as the approximate side length
                        side_len = int((dx**2 + dy**2)**0.5)
                        if side_len < 1: continue

                        # Calculate vertices for an equilateral triangle pointing up/down based on drag
                        # Top vertex at start_pos
                        p1 = start_pos
                        # Bottom Left
                        p2 = (start_pos[0] - side_len // 2, start_pos[1] + side_len)
                        # Bottom Right
                        p3 = (start_pos[0] + side_len // 2, start_pos[1] + side_len)
                        
                        # Note: This simple calculation assumes dragging downwards. 
                        # For a robust implementation, we'd calculate angle, but this suffices for basic practice.
                        pygame.draw.polygon(canvas, color, [p1, p2, p3], radius)

                    elif mode == 'rhombus':
                        # Rhombus is defined by center and diagonals
                        # Diagonals are determined by the bounding box of start and current pos
                        x1, y1 = start_pos
                        x2, y2 = current_pos
                        
                        # Center point
                        cx = (x1 + x2) // 2
                        cy = (y1 + y2) // 2
                        
                        # Vertices: Top, Right, Bottom, Left
                        p1 = (cx, y1)       # Top (aligned with start Y)
                        p2 = (x2, cy)       # Right (aligned with end X)
                        p3 = (cx, y2)       # Bottom (aligned with end Y)
                        p4 = (x1, cy)       # Left (aligned with start X)
                        
                        pygame.draw.polygon(canvas, color, [p1, p2, p3, p4], radius)

            elif event.type == pygame.MOUSEMOTION:
                current_pos = event.pos
                if drawing:
                    if mode == 'draw':
                        drawLineBetween(canvas, last_pos, current_pos, radius, color)
                    elif mode == 'eraser':
                        # Eraser paints over with the background color (Black)
                        drawLineBetween(canvas, last_pos, current_pos, radius, (0, 0, 0))
                    last_pos = current_pos

        # --- Rendering ---
        # 1. Blit the persistent canvas onto the screen
        screen.blit(canvas, (0, 0))
        
        # 2. Draw temporary live previews for shapes on the screen (not the canvas yet)
        if drawing:
            preview_color = (*color, 100) if len(color) == 3 else color # Simple transparency hack not native in pygame draw, so we just use color
            
            if mode == 'rect':
                rect = pygame.Rect(start_pos[0], start_pos[1], current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])
                rect.normalize()
                pygame.draw.rect(screen, color, rect, radius)
                
            elif mode == 'circle':
                dx = current_pos[0] - start_pos[0]
                dy = current_pos[1] - start_pos[1]
                dist = int((dx**2 + dy**2)**0.5)
                if dist > 0:
                    draw_width = radius if radius < dist else 0
                    pygame.draw.circle(screen, color, start_pos, dist, draw_width)
            
            elif mode == 'square':
                side = min(abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
                dir_x = 1 if current_pos[0] >= start_pos[0] else -1
                dir_y = 1 if current_pos[1] >= start_pos[1] else -1
                end_x = start_pos[0] + (side * dir_x)
                end_y = start_pos[1] + (side * dir_y)
                square_rect = pygame.Rect(start_pos[0], start_pos[1], end_x - start_pos[0], end_y - start_pos[1])
                pygame.draw.rect(screen, color, square_rect, radius)

            elif mode == 'rtriangle':
                p1 = start_pos
                p2 = (current_pos[0], start_pos[1])
                p3 = (current_pos[0], current_pos[1])
                pygame.draw.polygon(screen, color, [p1, p2, p3], radius)

            elif mode == 'etriangle':
                dx = current_pos[0] - start_pos[0]
                dy = current_pos[1] - start_pos[1]
                side_len = int((dx**2 + dy**2)**0.5)
                if side_len > 0:
                    p1 = start_pos
                    p2 = (start_pos[0] - side_len // 2, start_pos[1] + side_len)
                    p3 = (start_pos[0] + side_len // 2, start_pos[1] + side_len)
                    pygame.draw.polygon(screen, color, [p1, p2, p3], radius)

            elif mode == 'rhombus':
                x1, y1 = start_pos
                x2, y2 = current_pos
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2
                p1 = (cx, y1)
                p2 = (x2, cy)
                p3 = (cx, y2)
                p4 = (x1, cy)
                pygame.draw.polygon(screen, color, [p1, p2, p3, p4], radius)

        # 3. Draw On-Screen UI
        ui_text = f"Mode: {mode} (D/E/R/C/S/T/Q/B) | Color: 1-5 | Size: {radius}"
        text_surface = font.render(ui_text, True, (200, 200, 200))
        # Draw a background box for text readability
        bg_rect = text_surface.get_rect(topleft=(10, 10))
        pygame.draw.rect(screen, (0, 0, 0), bg_rect)
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(surface, start, end, width, color):
    """
    Draws a line between two points using circles to create a smooth thick line.
    """
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    if iterations == 0:
        pygame.draw.circle(surface, color, start, width)
        return
        
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(surface, color, (x, y), width)

if __name__ == '__main__':
    main()