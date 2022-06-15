import pymel.core as pm

def moveAToB(A, B):
    savedPosition = B.getPivots(worldSpace=True)[0]
    savedRotate = B.getRotation(space="world")

    # Translate
    piv = A.getPivots(worldSpace=True)[0]
    delta = savedPosition - piv
    A.translateBy(delta)

    # rotate
    A.rotateBy(A.getRotation().inverse())
    A.rotateBy(savedRotate)

class TransformClipboard(object):
    savedTranslate = None
    savedRotate = None
    savedScale = None

    @staticmethod
    def CopyTransform():
        n = None
        sel = pm.selected()
        if len(sel) > 0:
            n = sel[0]

        TransformClipboard.savedPosition = n.getPivots(worldSpace=True)[0]
        TransformClipboard.savedLocalRotate = n.getRotation()
        TransformClipboard.savedRotate = n.getRotation(space="world")
        TransformClipboard.savedScale = n.getScale()

        print ("Saved Translate: %s" % TransformClipboard.savedPosition)
        print ("Saved Rotate: %s" % TransformClipboard.savedRotate)
        print ("Saved Scale: %s" % TransformClipboard.savedScale)

        """
        pivotLocation = m.getPivots(worldSpace=True)[0]
        translation = m.getTranslation()

        originalLocations[m.name()] = translation
        originalPivots[m.name()] = pivotLocation
        m.setTranslation(translation - pivotLocation)
        """

    @staticmethod
    def PasteTransform(PasteTranslate=True, PasteRotate=True, PasteScale=False):
        sel = pm.selected(type="transform")
        pm.select(clear=True)

        with pm.UndoChunk():
            for n in sel:

                if PasteTranslate == True and TransformClipboard.savedPosition is not None:
                    #p = n.getPivots(worldSpace=True)[0]
                    #t = n.getTranslation(space="world")

                    # n.setTranslation(TransformClipboard.savedTranslate, space="world")
                    # n.setTranslation(t - p + TransformClipboard.savedPosition)
                    #newMatrix.setTranslation(t - p + TransformClipboard.savedPosition, space="world")
                    #newMatrix.setTranslation(TransformClipboard.savedPosition, space="world")
                    piv = n.getPivots(worldSpace=True)[0]
                    delta = TransformClipboard.savedPosition - piv
                    n.translateBy(delta)


                if PasteRotate == True and TransformClipboard.savedRotate is not None:
                    #n.setRotation(TransformClipboard.savedRotate, space="world")  #No Undo Ability
                    #pm.delete(pm.orientConstraint(master, slave, maintainOffset=False)) #Hax, and needs saved object to still be opresent
                    n.rotateBy(n.getRotation().inverse())
                    n.rotateBy(TransformClipboard.savedRotate)



                if PasteScale == True and TransformClipboard.savedScale is not None:
                    n.setScale(TransformClipboard.savedScale)

        pm.select(sel)

    @staticmethod
    def PastePivot(PasteTranslate=True, PasteRotate=True):
        sel = pm.selected(type="transform")
        pm.select(clear=True)

        if PasteTranslate == True or PasteRotate == True:
            with pm.UndoChunk():
                for n in sel:
                    
                    if PasteTranslate == True and TransformClipboard.savedPosition is not None:
                        
                        #piv = n.getPivots(worldSpace=True)[0]
                        #delta = TransformClipboard.savedPosition - piv
                        #n.translateBy(delta)

                        n.setPivots(TransformClipboard.savedPosition, worldSpace=True)

                    
                    

                    if PasteRotate == True and TransformClipboard.savedRotate is not None:

                        pm.select(n)

                        print(TransformClipboard.savedRotate)

                        pm.manipPivot(o=TransformClipboard.savedLocalRotate)

                        #n.setRotation(TransformClipboard.savedRotate, space="world")  #No Undo Ability
                        #pm.delete(pm.orientConstraint(master, slave, maintainOffset=False)) #Hax, and needs saved object to still be opresent
                        #n.rotateBy(n.getRotation().inverse())
                        #n.rotateBy(TransformClipboard.savedRotate)

            pm.select(sel)