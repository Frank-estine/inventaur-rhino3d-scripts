# Rhino Hatch Library Exporter

This folder includes an exporter script, not a bundled McNeel PAT file.

Run Inventaur_ExportRhinoDefaultHatches.py inside Rhino 9. The script calls RhinoCommon HatchPattern.GetDefaultHatchPatterns() and HatchPattern.WriteToFile() and writes the local PAT file to the user's Documents/Inventaur/Rhino Standards folder.

It reads the saved file back and checks the definition-header count and unique names. The generated PAT remains local and is ignored by Git.

McNeel's free-to-use hatch file is documented at https://wiki.mcneel.com/rhino/hatch. Use McNeel's source and terms for any separately sourced patterns.
