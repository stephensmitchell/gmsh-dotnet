import gmsh
import sys
# Initialize gmsh
gmsh.initialize()
# Create a new model
gmsh.model.add("square")
# Define the corner points of the square
lc = 1e-2  # Characteristic length
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(1, 1, 0, lc, 3)
gmsh.model.geo.addPoint(0, 1, 0, lc, 4)
# Define the lines of the square
gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)
# Define the curve loop and the plane surface
gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)
gmsh.model.geo.addPlaneSurface([1], 1)
# Synchronize to create the geometry
gmsh.model.geo.synchronize()
# Generate the mesh
gmsh.model.mesh.generate(2)
# Write the mesh to a file
gmsh.write("square.msh")
# Finalize the gmsh API
gmsh.finalize()
