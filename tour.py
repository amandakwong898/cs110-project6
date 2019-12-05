import stdio
from point import Point


class Tour:
    """
    Represents a tour in the traveling salesperson problem.
    """

    def __init__(self):
        """
        Creates an empty tour.
        """

        self._tour = []  # initializing tour, a list of Point objects

    def show(self):
        """
        Prints the tour to standard output.
        """

        for p in self._tour:  # enumerating and writing one/line each point
            stdio.writeln(str(p))  # in tour

    def draw(self):
        """
        Draws the tour to standard draw.
        """

        # Draw the tour by connecting the second point to the first, the third
        # point to the second, etc. Use drawTo() from Point to connect between
        # two points.

        for i in range(1, len(self._tour)):
            self._tour[i].drawTo(self._tour[i - 1])
        self._tour[-1].drawTo(self._tour[0])

    def size(self):
        """
        Returns the number of points on the tour.
        """

        # Return the length of the tour.

        return len(self._tour)

    def distance(self):
        """
        Returns the total distance of the tour.
        """

        # Return the total tour distance calculated as the sum of: the distance
        # of the second point to the first, distance of the third point to the
        # second, etc. Use distanceTo() from Point to calculate the distance
        # between two points.

        total = 0.0
        for i in range(1, self.size() + 1):
            total += self._tour[i % self.size()].distanceTo(self._tour[i - 1])
        return total

    def insertNearest(self, p):
        """
        Inserts the point p using the nearest neighbor heuristic.
        """

        # Find the index 0 <= i < tour size such that _tour[i].distanceTo(p) is
        # the smallest. Insert p (using the insert() method from list) into
        # _tour at index i + 1.

        nearestIndex = -1
        nearestDist = float('inf')
        for i, q in enumerate(self._tour):
            d = p.distanceTo(q)
            if d < nearestDist:
                nearestIndex = i
                nearestDist = d
        self._tour.insert(nearestIndex + 1, p)

    def insertSmallest(self, p):
        """
        Inserts the point p using the smallest increment heuristic.
        """

        # For each 1 <= i <= tour size, let x = _tour[i - 1] and y =
        # _tour[i % tour size]. The increase in the current tour distance that
        # results if p is inserted at i is given by distance(x, p) +
        # distance(y, p) - distance(x, y). Find the index i that results in the
        # smallest such increase. Insert p (using the insert() method from
        # list) into _tour at index i.

        smallestIndex = 0
        smallestIncrease = float('inf')
        for i in range(1, self.size() + 1):
            x = self._tour[i - 1]
            y = self._tour[i % self.size()]
            inc = x.distanceTo(p) + y.distanceTo(p) - x.distanceTo(y)
            if inc < smallestIncrease:
                smallestIndex = i
                smallestIncrease = inc
        self._tour.insert(smallestIndex, p)
