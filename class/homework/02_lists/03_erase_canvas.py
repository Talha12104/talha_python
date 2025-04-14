from graphics import GraphWin, Rectangle, Point
import time

canvas_width = 400
canvas_height = 400
cell_size = 40
eraser_size = 20

def erase_object(canvas, eraser, cells):
    eraser_x1, eraser_y1 = eraser.getP1().getX(), eraser.getP1().getY()
    eraser_x2, eraser_y1 = eraser.getP2().getX(), eraser.getP2().getY()

    for cell in cells:
        cell_x1, cell_y1 = cell.getP1().getX(), cell.getP1().getY()
        cell_x2, cell_y2 = cell.getP2().getX(), cell.getP2().getY()

        # Check if eraser overlaps with any cell
        if not (eraser_x2 < cell_x1 or eraser_x1 > cell_x2 or eraser_y1 > cell_y2 or eraser_y1 < cell_y1):
            cell.undraw()  # "Erase" by removing from canvas

def main():
    canvas = GraphWin("Eraser Canvas", canvas_width, canvas_height)
    
    num_rows = canvas_height // cell_size
    num_cols = canvas_width // cell_size

    cells = []  # Store drawn cells

    # Draw grid
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * cell_size
            top_y = row * cell_size
            right_x = left_x + cell_size
            bottom_y = top_y + cell_size

            cell = Rectangle(Point(left_x, top_y), Point(right_x, bottom_y))
            cell.setFill("blue")
            cell.draw(canvas)
            cells.append(cell)

    canvas.getMouse()

    last_click = canvas.getMouse()
    eraser = Rectangle(
        Point(last_click.getX(), last_click.getY()),
        Point(last_click.getX() + eraser_size, last_click.getY() + eraser_size)
    )
    eraser.setFill("pink")
    eraser.draw(canvas)

    while True:
        mouse = canvas.getMouse()
        eraser.move(mouse.getX() - last_click.getX(), mouse.getY() - last_click.getY())

        erase_object(canvas, eraser, cells)
        last_click = mouse

        time.sleep(0.05)

if __name__ == '__main__':
    main()
