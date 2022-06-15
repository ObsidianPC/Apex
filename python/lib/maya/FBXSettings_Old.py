FBXSettings = {
    "include_geometry_smoothinggroups" : 
        {
        "PATH": "Export|IncludeGrp|Geometry|SmoothingGroups",
        "TYPE": "Bool",
        "VALUE": "false",
        },

    "include_geometry_hardedges" :
        {
            "PATH"  : "Export|IncludeGrp|Geometry|expHardEdges",
            "TYPE"  : "Bool",
            "VALUE" : "false"
        },
    
    "include_geometry_tangentsandbinormals" :
        {
            "PATH": "Export|IncludeGrp|Geometry|TangentsandBinormals",
            "TYPE": "Bool",
            "VALUE": "false",
        },
	"include_geometry_smoothmesh" :
		{
			"PATH": "Export|IncludeGrp|Geometry|SmoothMesh",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"include_geometry_selectionset" :
		{
			"PATH": "Export|IncludeGrp|Geometry|SelectionSet",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_geometry_blinddata" :
		{
			"PATH": "Export|IncludeGrp|Geometry|BlindData",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"include_geometry_animationonly" :
		{
			"PATH": "Export|IncludeGrp|Geometry|AnimationOnly",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_geometry_instances" :
		{
			"PATH": "Export|IncludeGrp|Geometry|Instances",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_geometry_containerobjects" :
		{
			"PATH": "Export|IncludeGrp|Geometry|ContainerObjects",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"include_geometry_triangulate" :
		{
			"PATH": "Export|IncludeGrp|Geometry|Triangulate",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_geometry_geometrynurbssurfaceas" :
		{
			"PATH": "Export|IncludeGrp|Geometry|GeometryNurbsSurfaceAs",
			"TYPE": "Enum",
			"VALUE": "NURBS",
			"POSSIBLE_VALUES": "NURBS,Interactive Display Mesh,Software Render Mesh",
		},
	"include_animation" :
		{
			"PATH": "Export|IncludeGrp|Animation",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"include_animation_extragrp_usescenename" :
		{
			"PATH": "Export|IncludeGrp|Animation|ExtraGrp|UseSceneName",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_animation_extragrp_removesinglekey" :
		{
			"PATH": "Export|IncludeGrp|Animation|ExtraGrp|RemoveSingleKey",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_animation_extragrp_quaternion" :
		{
			"PATH": "Export|IncludeGrp|Animation|ExtraGrp|Quaternion",
			"TYPE": "Enum",
			"VALUE": "Resample As Euler Interpolation",
			"POSSIBLE_VALUES": "Retain Quaternion Interpolation,Set As Euler Interpolation,Resample As Euler Interpolation",
		},
	"include_animation_bakecomplexanimation" :
		{
			"PATH": "Export|IncludeGrp|Animation|BakeComplexAnimation",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_animation_bakecomplexanimation_bakeframestart" :
		{
			"PATH": "Export|IncludeGrp|Animation|BakeComplexAnimation|BakeFrameStart",
			"TYPE": "Integer",
			"VALUE": "1",
		},
	"include_animation_bakecomplexanimation_bakeframeend" :
		{
			"PATH": "Export|IncludeGrp|Animation|BakeComplexAnimation|BakeFrameEnd",
			"TYPE": "Integer",
			"VALUE": "48",
		},
	"include_animation_bakecomplexanimation_bakeframestep" :
		{
			"PATH": "Export|IncludeGrp|Animation|BakeComplexAnimation|BakeFrameStep",
			"TYPE": "Integer",
			"VALUE": "1",
		},
	"include_animation_bakecomplexanimation_resampleanimationcurves" :
		{
			"PATH": "Export|IncludeGrp|Animation|BakeComplexAnimation|ResampleAnimationCurves",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_animation_deformation" :
		{
			"PATH": "Export|IncludeGrp|Animation|Deformation",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"include_animation_deformation_skins" :
		{
			"PATH": "Export|IncludeGrp|Animation|Deformation|Skins",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"include_animation_deformation_shape" :
		{
			"PATH": "Export|IncludeGrp|Animation|Deformation|Shape",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"include_animation_curvefilter" :
		{
			"PATH": "Export|IncludeGrp|Animation|CurveFilter",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_animation_curvefilter_curvefiltercstkeyredtprec" :
		{
			"PATH": "Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_animation_curvefilter_customkeyreduction_curvefiltercstkeyredtprec" :
		{
			"PATH": "Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|CurveFilterCstKeyRedTPrec",
			"TYPE": "Number",
			"VALUE": "0.000100",
		},
	"include_animation_curvefilter_customkeyreduction_curvefiltercstkeyredrprec" :
		{
			"PATH": "Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|CurveFilterCstKeyRedRPrec",
			"TYPE": "Number",
			"VALUE": "0.009000",
		},
	"include_animation_curvefilter_customkeyreduction_curvefiltercstkeyredsprec" :
		{
			"PATH": "Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|CurveFilterCstKeyRedSPrec",
			"TYPE": "Number",
			"VALUE": "0.004000",
		},
	"include_animation_curvefilter_customkeyreduction_curvefiltercstkeyredoprec" :
		{
			"PATH": "Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|CurveFilterCstKeyRedOPrec",
			"TYPE": "Number",
			"VALUE": "0.009000",
		},
	"include_animation_curvefilter_customkeyreduction_autotangentsonly" :
		{
			"PATH": "Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|AutoTangentsOnly",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"include_animation_pointcache" :
		{
			"PATH": "Export|IncludeGrp|Animation|PointCache",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_animation_constraintsgrp_constraint" :
		{
			"PATH": "Export|IncludeGrp|Animation|ConstraintsGrp|Constraint",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_animation_constraintsgrp_character" :
		{
			"PATH": "Export|IncludeGrp|Animation|ConstraintsGrp|Character",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_cameras" :
		{
			"PATH": "Export|IncludeGrp|CameraGrp|Camera",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"include_lights" :
		{
			"PATH": "Export|IncludeGrp|LightGrp|Light",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"include_embedtexturegrp_embedtexture" :
		{
			"PATH": "Export|IncludeGrp|EmbedTextureGrp|EmbedTexture",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_bindpose" :
		{
			"PATH": "Export|IncludeGrp|BindPose",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"include_pivottonulls" :
		{
			"PATH": "Export|IncludeGrp|PivotToNulls",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_bypassrrsinheritance" :
		{
			"PATH": "Export|IncludeGrp|BypassRrsInheritance",
			"TYPE": "Bool",
			"VALUE": "false",
		},
	"include_inputconnectionsgrp_inputconnections" :
		{
			"PATH": "Export|IncludeGrp|InputConnectionsGrp|InputConnections",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"advanced_unitsgrp_dynamicscaleconversion" :
		{
			"PATH": "Export|AdvOptGrp|UnitsGrp|DynamicScaleConversion",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"advanced_unitsgrp_unitsselector" :
		{
			"PATH": "Export|AdvOptGrp|UnitsGrp|UnitsSelector",
			"TYPE": "Enum",
			"VALUE": "Centimeters",
			"POSSIBLE_VALUES": "Millimeters,Centimeters,Decimeters,Meters,Kilometers,Inches,Feet,Yards,Miles",
		},
	"advanced_axisconvgrp_upaxis" :
		{
			"PATH": "Export|AdvOptGrp|AxisConvGrp|UpAxis",
			"TYPE": "Enum",
			"VALUE": "Y",
			"POSSIBLE_VALUES": "Y,Z",
		},
	"advanced_ui_showwarningsmanager" :
		{
			"PATH": "Export|AdvOptGrp|UI|ShowWarningsManager",
			"TYPE": "Bool",
			"VALUE": "true",
		},
	"advanced_ui_generatelogdata" :
		{
			"PATH": "Export|AdvOptGrp|UI|GenerateLogData",
			"TYPE": "Bool",
			"VALUE": "true",
		},
#	"advanced_fileformat_obj_triangulate" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Obj|Triangulate",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_fileformat_obj_deformation" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Obj|Deformation",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_fileformat_motion_base_motionframecount" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Motion_Base|MotionFrameCount",
#			"TYPE": "Integer",
#			"VALUE": "0",
#		},
#	"advanced_fileformat_motion_base_motionfromglobalposition" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Motion_Base|MotionFromGlobalPosition",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_fileformat_motion_base_motionframerate" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Motion_Base|MotionFrameRate",
#			"TYPE": "Number",
#			"VALUE": "30.000000",
#		},
#	"advanced_fileformat_motion_base_motiongapsasvaliddata" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Motion_Base|MotionGapsAsValidData",
#			"TYPE": "Bool",
#			"VALUE": "false",
#		},
#	"advanced_fileformat_motion_base_motionc3drealformat" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Motion_Base|MotionC3DRealFormat",
#			"TYPE": "Bool",
#			"VALUE": "false",
#		},
#	"advanced_fileformat_motion_base_motionasfsceneowned" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Motion_Base|MotionASFSceneOwned",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_fileformat_biovision_bvh_motiontranslation" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Biovision_BVH|MotionTranslation",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_fileformat_acclaim_asf_motiontranslation" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Acclaim_ASF|MotionTranslation",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_fileformat_acclaim_asf_motionframerateused" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Acclaim_ASF|MotionFrameRateUsed",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_fileformat_acclaim_asf_motionframerange" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Acclaim_ASF|MotionFrameRange",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_fileformat_acclaim_asf_motionwritedefaultasbasetr" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Acclaim_ASF|MotionWriteDefaultAsBaseTR",
#			"TYPE": "Bool",
#			"VALUE": "false",
#		},
#	"advanced_fileformat_acclaim_amc_motiontranslation" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Acclaim_AMC|MotionTranslation",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_fileformat_acclaim_amc_motionframerateused" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Acclaim_AMC|MotionFrameRateUsed",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_fileformat_acclaim_amc_motionframerange" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Acclaim_AMC|MotionFrameRange",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_fileformat_acclaim_amc_motionwritedefaultasbasetr" :
#		{
#			"PATH": "Export|AdvOptGrp|FileFormat|Acclaim_AMC|MotionWriteDefaultAsBaseTR",
#			"TYPE": "Bool",
#			"VALUE": "false",
#		},
	"advanced_fbx_asciifbx" :
		{
			"PATH": "Export|AdvOptGrp|Fbx|AsciiFbx",
			"TYPE": "Enum",
			"VALUE": "Binary",
			"POSSIBLE_VALUES": "Binary,ASCII",
		},
	"advanced_fbx_exportfileversion" :
		{
			"PATH": "Export|AdvOptGrp|Fbx|ExportFileVersion",
			"TYPE": "Alias",
			"VALUE": "FBX201400",
			"POSSIBLE_VALUES": "FBX201600,FBX201400,FBX201300,FBX201200,FBX201100,FBX201000,FBX200900,FBX200611",
		},
#	"advanced_dxf_deformation" :
#		{
#			"PATH": "Export|AdvOptGrp|Dxf|Deformation",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_dxf_triangulate" :
#		{
#			"PATH": "Export|AdvOptGrp|Dxf|Triangulate",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_collada_triangulate" :
#		{
#			"PATH": "Export|AdvOptGrp|Collada|Triangulate",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_collada_singlematrix" :
#		{
#			"PATH": "Export|AdvOptGrp|Collada|SingleMatrix",
#			"TYPE": "Bool",
#			"VALUE": "true",
#		},
#	"advanced_collada_framerate" :
#		{
#			"PATH": "Export|AdvOptGrp|Collada|FrameRate",
#			"TYPE": "Number",
#			"VALUE": "30.000000",
#		}	
    }