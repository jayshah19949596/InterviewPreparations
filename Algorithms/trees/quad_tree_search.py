# We can construct a quadtree from a two-dimensional area using the following steps:
#
# 1. Divide the current 2D space into four boxes.
# 2. If a box contains one or more points in it, create a child object, storing in it the 2D space of the box
# 3. If a box does not contain any points, do not create a child for it
# 4. Recurse for each of the children.

# Insert Function
# The insert functions is used to insert a node into an existing Quad Tree.
# This function first checks whether the given node is within the boundaries of the current quad.
# If it is not, then we immediately cease the insertion. If it is within the boundaries,
# we select the appropriate child to contain this node based on its location.
# This function is O(Log N) where N is the size of distance.
#
# Search Function
# The search function is used to locate a node in the given quad.
# It can also be modified to return the closest node to the given point.
# This function is implemented by taking the given point, comparing with  boundaries of the child quads and recursing.
# This function is O(Log N) where N is size of distance.

# Application:
#      1. Image compression.
#      2. Searching in 2D space, example: Google Maps
# Limitation:
#      1. It does not scale well.
#      2. Changes in network topology are not reflected quickly since updates are spread node-by-node.
#      3. Does not handle negative cycle reachable from the source vertex to destination vertex.
# Complexity Analysis:
#       Insert Function is O(log(n))
#       Search Function is O(log(n))

class Rect:
    """A rectangle centred at (cx, cy) with width w and height h."""

    def __init__(self, cx, cy, w, h):
        self.cx, self.cy = cx, cy
        self.w, self.h = w, h
        self.west_edge, self.east_edge = cx - w/2, cx + w/2
        self.north_edge, self.south_edge = cy - h/2, cy + h/2

    def __repr__(self):
        return str((self.west_edge, self.east_edge, self.north_edge,
                self.south_edge))

    def __str__(self):
        return '({:.2f}, {:.2f}, {:.2f}, {:.2f})'.format(self.west_edge,
                    self.north_edge, self.east_edge, self.south_edge)

    def contains(self, point):
        """Is point (a Point object or (x,y) tuple) inside this Rect?"""

        try:
            point_x, point_y = point.x, point.y
        except AttributeError:
            point_x, point_y = point

        return point_x >= self.west_edge and point_x <  self.east_edge and point_y >= self.north_edge and point_y < self.south_edge

    def intersects(self, other):
        """Does Rect object other interesect this Rect?"""
        return not (other.west_edge > self.east_edge or
                    other.east_edge < self.west_edge or
                    other.north_edge > self.south_edge or
                    other.south_edge < self.north_edge)

    def draw(self, ax, c='k', lw=1, **kwargs):
        x1, y1 = self.west_edge, self.north_edge
        x2, y2 = self.east_edge, self.south_edge
        ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], c=c, lw=lw, **kwargs)


class QuadTree(object):
    def __init__(self, boundary, max_points=4, depth=0):
        """Initialize this node of the quadtree.

        boundary is a Rect object defining the region from which points are
        placed into this node;
        max_points is the maximum number of points the
        node can hold before it must divide (branch into four more nodes);
        depth keeps track of how deep into the quadtree this node lies.

        """

        self.boundary = boundary
        self.max_points = max_points
        self.points = []
        self.depth = depth
        # A flag to indicate whether this node has divided (branched) or not.
        self.divided = False

    def divide(self):
        """Divide (branch) this node by spawning four children nodes."""

        cx, cy = self.boundary.cx, self.boundary.cy
        w, h = self.boundary.w / 2, self.boundary.h / 2
        # The boundaries of the four children nodes are "northwest",
        # "northeast", "southeast" and "southwest" quadrants within the
        # boundary of the current node.
        self.nw = QuadTree(Rect(cx - w / 2, cy - h / 2, w, h),
                           self.max_points, self.depth + 1)
        self.ne = QuadTree(Rect(cx + w / 2, cy - h / 2, w, h),
                           self.max_points, self.depth + 1)
        self.se = QuadTree(Rect(cx + w / 2, cy + h / 2, w, h),
                           self.max_points, self.depth + 1)
        self.sw = QuadTree(Rect(cx - w / 2, cy + h / 2, w, h),
                           self.max_points, self.depth + 1)
        self.divided = True

    def insert(self, point):
        """Try to insert Point point into this QuadTree."""

        if not self.boundary.contains(point):
            return False  # The point does not lie inside boundary: bail.
        if len(self.points) < self.max_points:
            self.points.append(point)  # There's room for our point without dividing the QuadTree.
            return True

        # No room: divide if necessary, then try the sub-quads.
        if not self.divided:
            self.divide()

        return (self.ne.insert(point) or
                self.nw.insert(point) or
                self.se.insert(point) or
                self.sw.insert(point))

    def search(self, target_boundary, found_points):
        """Find the points in the quadtree that lie within boundary."""

        if not self.boundary.intersects(target_boundary):
            # If the domain of this node does not intersect the search
            # region, we don't need to look in it for points.
            return False

        # Search this node's points to see if they lie within boundary ...
        for point in self.points:
            if target_boundary.contains(point):
                found_points.append(point)
        # ... and if this node has children, search them too.
        if self.divided:
            self.nw.query(target_boundary, found_points)
            self.ne.query(target_boundary, found_points)
            self.se.query(target_boundary, found_points)
            self.sw.query(target_boundary, found_points)
        return found_points

