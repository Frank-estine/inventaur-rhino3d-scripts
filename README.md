# Inventaur Rhino3D Scripts

Reusable Rhino 9 drafting standards and startup automation maintained by Inventaur Inc.

This public repository contains first-party scripts and documentation under a proprietary commercial licence. It is not an open-source release. Read LICENSE.md before using the code.

## Components

- RhinoStandards/AutoLayer — Rhino startup entrypoint and annotation/hatch routing.
- RhinoStandards/Installer — metric layers/styles/hatch standards installer and local template generator.
- RhinoStandards/Template — template-generation and local deployment notes; generated 3DM is not redistributed.
- RhinoStandards/HatchLibrary — exporter for Rhino's 59 native hatch definitions; PAT payload is not redistributed.
- RhinoStandards/Legacy — historical v1.0 router for reference only.

## Requirements

- Windows
- Rhino 9
- Rhino's bundled RhinoCommon and rhinoscriptsyntax
- Optional: RhinoAI MCP Platform for automatic MCPStart

## Install

1. Obtain a valid Rhino installation.
2. Copy the AutoLayer and Installer scripts into the user's Documents/Inventaur/Rhino Standards folder.
3. In Rhino, run Inventaur_RhinoAutoLayer.py using the RunPythonScript command.
4. The installer adds Rhino's native hatch defaults and creates or validates the metric template locally. It does not change units in an existing model.
5. Configure Rhino Options > General > Startup Commands to run the AutoLayer entrypoint on future launches.

The source uses private component folders and individual READMEs. The deployed runtime remains flat because the Rhino startup entrypoint and installer expect their resources side-by-side.

## Hatch library

The installer uses Rhino's installed native hatch definitions; no McNeel hatch content is bundled in this repository. Run RhinoStandards/HatchLibrary/Inventaur_ExportRhinoDefaultHatches.py inside Rhino to create a local 59-definition PAT file. The generated file is written to the user's Documents runtime folder and is not committed.

McNeel publishes hatch information and a free-to-use Rhino hatch file at https://wiki.mcneel.com/rhino/hatch. Review McNeel's terms for any use or redistribution of its material.

## Behaviour

- Text and text dots route to TEXT.
- Dimensions and leaders route to ANNOTATIONS.
- Hatch objects route to HATCH.
- Ordinary geometry keeps its current layer.
- Existing document units and tolerances are preserved.
- The metric template is generated locally when missing; normal startup validates and reuses it.

## Licensing

Inventaur-authored source and documentation are proprietary. Commercial deployment requires a separate written commercial licence from Inventaur Inc. Public visibility does not grant an open-source licence. Third-party applications and materials remain subject to their respective owners' terms.

Commercial licensing information: https://inventaur.in
