import gmsh
import sys
# Initialize Gmsh
gmsh.initialize()
# Create a new model
gmsh.model.add("step_model")
# Path to the STEP file
step_file = "test-model-1.stp"
# Import the STEP file
gmsh.model.occ.importShapes(step_file)
gmsh.model.occ.synchronize()
# Set mesh size
gmsh.option.setNumber("Mesh.CharacteristicLengthMin", 0.1)
gmsh.option.setNumber("Mesh.CharacteristicLengthMax", 1.0)
# Generate the mesh
gmsh.model.mesh.generate(3)  # Use 3 for 3D mesh
# Write the mesh to a file
gmsh.write("mesh.msh")
# Optionally save the model as a new STEP file
gmsh.write("test-model-1-modified.step")
# Finalize the Gmsh API
gmsh.finalize()
