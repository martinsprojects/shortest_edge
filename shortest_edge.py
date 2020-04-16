# find shortest edge
import bpy
from bpy import context
from mathutils import Vector

obj = context.active_object

vectors = []
arrow = []
edgeslength = []
edgeindex = None
indexsel = 0
shortestedge = 0

for e in range(len(obj.data.edges)):
    edge = obj.data.edges[e]
    for i in range(2):
        edgeverts = edge.vertices[i]
        v = obj.data.vertices[edgeverts]
        co_final = obj.matrix_world @ v.co
        arrow.append(co_final)
    vectors.append(arrow)
    arrow = []

for p in range(len(vectors)):
    edgevec = vectors[p][1] - vectors[p][0]
    veclength = edgevec.length
    edgeslength.append(veclength)

for i in edgeslength:
    if edgeindex == None:
        edgeindex = i
    if i < edgeindex:
        edgeindex = i
        shortestedge = indexsel
    indexsel += 1
            
print(shortestedge)
obj.data.edges[shortestedge].select = True

bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')