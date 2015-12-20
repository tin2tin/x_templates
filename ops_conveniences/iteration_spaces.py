farther


AREA = 'TEXT_EDITOR'

for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:

        if not area.type == AREA:
            continue

        for s in area.spaces:
            if s.type == AREA:
                # do_something_here
                ...


---------------+-------------------------------------------------------------
bl_space_type  | 'CLIP_EDITOR', 'CONSOLE', 'DOPESHEET_EDITOR', 'EMPTY',
               | 'FILE_BROWSER', 'GRAPH_EDITOR', 'IMAGE_EDITOR', 'INFO',
               | 'LOGIC_EDITOR', 'NLA_EDITOR', 'NODE_EDITOR', 'OUTLINER',
               | 'PROPERTIES', 'SEQUENCE_EDITOR', 'TEXT_EDITOR', 'TIMELINE',
               | 'USER_PREFERENCES', 'VIEW_3D'