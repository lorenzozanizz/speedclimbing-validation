"""


"""

import gpu
from gpu_extras.batch import batch_for_shader
import bpy

# Get total frames
scene = bpy.context.scene
start_frame = scene.frame_start
end_frame = scene.frame_end


shader = gpu.shader.from_builtin('POLYLINE_UNIFORM_COLOR')
handler = None

FOOTAGE_ID = 1

def draw_skeleton():
    """

    :return:
    """
    head = bpy.data.objects[f'{FOOTAGE_ID} Head Point'].location
    ls = bpy.data.objects[f'{FOOTAGE_ID} Left Shoulder'].location
    rs = bpy.data.objects[f'{FOOTAGE_ID} Right Shoulder'].location
    lh = bpy.data.objects[f'{FOOTAGE_ID} Left Hip'].location
    rh = bpy.data.objects[f'{FOOTAGE_ID} Right Hip'].location
    lk = bpy.data.objects[f'{FOOTAGE_ID} Left Knee'].location
    rk = bpy.data.objects[f'{FOOTAGE_ID} Right Knee'].location
    le = bpy.data.objects[f'{FOOTAGE_ID} Left Elbow'].location
    lw = bpy.data.objects[f'{FOOTAGE_ID} Left Wrist'].location
    re = bpy.data.objects[f'{FOOTAGE_ID} Right Elbow'].location
    rw = bpy.data.objects[f'{FOOTAGE_ID} Right Wrist'].location
    la = bpy.data.objects[f'{FOOTAGE_ID} Left Ankle'].location
    ra = bpy.data.objects[f'{FOOTAGE_ID} Right Ankle'].location

    # Each tuple connects a pair of landmarks, recreate a small neat
    # skeleton to visualize
    landmark_coos = [
        head, ls,
        head, rs,
        ls, lh,
        rs, rh,
        lh, lk,
        rh, rk,
        lk, la,
        rk, ra,
        ls, le,
        le, lw,
        rs, re,
        re, rw]

    batch = batch_for_shader(shader, 'LINES', {"pos": landmark_coos})
    # Shader specs
    shader.uniform_float("viewportSize", gpu.state.viewport_get()[2:])
    shader.uniform_float("lineWidth", 3.5)
    shader.uniform_float("color", (1, 1, 0, 1))
    batch.draw(shader)


def register_handler():
    """

    :return:
    """
    global handler
    handler = bpy.types.SpaceView3D.draw_handler_add(draw_skeleton, (), 'WINDOW', 'POST_VIEW')
    print("> Handler registered")


def unregister_handler():
    """

    :return:
    """
    global handler
    if handler:
        bpy.types.SpaceView3D.draw_handler_remove(handler, 'WINDOW')
        handler = None
        print("> Handler removed")


unregister_handler()
register_handler()
print("> Completed")
