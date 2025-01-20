# STLtoPolyhedron
Code to extract the faces and points of a 3d model stored in a STL file and to create an OpenSCAD polyhedron with it.

This code is useful, for example, when you want to import an STL model into OpenSCAD but don't have access to (or are uncertain about) the filesystem surrounding your file.
This was, for me, the case with MakerWorld having a nice customization system based upon OpenSCAD. This allowed me to make an existing model customizable even if it didn't originate from OpenSCAD. Simply extracting faces and points of STLs can already be useful in many applications requiring 3d rendering, for example.
