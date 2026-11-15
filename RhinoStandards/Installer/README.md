# Rhino Standards Installer

Script: Inventaur_RhinoStandards_Install.py
Package version: 1.3.3

Installs the shared metric architectural layers, annotation/text styles, Rhino native hatch defaults and object-event routing. It also validates or generates the user's local metric template.

## Native hatch source

The installer gets hatch definitions from Rhino's own HatchPattern.GetDefaultHatchPatterns() API. A PAT file is optional; no McNeel hatch content is bundled in this public repository. If a local PAT file exists next to the runtime script, the installer imports it. If it does not exist, Rhino's native defaults are used.

## Template

If the runtime metric template is missing, the installer generates it locally through a disposable headless Rhino document and saves it under the user's Documents/Inventaur/Rhino Standards folder. Normal startup validates and reuses a valid template; it does not rebuild it.

## Safety

- Existing model units and tolerances are preserved.
- Only explicit template generation creates a millimetre template.
- Existing geometry and ordinary geometry-layer assignments are preserved.
- User-selected custom dimension styles are preserved.
- No geometry is created in the default template.
