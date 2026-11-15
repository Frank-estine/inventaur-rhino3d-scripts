# Rhino AutoLayer Startup Entrypoint

Script: Inventaur_RhinoAutoLayer.py
Package version: 1.3.3

Loads the standards installer, registers document/object event handlers and optionally invokes RhinoAI's MCPStart command.

## Routing

- Text entities and text dots route to TEXT.
- Dimensions and leaders route to ANNOTATIONS.
- Hatch objects route to HATCH.
- Curves, points, surfaces, Breps, meshes, SubD, blocks and furniture remain on their existing layers.

This is an annotation/hatch router, not a semantic architectural classifier.

## Install

Copy this script and the Installer script into the user's Documents/Inventaur/Rhino Standards folder. Configure Rhino Options > General > Startup Commands to run this script using RunPythonScript.

Logs are written under the user's LOCALAPPDATA/Inventaur/RhinoStandards/logs folder.

RhinoAI MCP is optional. If installed and loaded, the entrypoint issues MCPStart separately from the standards installer.

## Direct GitHub links

- Main repository: https://github.com/Frank-estine/inventaur-rhino3d-scripts
- Main README: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/README.md
- Rhino standards package: https://github.com/Frank-estine/inventaur-rhino3d-scripts/tree/main/RhinoStandards
- AutoLayer folder: https://github.com/Frank-estine/inventaur-rhino3d-scripts/tree/main/RhinoStandards/AutoLayer
- AutoLayer README: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/AutoLayer/README.md
- Raw AutoLayer README: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/AutoLayer/README.md
- Script: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/AutoLayer/Inventaur_RhinoAutoLayer.py
- Raw script: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/AutoLayer/Inventaur_RhinoAutoLayer.py

Use the **folder URL** to introduce the component, the **README URL** to reference its documentation, and the **raw README URL** when a forum or external page needs the Markdown source.
