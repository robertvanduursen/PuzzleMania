class Puzzle:
    pieces = int
    _width = float  # in centimeters
    height = float  # in centimeters
    image = False

    def __init__(self):
        pass

    # @setter
    # def width(self,val):
    #     self._width = val

    @property
    def width(self):
        if not isinstance(self._width, float):
            self._width = float(self._width)
        return self._width

    @width.setter
    def width(self, value):
        print("Set radius")
        self._width = value

    def with_difficulty(level='X'):
        # komt door
        amount_of_pieces = 10
        # more pieces = more difficult
        ambiguitiy_of_pieces = 10
        # if they can be seeminlgy placed on more places
        image_readability = 10
        # if pieces can be easily located on the image

        # if you can deduce these facts from an image you can reverse engineer the diff level from existing puzzles

        # if you can specify them you can tailor a puzzle to the puzzler

        return ''

    def manufactoring_difficulty(self):
        """
        i.e. properties that leads to costs and quality
        :return:
        """

    def make_puzzle(self):
        assert self.image
        print(self.width)
        assert isinstance(self.width, float)

        print("puzzle made")

    class Grid:
        """ a WIP way to make a puzzle layout """

        def __init__(self, width, height, pieces):
            # spread dots inside the puzzle
            pass
            self.width = width
            self.height = height
            self.pieces = pieces

        def kek(self):
            # todo: if you were to make a grid of X pieces
            #  how many dots would be on the edges?

            # a rectangular grid
            # of evenly sided pieces
            # in a X:Y ratio
            pieces = self.pieces
            width = self.width
            height = self.height

            ratio = width / height
            print(f"ratio = width/height 1:{round(ratio, 4)}")

            area = width * height
            piece_area = area / pieces
            print(f"area of piece = {piece_area}")
            # Area of rectangle / x = Area of each piece
            import math
            length_piece = math.sqrt(piece_area)
            p_length = round(length_piece, 3)
            print(f"a piece = {p_length} x {p_length} cm")

            pieces_width = width / length_piece
            print(f"pieces = {pieces_width}")
            pieces_height = height / length_piece
            print(f"pieces = {pieces_height}")
            # todo: if evenly dividable
            #  how big would a piece be?

            self.do(int(pieces_width), int(pieces_height))

        def do(self, pieces_width, pieces_height):
            import numpy as np
            # 3000
            # nx, ny = (3, 2)
            nx, ny = (pieces_width, pieces_height)
            nx, ny = (pieces_height, pieces_width)
            x = np.linspace(0, 1, nx)
            y = np.linspace(0, 1, ny)
            xv, yv = np.meshgrid(x, y)

            import matplotlib.pyplot as plt
            # plt.plot(xv, yv, marker='o', color='k', linestyle='none')
            # plt.show()

            self.make_grid(nx, ny)

        def make_grid(self, nx, ny):
            import numpy as np
            import matplotlib.pyplot as plt
            from matplotlib.collections import LineCollection

            # x, y = np.meshgrid(np.linspace(0, 1, 11), np.linspace(0, 0.6, 7))
            x, y = np.meshgrid(np.linspace(0, 100, nx), np.linspace(0, 200, ny))

            plt.scatter(x, y)

            segs1 = np.stack((x, y), axis=2)
            segs2 = segs1.transpose(1, 0, 2)
            plt.gca().add_collection(LineCollection(segs1))
            plt.gca().add_collection(LineCollection(segs2))

            # f = plt.figure()
            # f.set_figwidth(20)
            # f.set_figheight(10)

            plt.savefig('foo.png', bbox_inches='tight')
            # plt.show()

        def test_quad_mesh(self):
            from scipy.spatial import Delaunay
            import numpy as np

            n_points = 100
            jitter = 0.1

            # Create an array of evenly spaced values between 0 and 1
            x = np.linspace(0, 1, n_points)

            # Add random jitter to the values
            x += np.random.normal(scale=jitter, size=n_points)

            # Repeat the process for the y values
            y = np.linspace(0, 1, n_points)
            y += np.random.normal(scale=jitter, size=n_points)

            # Combine the x and y values into a 2D array
            vectors = np.column_stack((x, y))

            # vectors = np.meshgrid(np.linspace(0, 100, 200), np.linspace(0, 200, 300))

            # Create an array of 2D vectors
            # vectors = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])

            # Create a Delaunay triangulation of the vectors
            tri = Delaunay(vectors)

            # Create the quadrilateral mesh
            quads = tri.simplices
            print(quads)

            # Create a blank image with the desired size
            image = np.zeros((1024, 1024))

            # Iterate over the quads in the mesh
            for quad in tri.simplices:
                # Get the coordinates of the quad
                x, y = vectors[quad, :].T
                # Plot the quad on the image
                image[np.int32(x * 512), np.int32(y * 512)] = 256

            # save the image to a file
            # https://fileinfo.com/extension/npy
            import sys
            sys.path.append(r"/home/robert/Desktop/myWork/PuzzleMania")
            from lib.show_image import show_image
            show_image(image)
            np.save("quads_mesh.pgy", image)

            # from PIL import Image
            # im = Image.fromarray(image)
            # im.save("your_file.jpeg")

            # import scipy.misc
            import imageio
            imageio.imwrite('outfile.jpg', image)
            # scipy.misc.imsave('outfile.jpg', image)

            print("done")
            # todo: SAVE

            # import matplotlib.pyplot as plt
            #
            # # Plot the quadrilateral mesh
            # plt.triplot(vectors[:, 0], vectors[:, 1], quads)
            #
            # # Save the image to a file
            # plt.savefig("mesh.png")


if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.image = '/home/robert/Desktop/myWork/PuzzleMania/image_color.jpeg'
    puzzle.pieces = 3000
    puzzle.height = 84
    puzzle.width = 118
    puzzle.make_puzzle()

    grid = puzzle.Grid(
        puzzle.width,
        puzzle.height,
        puzzle.pieces,
    )
    grid.test_quad_mesh()

