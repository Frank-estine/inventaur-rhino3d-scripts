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
