# Rhino Hatch Library Exporter

This folder includes an exporter script, not a bundled McNeel PAT file.

Run Inventaur_ExportRhinoDefaultHatches.py inside Rhino 9. The script calls RhinoCommon HatchPattern.GetDefaultHatchPatterns() and HatchPattern.WriteToFile() and writes the local PAT file to the user's Documents/Inventaur/Rhino Standards folder.

It reads the saved file back and checks the definition-header count and unique names. The generated PAT remains local and is ignored by Git.

McNeel's free-to-use hatch file is documented at https://wiki.mcneel.com/rhino/hatch. Use McNeel's source and terms for any separately sourced patterns.

## Direct GitHub links

- Main repository: https://github.com/Frank-estine/inventaur-rhino3d-scripts
- Main README: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/README.md
- Rhino standards package: https://github.com/Frank-estine/inventaur-rhino3d-scripts/tree/main/RhinoStandards
- HatchLibrary folder: https://github.com/Frank-estine/inventaur-rhino3d-scripts/tree/main/RhinoStandards/HatchLibrary
- HatchLibrary README: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/HatchLibrary/README.md
- Raw HatchLibrary README: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/HatchLibrary/README.md
- Script: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/HatchLibrary/Inventaur_ExportRhinoDefaultHatches.py
- Raw script: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/HatchLibrary/Inventaur_ExportRhinoDefaultHatches.py

Use the **folder URL** to introduce the component, the **README URL** to reference its documentation, and the **raw README URL** when a forum or external page needs the Markdown source.
