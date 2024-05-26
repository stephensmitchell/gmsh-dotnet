import gmsh
import sys
def write_mesh_to_obj(filename, nodes, elements, element_types):
    with open(filename, 'w') as file:
        # Write vertices
        for node in nodes:
            file.write(f"v {node[0]} {node[1]} {node[2]}\n")
        # Write faces (triangles and quadrilaterals)
        for elem_type, element in zip(element_types, elements):
            if elem_type == 2:  # Triangles
                for i in range(0, len(element), 3):
                    file.write(f"f {element[i]+1} {element[i+1]+1} {element[i+2]+1}\n")
            elif elem_type == 3:  # Quadrilaterals
                for i in range(0, len(element), 4):
                    file.write(f"f {element[i]+1} {element[i+1]+1} {element[i+2]+1} {element[i+3]+1}\n")
# Initialize Gmsh
gmsh.initialize()
# Create a new model
gmsh.model.add("3D_mesh_example")
# Define the corner points of the cube using OpenCASCADE
gmsh.model.occ.addBox(0, 0, 0, 1, 1, 1)
# Synchronize the OpenCASCADE CAD kernel with the Gmsh model
gmsh.model.occ.synchronize()
# Set mesh size
gmsh.option.setNumber("Mesh.CharacteristicLengthMin", 0.1)
gmsh.option.setNumber("Mesh.CharacteristicLengthMax", 0.1)
# Generate the 3D mesh
gmsh.model.mesh.generate(3)
# Retrieve mesh nodes and elements
node_tags, node_coords, _ = gmsh.model.mesh.getNodes()
element_types, element_tags, element_node_tags = gmsh.model.mesh.getElements()
# Format node coordinates
nodes = [(node_coords[3*i], node_coords[3*i+1], node_coords[3*i+2]) for i in range(len(node_tags))]
# Flatten the element_node_tags and filter only the triangles and quadrilaterals
elements = []
filtered_types = []
for elem_type, elem_node_tag in zip(element_types, element_node_tags):
    if elem_type in [2, 3]:  # 2 -> triangles, 3 -> quadrilaterals
        elements.append(elem_node_tag)
        filtered_types.append(elem_type)
# Write to OBJ file
write_mesh_to_obj("cube.obj", nodes, elements, filtered_types)
# Finalize the Gmsh API
gmsh.finalize()
