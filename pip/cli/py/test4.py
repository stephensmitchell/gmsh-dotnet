import gmsh
import sys
# Initialize Gmsh
gmsh.initialize()
# Create a new model
gmsh.model.add("3D_mesh_example")
# Define the corner points of the cube
lc = 1.0  # Characteristic length
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(1, 1, 0, lc, 3)
gmsh.model.geo.addPoint(0, 1, 0, lc, 4)
gmsh.model.geo.addPoint(0, 0, 1, lc, 5)
gmsh.model.geo.addPoint(1, 0, 1, lc, 6)
gmsh.model.geo.addPoint(1, 1, 1, lc, 7)
gmsh.model.geo.addPoint(0, 1, 1, lc, 8)
# Define the lines of the cube
gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)
gmsh.model.geo.addLine(5, 6, 5)
gmsh.model.geo.addLine(6, 7, 6)
gmsh.model.geo.addLine(7, 8, 7)
gmsh.model.geo.addLine(8, 5, 8)
gmsh.model.geo.addLine(1, 5, 9)
gmsh.model.geo.addLine(2, 6, 10)
gmsh.model.geo.addLine(3, 7, 11)
gmsh.model.geo.addLine(4, 8, 12)
# Define the surfaces of the cube
gmsh.model.geo.addCurveLoop([1, 10, -5, -9], 1)
gmsh.model.geo.addCurveLoop([2, 11, -6, -10], 2)
gmsh.model.geo.addCurveLoop([3, 12, -7, -11], 3)
gmsh.model.geo.addCurveLoop([4, 9, -8, -12], 4)
gmsh.model.geo.addCurveLoop([5, 6, 7, 8], 5)
gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 6)
gmsh.model.geo.addPlaneSurface([1], 1)
gmsh.model.geo.addPlaneSurface([2], 2)
gmsh.model.geo.addPlaneSurface([3], 3)
gmsh.model.geo.addPlaneSurface([4], 4)
gmsh.model.geo.addPlaneSurface([5], 5)
gmsh.model.geo.addPlaneSurface([6], 6)
# Define the volume of the cube
gmsh.model.geo.addSurfaceLoop([1, 2, 3, 4, 5, 6], 1)
gmsh.model.geo.addVolume([1])
# Synchronize to create the geometry
gmsh.model.geo.synchronize()
# Generate the 3D mesh
gmsh.model.mesh.generate(3)
# Write the mesh to a file
gmsh.write("cube.msh")
# Optionally save the model as a new STEP file
gmsh.write("cube.ply")
# Finalize the Gmsh API
gmsh.finalize()
