# Python API 2.0
# modules found in "maya.api" e.g. maya.api.OpenMaya
import maya.api.OpenMaya as om2

om2.MGlobal.displayError("API 2.0 Error")

# Python API 1.0 (legacy - only use if not supported by Python API 2.0)
# modules found in "maya" e.g. maya.OpenMaya

# import maya.OpenMaya as om1
import maya.OpenMaya as om1

om1.MGlobal.displayError("API 1.0 Error")
