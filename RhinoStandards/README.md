# Rhino 9 Standards Package

The metric template, installer, AutoLayer entrypoint and hatch exporter are one shared standards package.

- AutoLayer: startup entrypoint and automatic TEXT / ANNOTATIONS / HATCH routing.
- Installer: installs drafting layers/styles, Rhino native hatch defaults, and generates/validates the local metric template.
- Template: notes for the template generated locally by the installer.
- HatchLibrary: exports native Rhino hatch definitions to a local PAT file.
- Legacy: reference-only legacy router.

Each component has its own README. The public source package does not include generated 3DM or PAT files. Those are generated or stored locally by the user's own Rhino installation.

## Direct GitHub links

- Main repository: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts
- Main README: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/blob/main/README.md
- Rhino standards package folder: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/tree/main/RhinoStandards
- Package README: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/blob/main/RhinoStandards/README.md

### AutoLayer
- Folder: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/tree/main/RhinoStandards/AutoLayer
- README: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/blob/main/RhinoStandards/AutoLayer/README.md
- Raw README: https://raw.githubusercontent.com/Krishna-Inventaur/inventaur-rhino3d-scripts/main/RhinoStandards/AutoLayer/README.md
- Script: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/blob/main/RhinoStandards/AutoLayer/Inventaur_RhinoAutoLayer.py

### Installer
- Folder: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/tree/main/RhinoStandards/Installer
- README: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/blob/main/RhinoStandards/Installer/README.md
- Raw README: https://raw.githubusercontent.com/Krishna-Inventaur/inventaur-rhino3d-scripts/main/RhinoStandards/Installer/README.md
- Script: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/blob/main/RhinoStandards/Installer/Inventaur_RhinoStandards_Install.py

### HatchLibrary
- Folder: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/tree/main/RhinoStandards/HatchLibrary
- README: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/blob/main/RhinoStandards/HatchLibrary/README.md
- Raw README: https://raw.githubusercontent.com/Krishna-Inventaur/inventaur-rhino3d-scripts/main/RhinoStandards/HatchLibrary/README.md
- Script: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/blob/main/RhinoStandards/HatchLibrary/Inventaur_ExportRhinoDefaultHatches.py

### Legacy
- Folder: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/tree/main/RhinoStandards/Legacy
- README: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/blob/main/RhinoStandards/Legacy/README.md
- Raw README: https://raw.githubusercontent.com/Krishna-Inventaur/inventaur-rhino3d-scripts/main/RhinoStandards/Legacy/README.md
- Script: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/blob/main/RhinoStandards/Legacy/Inventaur_RhinoAutoLayer_legacy_1_0.py

### Template
- Folder: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/tree/main/RhinoStandards/Template
- README: https://github.com/Krishna-Inventaur/inventaur-rhino3d-scripts/blob/main/RhinoStandards/Template/README.md
- Raw README: https://raw.githubusercontent.com/Krishna-Inventaur/inventaur-rhino3d-scripts/main/RhinoStandards/Template/README.md

---

## Rhino 8 / Rhino 9 MCP startup

The shared AutoLayer entrypoint uses explicit non-interactive port arguments:

- Rhino 8: MCP only on 127.0.0.1:10508; the Rhino 9 standards installer is skipped.
- Rhino 9: applies the drafting standards and starts MCP on 127.0.0.1:10500.

The two ports are distinct so Rhino 8 and Rhino 9 can be open at the same time. See [AutoLayer README](AutoLayer/README.md) for the command, startup configuration and log markers.
