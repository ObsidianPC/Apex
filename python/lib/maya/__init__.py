def SetNodeUIColor(theNode, color, inOutliner=True, inViewport=True):
    if theNode is not None:
        try:
            #TODO: this would be much safer if we checked the node's display layer, removed it is if exists, made the changes, and then re-added the node.
            theNode.useOutlinerColor.set(inOutliner)
            theNode.outlinerColor.set(color)

            theNode.wireColorRGB.set(color)
            theNode.overrideColorRGB.set(color)


            theNode.overrideEnabled.set(inViewport)
            theNode.overrideRGBColors.set(inViewport)
            theNode.useObjectColor.set(inViewport)
        except:
            pass