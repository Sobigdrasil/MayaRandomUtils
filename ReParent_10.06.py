import maya.cmds as cmds

selection = cmds.ls(selection=True)

if not selection:
    print('please select something')
else:
    child_obj = cmds.ls(selection=True)[0]

    locator = cmds.spaceLocator(name="Parent_Locator")[0]
    cmds.setAttr('Parent_Locator.scale', 5, 5, 5)

    cmds.parentConstraint(child_obj, locator)

    start = (cmds.playbackOptions(query=1, minTime=1))
    end = (cmds.playbackOptions(query=1, maxTime=1))
    cmds.bakeResults("Parent_Locator", t=(start, end), simulation=1)

    cmds.select("Parent_Locator")
    cmds.delete("Parent_Locator_parentConstraint1")

    cmds.parentConstraint(locator, child_obj)

