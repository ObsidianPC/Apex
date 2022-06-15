import lib.pyperclip as clipboard

fbxSettingsText = """  FBXSettings() for Maya 2020
// PATH: Import|PlugInGrp|PlugInUIWidth    ( TYPE: Integer ) ( VALUE: 500 ) // 
// PATH: Import|PlugInGrp|PlugInUIHeight    ( TYPE: Integer ) ( VALUE: 500 ) // 
// PATH: Import|PlugInGrp|PlugInUIXpos    ( TYPE: Integer ) ( VALUE: 100 ) // 
// PATH: Import|PlugInGrp|PlugInUIYpos    ( TYPE: Integer ) ( VALUE: 100 ) // 
// PATH: Import|PlugInGrp|UILIndex    ( TYPE: Enum )  ( VALUE: "ENU" )  (POSSIBLE VALUES: "ENU" "DEU" "FRA" "JPN" "KOR" "CHS" "PTB"  ) // 
// PATH: Import|IncludeGrp|MergeMode    ( TYPE: Enum )  ( VALUE: "Add and update animation" )  (POSSIBLE VALUES: "Add" "Add and update animation" "Update animation"  ) // 
// PATH: Import|IncludeGrp|Geometry|UnlockNormals    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Import|IncludeGrp|Geometry|HardEdges    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Import|IncludeGrp|Geometry|BlindData    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|IncludeGrp|Animation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// bugged PATH: Import|IncludeGrp|Animation|ExtraGrp|Take    ( TYPE: Enum )  ( VALUE: "" )  (POSSIBLE VALUES:  ) // 
// PATH: Import|IncludeGrp|Animation|ExtraGrp|TimeLine    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Import|IncludeGrp|Animation|ExtraGrp|BakeAnimationLayers    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|IncludeGrp|Animation|ExtraGrp|Markers    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Import|IncludeGrp|Animation|ExtraGrp|Quaternion    ( TYPE: Enum )  ( VALUE: "Resample As Euler Interpolation" )  (POSSIBLE VALUES: "Retain Quaternion Interpolation" "Set As Euler Interpolation" "Resample As Euler Interpolation"  ) // 
// PATH: Import|IncludeGrp|Animation|ExtraGrp|ProtectDrivenKeys    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Import|IncludeGrp|Animation|ExtraGrp|DeformNullsAsJoints    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|IncludeGrp|Animation|ExtraGrp|NullsToPivot    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|IncludeGrp|Animation|ExtraGrp|PointCache    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|IncludeGrp|Animation|Deformation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|IncludeGrp|Animation|Deformation|Skins    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|IncludeGrp|Animation|Deformation|Shape    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|IncludeGrp|Animation|Deformation|ForceWeightNormalize    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Import|IncludeGrp|Animation|SamplingPanel|SamplingRateSelector    ( TYPE: Enum )  ( VALUE: "Scene" )  (POSSIBLE VALUES: "Scene" "File" "Custom"  ) // 
// PATH: Import|IncludeGrp|Animation|SamplingPanel|CurveFilterSamplingRate    ( TYPE: Number ) ( VALUE: 30.000000 ) // 
// PATH: Import|IncludeGrp|Animation|CurveFilter    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Import|IncludeGrp|Animation|ConstraintsGrp|Constraint    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Import|IncludeGrp|Animation|ConstraintsGrp|CharacterType    ( TYPE: Enum )  ( VALUE: "HumanIK" )  (POSSIBLE VALUES: "None" "HumanIK"  ) // 
// PATH: Import|IncludeGrp|CameraGrp|Camera    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|IncludeGrp|LightGrp|Light    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|IncludeGrp|Audio    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|UnitsGrp|DynamicScaleConversion    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|UnitsGrp|UnitsSelector    ( TYPE: Enum )  ( VALUE: "Millimeters" )  (POSSIBLE VALUES: "Millimeters" "Centimeters" "Decimeters" "Meters" "Kilometers" "Inches" "Feet" "Yards" "Miles"  ) // 
// PATH: Import|AdvOptGrp|AxisConvGrp|AxisConversion    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Import|AdvOptGrp|AxisConvGrp|UpAxis    ( TYPE: Enum )  ( VALUE: "Y" )  (POSSIBLE VALUES: "Y" "Z"  ) // 
// PATH: Import|AdvOptGrp|UI|ShowWarningsManager    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|UI|GenerateLogData    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Obj|ReferenceNode    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Max_3ds|ReferenceNode    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Max_3ds|Texture    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Max_3ds|Material    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Max_3ds|Animation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Max_3ds|Mesh    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Max_3ds|Light    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Max_3ds|Camera    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Max_3ds|AmbientLight    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Max_3ds|Rescaling    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Max_3ds|Filter    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Max_3ds|Smoothgroup    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Motion_Base|MotionFrameCount    ( TYPE: Integer ) ( VALUE: 0 ) // 
// PATH: Import|AdvOptGrp|FileFormat|Motion_Base|MotionFrameRate    ( TYPE: Number ) ( VALUE: 0.000000 ) // 
// PATH: Import|AdvOptGrp|FileFormat|Motion_Base|MotionActorPrefix    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Motion_Base|MotionRenameDuplicateNames    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Motion_Base|MotionExactZeroAsOccluded    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Motion_Base|MotionSetOccludedToLastValidPos    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Motion_Base|MotionAsOpticalSegments    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Motion_Base|MotionASFSceneOwned    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Biovision_BVH|MotionCreateReferenceNode    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|MotionAnalysis_HTR|MotionCreateReferenceNode    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|MotionAnalysis_HTR|MotionBaseTInOffset    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|MotionAnalysis_HTR|MotionBaseRInPrerotation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Acclaim_ASF|MotionCreateReferenceNode    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Acclaim_ASF|MotionDummyNodes    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Acclaim_ASF|MotionLimits    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Acclaim_ASF|MotionBaseTInOffset    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Acclaim_ASF|MotionBaseRInPrerotation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Acclaim_AMC|MotionCreateReferenceNode    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Acclaim_AMC|MotionDummyNodes    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Acclaim_AMC|MotionLimits    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Acclaim_AMC|MotionBaseTInOffset    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|FileFormat|Acclaim_AMC|MotionBaseRInPrerotation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|Dxf|WeldVertices    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|Dxf|ObjectDerivation    ( TYPE: Enum )  ( VALUE: "By layer" )  (POSSIBLE VALUES: "By layer" "By entity" "By block"  ) // 
// PATH: Import|AdvOptGrp|Dxf|ReferenceNode    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Import|AdvOptGrp|Performance|RemoveBadPolysFromMesh    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|PlugInGrp|PlugInUIWidth    ( TYPE: Integer ) ( VALUE: 500 ) // 
// PATH: Export|PlugInGrp|PlugInUIHeight    ( TYPE: Integer ) ( VALUE: 500 ) // 
// PATH: Export|PlugInGrp|PlugInUIXpos    ( TYPE: Integer ) ( VALUE: 100 ) // 
// PATH: Export|PlugInGrp|PlugInUIYpos    ( TYPE: Integer ) ( VALUE: 100 ) // 
// PATH: Export|PlugInGrp|UILIndex    ( TYPE: Enum )  ( VALUE: "ENU" )  (POSSIBLE VALUES: "ENU" "DEU" "FRA" "JPN" "KOR" "CHS" "PTB"  ) // 
// PATH: Export|IncludeGrp|Geometry|SmoothingGroups    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Geometry|expHardEdges    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Geometry|TangentsandBinormals    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Geometry|SmoothMesh    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|Geometry|SelectionSet    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Geometry|BlindData    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|Geometry|AnimationOnly    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Geometry|Instances    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Geometry|ContainerObjects    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|Geometry|Triangulate    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Geometry|GeometryNurbsSurfaceAs    ( TYPE: Enum )  ( VALUE: "NURBS" )  (POSSIBLE VALUES: "NURBS" "Interactive Display Mesh" "Software Render Mesh"  ) // 
// PATH: Export|IncludeGrp|Animation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|Animation|ExtraGrp|UseSceneName    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Animation|ExtraGrp|RemoveSingleKey    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Animation|ExtraGrp|Quaternion    ( TYPE: Enum )  ( VALUE: "Resample As Euler Interpolation" )  (POSSIBLE VALUES: "Retain Quaternion Interpolation" "Set As Euler Interpolation" "Resample As Euler Interpolation"  ) // 
// PATH: Export|IncludeGrp|Animation|BakeComplexAnimation    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Animation|BakeComplexAnimation|BakeFrameStart    ( TYPE: Integer ) ( VALUE: 0 ) // 
// PATH: Export|IncludeGrp|Animation|BakeComplexAnimation|BakeFrameEnd    ( TYPE: Integer ) ( VALUE: 60 ) // 
// PATH: Export|IncludeGrp|Animation|BakeComplexAnimation|BakeFrameStep    ( TYPE: Integer ) ( VALUE: 1 ) // 
// PATH: Export|IncludeGrp|Animation|BakeComplexAnimation|ResampleAnimationCurves    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Animation|BakeComplexAnimation|HideComplexAnimationBakedWarning    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Animation|Deformation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|Animation|Deformation|Skins    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|Animation|Deformation|Shape    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|Animation|Deformation|ShapeAttributes    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Animation|Deformation|ShapeAttributes|ShapeAttributesValues    ( TYPE: Enum )  ( VALUE: "Relative" )  (POSSIBLE VALUES: "Relative" "Absolute"  ) // 
// PATH: Export|IncludeGrp|Animation|CurveFilter    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|CurveFilterCstKeyRedTPrec    ( TYPE: Number ) ( VALUE: 0.000090 ) // 
// PATH: Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|CurveFilterCstKeyRedRPrec    ( TYPE: Number ) ( VALUE: 0.009000 ) // 
// PATH: Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|CurveFilterCstKeyRedSPrec    ( TYPE: Number ) ( VALUE: 0.004000 ) // 
// PATH: Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|CurveFilterCstKeyRedOPrec    ( TYPE: Number ) ( VALUE: 0.009000 ) // 
// PATH: Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|AutoTangentsOnly    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|Animation|PointCache    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Animation|PointCache|SelectionSetNameAsPointCache    ( TYPE: Enum )  ( VALUE: " " )  (POSSIBLE VALUES: " "  ) // 
// PATH: Export|IncludeGrp|Animation|ConstraintsGrp|Constraint    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|Animation|ConstraintsGrp|Character    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|CameraGrp|Camera    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|LightGrp|Light    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|Audio    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|EmbedTextureGrp|EmbedTexture    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|BindPose    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|PivotToNulls    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|BypassRrsInheritance    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|IncludeGrp|InputConnectionsGrp|IncludeChildren    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|IncludeGrp|InputConnectionsGrp|InputConnections    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|UnitsGrp|DynamicScaleConversion    ( TYPE: Bool ) ( VALUE: "true" ) // 
// bugged PATH: Export|AdvOptGrp|UnitsGrp|UnitsSelector    ( TYPE: Enum )  ( VALUE: "" )  (POSSIBLE VALUES:  ) // 
// PATH: Export|AdvOptGrp|AxisConvGrp|UpAxis    ( TYPE: Enum )  ( VALUE: "Y" )  (POSSIBLE VALUES: "Y" "Z"  ) // 
// PATH: Export|AdvOptGrp|UI|ShowWarningsManager    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|UI|GenerateLogData    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Obj|Triangulate    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Obj|Deformation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Motion_Base|MotionFrameCount    ( TYPE: Integer ) ( VALUE: 0 ) // 
// PATH: Export|AdvOptGrp|FileFormat|Motion_Base|MotionFromGlobalPosition    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Motion_Base|MotionFrameRate    ( TYPE: Number ) ( VALUE: 30.000000 ) // 
// PATH: Export|AdvOptGrp|FileFormat|Motion_Base|MotionGapsAsValidData    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Motion_Base|MotionC3DRealFormat    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Motion_Base|MotionASFSceneOwned    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Biovision_BVH|MotionTranslation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Acclaim_ASF|MotionTranslation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Acclaim_ASF|MotionFrameRateUsed    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Acclaim_ASF|MotionFrameRange    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Acclaim_ASF|MotionWriteDefaultAsBaseTR    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Acclaim_AMC|MotionTranslation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Acclaim_AMC|MotionFrameRateUsed    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Acclaim_AMC|MotionFrameRange    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|FileFormat|Acclaim_AMC|MotionWriteDefaultAsBaseTR    ( TYPE: Bool ) ( VALUE: "false" ) // 
// PATH: Export|AdvOptGrp|Fbx|AsciiFbx    ( TYPE: Enum )  ( VALUE: "Binary" )  (POSSIBLE VALUES: "Binary" "ASCII"  ) // 
// PATH: Export|AdvOptGrp|Fbx|ExportFileVersion    ( TYPE: Alias )  ( VALUE: "FBX202000" )  (POSSIBLE VALUES: "FBX202000" "FBX201900" "FBX201800" "FBX201600" "FBX201400" "FBX201300" "FBX201200" "FBX201100" "FBX201000" "FBX200900" "FBX200611"  ) // 
// PATH: Export|AdvOptGrp|Dxf|Deformation    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|Dxf|Triangulate    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|Collada|Triangulate    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|Collada|SingleMatrix    ( TYPE: Bool ) ( VALUE: "true" ) // 
// PATH: Export|AdvOptGrp|Collada|FrameRate    ( TYPE: Number ) ( VALUE: 30.000000 ) // 
"""

"""
We need this script to parse through the output of the mel command FBXProperties() 
"""

settingsLines = fbxSettingsText.split("\n")

FBXSettings = dict()


class FBXSetting:
    def __init__(self):
        self.path = None
        self.type = None
        self.value = None
        self.possible_values = list()

    def __str__(self):
        srep = "\t\"" + str(self.path) + "\" :" + "\n"
        srep += "\t\t{\n"
        srep += "\t\t\"PATH\": " + "\"" + str(self.path) + "\"," + "\n"
        srep += "\t\t\"TYPE\": " + "\"" + str(self.type) + "\"," + "\n"
        srep += "\t\t\"VALUE\": " + "\"" + str(self.value) + "\"" 

        if len(self.possible_values) > 0:
            srep += ",\n" + "\t\t\"POSSIBLE_VALUES\": " + "\""
            
            for i in range(0, len(self.possible_values)):
                srep += self.possible_values[i]

                if i < (len(self.possible_values) - 1):
                    srep += ","
                
            srep += "\""
                
        srep += "\n"            
        
        srep += "\t\t}"
        
        return srep


settingsCollection = dict()

for line in settingsLines:
    if ("PATH:" in line):
        #print( "original Line: " + line)

        line = line.replace("//", "")
        line = line.replace(" PATH: ", "")

        pieces = line.split("(")

        setting = FBXSetting()

        for i in range(0, len(pieces)):
            s = pieces[i]
            
            s = s.replace(")", "")
            s = s.strip()

            
            if i == 0:
                setting.path = s
            else:
                sub_pieces = s.split(":")
                
                if sub_pieces[0] == "TYPE":
                    v = sub_pieces[1].strip()
                    setting.type = v
                elif sub_pieces[0] == "VALUE":
                    v = sub_pieces[1].strip()
                    v = v.replace("\"", "")
                    setting.value = v
                elif sub_pieces[0] == "POSSIBLE VALUES":
                    vlist = sub_pieces[1].split("\" \"")
                    for v in vlist:
                        v = v.replace("\"", "")
                        v = v.strip()
                        setting.possible_values.append(v)
        
        settingsCollection[setting.path] = setting
        

def copyFBXSettingsToClipboard():
    result = ""
    result += "FBXSettings = {\n"

    for k,v in enumerate(settingsCollection):
        result += str(settingsCollection[v]) + ",\n"
    
    result += ("}\n")

    clipboard.copy(result)

