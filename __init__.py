bl_info = {
    "name": "NFull Geometry Nodes",
    "author": "Nanyin",
    "version": (0, 0),
    "blender": (3, 6, 0),
    "location": "",
    "description": "Adds new Geometry Nodes",
    "warning": "",
    "wiki_url": "",
    "category": "Nodes",
    }
import bpy

class NFullNodeTree(bpy.types.NodeTree):
    bl_idname='NFullNodeTree'
    bl_label='NFull Node Tree'
    bl_icon='BLENDER'

    
class NFullNode(bpy.types.Node):
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'NFullNodeTree'

class TestNode(NFullNode):
    bl_idname = 'TestNode'
    bl_label = 'Simple Input NodeXXX'
    bl_icon = 'PLUS'
    
    intProp = bpy.props.IntProperty()
    def init(self, context):
        self.outputs.new('NodeSocketInt', "output")
        
    def copy(self, node):
        print("copied node", node)
        
    def free(self):
        print("Node removed", self)
        
    def draw_buttons(self, context, layout):
        layout.prop(self, 'intProp')

class TestNode02(NFullNode):
    bl_idname = 'TestNode02'
    bl_label = 'Simple Input Node02'
    bl_icon = 'PLUS'
    
    intProp = bpy.props.IntProperty()
    def init(self, context):
        self.outputs.new('NodeSocketInt', "output")
        
    def copy(self, node):
        print("copied node", node)
        
    def free(self):
        print("Node removed", self)
        
    def draw_buttons(self, context, layout):
        layout.prop(self, 'intProp')
    
import nodeitems_utils

class NFullNodeCategory(nodeitems_utils.NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'NFullNodeTree'
    
node_categories = [
    NFullNodeCategory("CUSTOMINPUTNODES", "Custom Input NodesYYY", items=[
        nodeitems_utils.NodeItem("TestNode"),
        nodeitems_utils.NodeItem("TestNode02"),
        ]),
]

classes=(
        NFullNodeTree,
        TestNode,
        TestNode02,
        )
    
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    nodeitems_utils.register_node_categories("NFULL_NODES", node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories("NFULL_NODES")
    for cls in classes:
        bpy.utils.unregister_class(cls)

