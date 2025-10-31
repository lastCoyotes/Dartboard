##################
# DartboardViewer contains any functions necessary to
# render a Dartboard graphic. There are functions to
# resize, repaint, and draw points on the board when
# clicked.
##################
import math

from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QPainter, QPen, QBrush, QPolygon, QFont
from PySide2.QtWidgets import QGraphicsView, QGraphicsScene


##
# DartboardViewer class inherits QGraphicsView
# and adds additional functionality to represent
# a clickable and resizable dartboard.

class DartboardViewer(QGraphicsView):

    ##
    # constructor for QGraphicsView subclass
    def __init__(self, parent=None):

        # call parent constructor
        super().__init__(parent)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)

        # set and set scene for QGraphicsView
        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(QBrush(Qt.white))
        self.setScene(self.scene)

        # set variables and constants

        self.WindowSizeX = 300
        self.WindowSizeY = 300
        self.WindowPosX = 300
        self.WindowPosY = 300

        # this variable sets the number of vertices within each rendered circle
        # it must be a multiple of 20 to paint the dartboard correctly
        self.regionVertices = 2000

        # this variable defines the number of regions on a dartboard
        self.regions = 20

        self.radius = 0
        self.scores = ["6", "10", "15", "2", "17", "3", "19", "7", "16", "8", "11", "14", "9", "12", "5", "20", "1",
                       "18", "4", "13"]

        # this list holds the points
        self.points = {}


        # this variable holds the index of the dart thrown
        self.dart_index = 0

        # sets initial geometry for the window
        self.setGeometry(self.WindowPosX, self.WindowPosY, self.WindowSizeX, self.WindowSizeY)

        # draws the circles and dots for the first time
        self.DrawRegions()

        # shows the window
        self.show()
    
    # this function is called when the window is resized
    def resizeEvent(self, event):
        # print(self.sceneRect())

        # these lines set the variables initialized in the constructor to their new values
        self.WindowSizeX = event.size().width()
        self.WindowSizeY = event.size().height()
        self.WindowPosX = self.pos().x()
        self.WindowPosY = self.pos().y()

        # this line sets the Scene's geometry based on the newly resized window
        self.scene.setSceneRect(self.WindowPosX, self.WindowPosY, self.WindowSizeX, self.WindowSizeY)

        # recall the drawing function to replace the circles and points with the new size
        self.DrawRegions()

        super().resizeEvent(event)

    # helper used to calculate circular coordinates
    def GetPointsInCircle(self, r, n=20):
        n = self.regionVertices
        pi = math.pi
        points = [QPoint(math.cos(2 * pi / n * x) * r + self.WindowPosX + (self.WindowSizeX / 2.0),
                         math.sin(2 * pi / n * x) * r + self.WindowPosY + (self.WindowSizeY / 2.0)) for x in
                  range(0, n + 1)]
        for p in points:
            self.rotate(p, -pi / 20)
        return points

    def rotate(self, point, angle):
        # Get Center of Dartboard
        centerX = self.WindowPosX + (self.WindowSizeX / 2.0)
        centerY = self.WindowPosY + (self.WindowSizeY / 2.0)

        # Calculate important trig information
        sin = math.sin(angle)
        cos = math.cos(angle)

        # Offset points so the center is the origin
        px = point.x() - centerX
        py = point.y() - centerY

        # Calculate new rotated points
        xnew = (px * cos) - (py * sin)
        ynew = (px * sin) + (py * cos)

        # Update actual point data
        point.setX(xnew + centerX)
        point.setY(ynew + centerY)

    # function used to draw all the shapes
    def DrawRegions(self):

        Pen = QPen()
        Pen.setColor(Qt.black)
        Pen.setWidth(3)

        # clear the scene
        self.scene.clear()
        if (self.WindowSizeX <= self.WindowSizeY):
            self.radius = self.WindowSizeX / 2
        else:
            self.radius = self.WindowSizeY / 2

        # create polygon and add points to it
        border_points = self.GetPointsInCircle(self.radius)
        self.border = QPolygon(border_points)

        # create polygon and add points to it
        double_out_points = self.GetPointsInCircle(self.radius * 0.75)
        self.double_out = QPolygon(double_out_points)

        # create polygon and add points to it
        double_in_points = self.GetPointsInCircle(self.radius * 0.70)
        self.double_in = QPolygon(double_in_points)

        # create polygon and add points to it
        triple_out_points = self.GetPointsInCircle(self.radius * 0.48)
        self.triple_out = QPolygon(triple_out_points)

        # create polygon and add points to it
        triple_in_points = self.GetPointsInCircle(self.radius * 0.43)
        self.triple_in = QPolygon(triple_in_points)

        # create polygon and add points to it
        outer_bullseye_points = self.GetPointsInCircle(self.radius * 0.08)
        self.outer_bullseye = QPolygon(outer_bullseye_points)

        # create polygon and add points to it
        bullseye_points = self.GetPointsInCircle(self.radius * 0.03)
        self.bullseye = QPolygon(bullseye_points)

        self.inner_regions = []

        for i in range(self.regions):
            dpoints = []
            endpoint = QPoint()
            for j in range(i * (self.regionVertices // self.regions),
                           i * (self.regionVertices // self.regions) + (self.regionVertices // self.regions) + 1):
                dpoints.append(outer_bullseye_points[j])
            for j in range(i * (self.regionVertices // self.regions) + (self.regionVertices // self.regions),
                           i * (self.regionVertices // self.regions) - 1, -1):
                dpoints.append(triple_in_points[j])

            dpoints.append(outer_bullseye_points[i * (self.regionVertices // self.regions)])

            self.inner_regions.append(QPolygon(dpoints))

        color = True
        for i in self.inner_regions:
            if (color):
                self.scene.addPolygon(i, Pen, QBrush(Qt.white))
            else:
                self.scene.addPolygon(i, Pen, QBrush(Qt.black))
            color = not color

        self.triples_regions = []
        for i in range(self.regions):
            dpoints = []
            endpoint = QPoint()
            for j in range(i * (self.regionVertices // self.regions),
                           i * (self.regionVertices // self.regions) + (self.regionVertices // self.regions) + 1):
                dpoints.append(triple_in_points[j])
            for j in range(i * (self.regionVertices // self.regions) + (self.regionVertices // self.regions),
                           i * (self.regionVertices // self.regions) - 1, -1):
                dpoints.append(triple_out_points[j])

            dpoints.append(triple_in_points[i * (self.regionVertices // self.regions)])

            self.triples_regions.append(QPolygon(dpoints))

        color = True
        for i in self.triples_regions:
            if (color):
                self.scene.addPolygon(i, Pen, QBrush(Qt.red))
            else:
                self.scene.addPolygon(i, Pen, QBrush(Qt.green))
            color = not color

        self.outer_regions = []
        for i in range(self.regions):
            dpoints = []
            endpoint = QPoint()
            for j in range(i * (self.regionVertices // self.regions),
                           i * (self.regionVertices // self.regions) + (self.regionVertices // self.regions) + 1):
                dpoints.append(triple_out_points[j])
            for j in range(i * (self.regionVertices // self.regions) + (self.regionVertices // self.regions),
                           i * (self.regionVertices // self.regions) - 1, -1):
                dpoints.append(double_in_points[j])

            dpoints.append(triple_out_points[i * (self.regionVertices // self.regions)])

            self.outer_regions.append(QPolygon(dpoints))

        color = True
        for i in self.outer_regions:
            if (color):
                self.scene.addPolygon(i, Pen, QBrush(Qt.white))
            else:
                self.scene.addPolygon(i, Pen, QBrush(Qt.black))
            color = not color

        self.doubles_regions = []

        for i in range(self.regions):
            dpoints = []
            endpoint = QPoint()
            for j in range(i * (self.regionVertices // self.regions),
                           i * (self.regionVertices // self.regions) + (self.regionVertices // self.regions) + 1):
                dpoints.append(double_in_points[j])
            for j in range(i * (self.regionVertices // self.regions) + (self.regionVertices // self.regions),
                           i * (self.regionVertices // self.regions) - 1, -1):
                dpoints.append(double_out_points[j])

            dpoints.append(double_in_points[i * (self.regionVertices // self.regions)])

            self.doubles_regions.append(QPolygon(dpoints))

        color = True
        for i in self.doubles_regions:

            if (color):
                self.scene.addPolygon(i, Pen, QBrush(Qt.red))
            else:
                self.scene.addPolygon(i, Pen, QBrush(Qt.green))
            color = not color

        self.border_regions = []

        for i in range(self.regions):
            dpoints = []
            endpoint = QPoint()
            for j in range(i * (self.regionVertices // self.regions),
                           i * (self.regionVertices // self.regions) + (self.regionVertices // self.regions) + 1):
                dpoints.append(double_out_points[j])
            for j in range(i * (self.regionVertices // self.regions) + (self.regionVertices // self.regions),
                           i * (self.regionVertices // self.regions) - 1, -1):
                dpoints.append(border_points[j])

            dpoints.append(double_out_points[i * (self.regionVertices // self.regions)])

            self.border_regions.append(QPolygon(dpoints))

        for i in self.border_regions:
            self.scene.addPolygon(i, Pen, QBrush(Qt.black))

        font = QFont("Helvetica")
        font.setPointSize(12)
        for i in range(self.regions):

            text = self.scene.addText(self.scores[i])
            text.setDefaultTextColor(Qt.white)
            text.setFont(font)
            if (len(self.scores[i]) == 2):
                text.setPos((self.border_regions[i][0].x() + self.border_regions[i][
                    (self.regionVertices // self.regions) + 1].x()) / 2.0 - 10, (
                                        self.border_regions[i][0].y() + self.border_regions[i][
                                    (self.regionVertices // self.regions) + 1].y()) / 2.0 - 10)
            elif (len(self.scores[i]) == 1):
                text.setPos((self.border_regions[i][0].x() + self.border_regions[i][
                    (self.regionVertices // self.regions) + 1].x()) / 2.0 - 5, (
                                        self.border_regions[i][0].y() + self.border_regions[i][
                                    (self.regionVertices // self.regions) + 1].y()) / 2.0 - 5)

        # draw the the bullseyes
        self.scene.addPolygon(self.outer_bullseye, Pen, QBrush(Qt.green))
        self.scene.addPolygon(self.bullseye, Pen, QBrush(Qt.red))

        # calculate and draw the points that were initially placed before resize
  
        for key, value in self.points.items():
            x_dec = self.radius * value[0]
            y_dec = self.radius * value[1]
            self.scene.addEllipse(self.WindowPosX + (self.WindowSizeX / 2.0) + x_dec,
                                  self.WindowPosY + (self.WindowSizeY / 2.0) + y_dec, 3, 3, QPen(), QBrush(Qt.white))

    def set_points(self, points):
        self.points = points
        self.DrawRegions()
