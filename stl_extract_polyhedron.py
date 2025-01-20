
"""

STL to Polyhedron


Author: mosselini1 (https://www.printables.com/@mosselini1_1346202 & https://makerworld.com/en/@mosselini1)
Date: 20/01/25
"""

import numpy as np
from stl import mesh # numpy-stl module

def np_point_conv(np_point):
	return tuple([float(elem) for elem in np_point])

def get_points_and_faces_from_mesh(stl_mesh):
	#get all unique points
	points = np.unique(stl_mesh.vectors.reshape([int(stl_mesh.vectors.size/3), 3]), axis=0)

	#give all points an unique id
	points_dict = {np_point_conv(point):p for p,point in enumerate(list(points))} # dictionnary matching points with an id

	faces = stl_mesh.vectors
	rel_faces = []
	for face in faces: #for each face replace each point by its id
		rel_face = [ points_dict[np_point_conv(f_point)] for f_point in face ]
		rel_faces.append(rel_face)
	
	return [list(point) for point in points_dict.keys()],rel_faces

def write_openscad_file(points,faces,outpath):
	with open(outpath,"w") as f:
		f.write("module model() {polyhedron(\n")
		f.write(f"points={points},\n")
		f.write(f"faces={faces}")
		f.write(");}\n")
		f.write("model();")

def main():
	stl_mesh = mesh.Mesh.from_file("model.stl") # import input mesh
	points,faces = get_points_and_faces_from_mesh(stl_mesh)
	write_openscad_file(points,faces,"model_data.scad") # write output file
	
if __name__ == "__main__": main()
