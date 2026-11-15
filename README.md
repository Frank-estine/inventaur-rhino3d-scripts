# Inventaur Rhino3D Scripts

**Inventaur Rhino Standards — version 1.3.3**
Reusable Rhino 9 drafting standards, startup automation, annotation routing and hatch tooling maintained by Inventaur Inc.

This repository contains **four Python scripts**. The current workflow is built around the AutoLayer startup entrypoint and the standards installer. The hatch exporter is an optional utility. The v1.0 router is retained for historical reference and is not part of the current install path.

> **Licence:** This is a public-facing, proprietary commercial source repository. It is **not open-source**. Public visibility is for inspection and evaluation; use, execution, modification, integration or commercial deployment requires a separate written commercial licence from Inventaur Inc. See [LICENSE.md](LICENSE.md).

---

## Direct GitHub links

These absolute URLs are suitable for forum posts, project pages and external documentation. The folder URL opens the component; the README URL opens its documentation; the raw URL serves the Markdown source.

- Main repository: https://github.com/Frank-estine/inventaur-rhino3d-scripts
- Main README: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/README.md
- Raw main README: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/README.md
- Rhino standards package: https://github.com/Frank-estine/inventaur-rhino3d-scripts/tree/main/RhinoStandards
- Rhino standards package README: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/README.md

### AutoLayer
- Folder: https://github.com/Frank-estine/inventaur-rhino3d-scripts/tree/main/RhinoStandards/AutoLayer
- README: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/AutoLayer/README.md
- Raw README: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/AutoLayer/README.md
- Script: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/AutoLayer/Inventaur_RhinoAutoLayer.py
- Raw script: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/AutoLayer/Inventaur_RhinoAutoLayer.py

### Installer
- Folder: https://github.com/Frank-estine/inventaur-rhino3d-scripts/tree/main/RhinoStandards/Installer
- README: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/Installer/README.md
- Raw README: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/Installer/README.md
- Script: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/Installer/Inventaur_RhinoStandards_Install.py
- Raw script: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/Installer/Inventaur_RhinoStandards_Install.py

### HatchLibrary
- Folder: https://github.com/Frank-estine/inventaur-rhino3d-scripts/tree/main/RhinoStandards/HatchLibrary
- README: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/HatchLibrary/README.md
- Raw README: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/HatchLibrary/README.md
- Script: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/HatchLibrary/Inventaur_ExportRhinoDefaultHatches.py
- Raw script: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/HatchLibrary/Inventaur_ExportRhinoDefaultHatches.py

### Legacy
- Folder: https://github.com/Frank-estine/inventaur-rhino3d-scripts/tree/main/RhinoStandards/Legacy
- README: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/Legacy/README.md
- Raw README: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/Legacy/README.md
- Script: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/Legacy/Inventaur_RhinoAutoLayer_legacy_1_0.py
- Raw script: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/Legacy/Inventaur_RhinoAutoLayer_legacy_1_0.py

### Template
- Folder: https://github.com/Frank-estine/inventaur-rhino3d-scripts/tree/main/RhinoStandards/Template
- README: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/RhinoStandards/Template/README.md
- Raw README: https://raw.githubusercontent.com/Frank-estine/inventaur-rhino3d-scripts/main/RhinoStandards/Template/README.md
- Generated template: created locally by the Installer script; no prebuilt 3DM is hosted in this repository.

### Other repository reference files
- Licence: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/LICENSE.md
- Third-party notices: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/THIRD_PARTY_NOTICES.md
- Verification summary: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/VERIFICATION.md
- Manifest: https://github.com/Frank-estine/inventaur-rhino3d-scripts/blob/main/manifest.json

---
## At a glance

| File / component | What it does | When to use it |
|---|---|---|
| [AutoLayer startup script](RhinoStandards/AutoLayer/Inventaur_RhinoAutoLayer.py) | Rhino startup bootstrap. Loads the standards installer and requests the optional RhinoAI MCPStart command. | **Current startup entrypoint.** Configure this to run when Rhino launches. |
| [Standards installer](RhinoStandards/Installer/Inventaur_RhinoStandards_Install.py) | Installs drafting layers, dimension/text styles, hatch definitions and live object-routing handlers; validates or creates the metric template. | The core standards engine. Normally loaded by AutoLayer; can also be run directly for setup or repair. |
| [Native hatch exporter](RhinoStandards/HatchLibrary/Inventaur_ExportRhinoDefaultHatches.py) | Exports hatch definitions available in the installed Rhino version to a local PAT file and JSON report. | Run manually when a local PAT export is needed. |
| [Legacy v1.0 router](RhinoStandards/Legacy/Inventaur_RhinoAutoLayer_legacy_1_0.py) | Historical v1.0 text/annotation layer router. | Reference only. Do not install alongside the current AutoLayer system. |

The [Template folder](RhinoStandards/Template/README.md) documents the metric architectural template generated by the installer. It does **not** contain a separate Python script or a prebuilt 3DM file.

## What the current package does

### 1. Drafting layer structure

The installer defines the following exact layer paths. Rhino creates the required parent groups for the nested paths:

~~~text
00_GUIDES
01_SITE::BOUNDARY
01_SITE::TOPOGRAPHY
01_SITE::LANDSCAPE
02_EXISTING
03_DEMOLITION
04_ARCHITECTURE::GENERAL
04_ARCHITECTURE::WALLS
04_ARCHITECTURE::DOORS
04_ARCHITECTURE::WINDOWS
04_ARCHITECTURE::FLOORS
04_ARCHITECTURE::CEILINGS
04_ARCHITECTURE::STAIRS
04_ARCHITECTURE::ROOFS
05_STRUCTURE::FOUNDATIONS
05_STRUCTURE::COLUMNS
05_STRUCTURE::BEAMS
05_STRUCTURE::SLABS
05_STRUCTURE::BRACING
05_STRUCTURE::CONNECTIONS
06_INTERIORS::PARTITIONS
06_INTERIORS::JOINERY
06_INTERIORS::FINISHES
07_FURNITURE::GENERAL
07_FURNITURE::FIXED
07_FURNITURE::LOOSE
07_FURNITURE::CUSTOM
08_SERVICES::HVAC
08_SERVICES::ELECTRICAL
08_SERVICES::PLUMBING
08_SERVICES::FIRE
TEXT
ANNOTATIONS
HATCH
DETAILS
REFERENCES
PRESENTATION
~~~

The verified template baseline contains **44 layers**. Existing layers are reused rather than blindly duplicated.

### 2. Annotation and hatch routing

The installer applies standards to the active document when it runs, then registers Rhino document event handlers. Documents created or opened afterwards are initialized by those handlers; subsequently added objects are routed as they are created. The AddRhinoObject handler is registered at the Rhino document level.

| Object type | Destination |
|---|---|
| Text entities and text dots | TEXT |
| Dimensions and leaders / Rhino annotation objects | ANNOTATIONS |
| Hatch objects | HATCH |
| Ordinary geometry (curves, points, surfaces, Breps, meshes, SubD, blocks, furniture, etc.) | Remains on its current layer |

This is a **type-based drafting router**, not an architectural or semantic geometry classifier. It does not attempt to decide whether a Brep is a wall, door, beam or furniture item.

### 3. Dimension and text styles

The installer creates or validates the package's persistent metric annotation and text styles. The verified template baseline contains **14 persistent styles**: ten dimension/leader styles and four text-height styles.

Dimension and leader styles:

- **INV_STD_MM** — millimetres, integer display.
- **INV_STD_M** — metres, three decimal places, m suffix.
- **INV_STD_IN_DEC** — decimal inches, two decimal places.
- **INV_STD_IN_FRAC** — fractional inches.
- **INV_STD_FT_IN** — architectural feet-and-inches display.
- **INV_STD_MM_M** — millimetre primary units with metre alternate units.
- **INV_STD_MM_IN** — millimetre primary units with decimal-inch alternate units.
- **INV_STD_MM_FT_IN** — millimetre primary units with feet-and-inches alternate units.
- **INV_STD_M_MM** — metre primary units with millimetre alternate units.
- **INV_STD_LEADER_MM** — millimetre leader style.

Text styles:

- **INV_STD_TEXT_2_5MM** — 2.5 mm text height.
- **INV_STD_TEXT_3_5MM** — 3.5 mm text height.
- **INV_STD_TEXT_5_0MM** — 5.0 mm text height.
- **INV_STD_TEXT_7_0MM** — 7.0 mm text height.

The dimension styles use Arial, solid-triangle dimension arrowheads and open leader arrowheads; trailing zeroes are suppressed. Alternate-unit styles retain their configured alternate display and suffix. Existing valid user styles are preserved; reference styles are not treated as persistent standards. When asked to set the current style, the installer selects the style matching the model's unit system.

### 4. Rhino hatch definitions

The installer obtains the installed Rhino version's native hatch definitions through RhinoCommon. The verified Rhino 9 baseline contains **59 hatch definitions**. It checks for the standard names Concrete, Concrete Reinforced, Earth, Granite, Herringbone and Sand.

A local PAT file is optional. If one exists beside the installed runtime scripts, the installer attempts to import it. If no PAT file exists, it uses Rhino's native hatch definitions. This public repository does not redistribute McNeel's PAT payload.

### 5. Local metric template

When the template is missing, the installer creates it locally using a disposable headless Rhino document. The verified baseline is:

- Model and page units: millimetres
- 44 layers
- 14 persistent annotation/text styles
- 59 native hatch definitions
- Zero geometry objects
- Current layer: 04_ARCHITECTURE::GENERAL
- Current dimension style: INV_STD_MM

The installer reads the saved 3DM back and validates that the definitions persisted. A valid existing template is reused, not rebuilt at every Rhino launch. If an existing template fails validation, the installer refuses to overwrite it automatically.

**Important:** Opening or applying standards to an existing user model does not change its model units, page units, tolerances or ordinary geometry layer assignments. Millimetre units and template tolerances are set only while building the dedicated template.

---

## Script reference

### A. Current startup entrypoint — AutoLayer

**Path:** RhinoStandards/AutoLayer/Inventaur_RhinoAutoLayer.py
**Version:** 1.3.3

**Purpose**

Acts as the single Rhino startup entrypoint for this package. It loads and executes the installer from the user's runtime folder, then separately requests the RhinoAI MCP startup command.

**What it does**

1. Resolves the runtime installer at Documents/Inventaur/Rhino Standards/Inventaur_RhinoStandards_Install.py.
2. Loads and executes the installer so layers, styles, hatches, template validation and event handlers are applied.
3. Writes bootstrap success or error details to the startup log.
4. Invokes Rhino's _MCPStart command as a separate step. This is intended for installations where the RhinoAI MCP command is present and loaded; an unavailable command is logged rather than being confused with installer success.

**Run it**

Run this file with Rhino's RunPythonScript command during initial setup, then add the same command to **Rhino Options → General → Startup commands** for automatic execution on future launches.

**Runtime dependency**

The installer file must be present at the expected runtime path. AutoLayer does not embed a second copy of the installer.

**Log**

%LOCALAPPDATA%\Inventaur\RhinoStandards\logs\Inventaur_RhinoBootstrap.log

Component notes: [AutoLayer README](RhinoStandards/AutoLayer/README.md).

### B. Core standards engine — Installer

**Path:** RhinoStandards/Installer/Inventaur_RhinoStandards_Install.py
**Version:** 1.3.3

**Purpose**

Applies the actual Rhino standards. This is the package's main implementation, not just a file-copy installer.

**What it does**

- Creates or reuses the architectural layer tree and its drafting utility layers.
- Creates or validates the persistent metric dimension and text styles.
- Adds Rhino's installed native hatch definitions and optionally imports a local PAT file.
- Validates the required hatch names and minimum hatch baseline.
- Registers handlers for AddRhinoObject, NewDocument and EndOpenDocument.
- Routes existing and newly added text, annotation and hatch objects to their designated layers.
- Preserves ordinary geometry's existing layer assignment.
- Generates the metric 3DM template only when it is missing.
- Reads the generated or existing template back to confirm that required layers, styles, hatches and units are present.
- Logs applied counts, routing activity and failures.

**How routing works**

The event handler examines Rhino object types. Text entities/text dots go to TEXT; Rhino annotation objects such as dimensions and leaders go to ANNOTATIONS; hatch objects go to HATCH. Other geometry is deliberately left alone. Re-entry guards prevent the handler from repeatedly processing its own layer modifications.

**Run it**

The preferred route is to run Inventaur_RhinoAutoLayer.py, which loads this installer. The installer can also be run directly inside Rhino with RunPythonScript for a deliberate setup or repair operation.

**Safety boundaries**

- Existing user-document units and tolerances are preserved.
- The dedicated template is built in a separate headless document.
- A valid existing template is reused.
- An unreadable or invalid existing template is not silently overwritten.
- Ordinary geometry and its layer assignment are not reclassified.
- The installer does not create geometry in the template.

**Runtime outputs**

- Template: %USERPROFILE%\Documents\Inventaur\Rhino Standards\Inventaur_Architecture_MM.3dm
- Optional PAT input: %USERPROFILE%\Documents\Inventaur\Rhino Standards\McNeel_Rhino_Hatch_Library.pat
- Log: %LOCALAPPDATA%\Inventaur\RhinoStandards\logs\Inventaur_RhinoStandards.log

Component notes: [Installer README](RhinoStandards/Installer/README.md).

### C. Native hatch exporter — HatchLibrary

**Path:** RhinoStandards/HatchLibrary/Inventaur_ExportRhinoDefaultHatches.py

**Purpose**

Creates a local PAT export from the hatch definitions exposed by the Rhino installation on which the script is run. It is an export utility; it does not install or modify the current document's drafting standards.

**What it does**

1. Calls Rhino.DocObjects.HatchPattern.GetDefaultHatchPatterns().
2. Writes the returned definitions using HatchPattern.WriteToFile().
3. Reads the PAT headers back and checks that the count matches Rhino's returned pattern count.
4. Checks that pattern names are unique.
5. Calculates a SHA-256 hash of the resulting PAT file.
6. Writes a JSON report containing the Rhino version, pattern count, names, file path and hash.

**Run it**

Open Rhino 9 and run Inventaur_ExportRhinoDefaultHatches.py with RunPythonScript. It writes the files below; it does not require you to select geometry.

**Generated files**

- %USERPROFILE%\Documents\Inventaur\Rhino Standards\McNeel_Rhino_Hatch_Library.pat
- %USERPROFILE%\Documents\Inventaur\Rhino Standards\HatchLibrary_Export_Report.json

The generated PAT is local to the user's machine and is excluded from this repository. Exporting definitions from Rhino does not grant rights to redistribute third-party pattern content; review McNeel's terms before sharing generated files.

Component notes: [HatchLibrary README](RhinoStandards/HatchLibrary/README.md).

### D. Historical router — Legacy v1.0

**Path:** RhinoStandards/Legacy/Inventaur_RhinoAutoLayer_legacy_1_0.py
**Version:** 1.0.0

**Purpose**

Preserved as historical reference for the earlier AutoLayer implementation.

**What it does**

- Ensures top-level TEXT and ANNOTATIONS layers exist.
- Routes text entities and text dots to TEXT.
- Routes Rhino annotation objects, including dimensions and leaders, to ANNOTATIONS.
- Processes existing open documents and listens for new objects and document open/create events.
- Changes only the object's layer assignment when routing it.

**What it does not do**

- It does not install the current 44-layer architectural standards.
- It does not create or validate the metric template.
- It does not install or route hatch objects to HATCH.
- It does not include the current bootstrap's MCP startup call.

**Use**

Reference only. Do not configure this file as a startup command when using version 1.3.3. Running both routers can create overlapping event handlers and confusing behaviour.

Component notes: [Legacy README](RhinoStandards/Legacy/README.md).

---

## Installation

### Requirements

- Windows
- Rhino 9
- Rhino's locally installed RhinoCommon APIs and Python scripting environment
- rhinoscriptsyntax for optional PAT import when a local PAT file is present
- RhinoAI / its _MCPStart command only if automatic MCP startup is required

A valid Rhino licence is required. This repository does not include the Rhino application, RhinoCommon binaries or Rhino SDK.

### Initial setup

1. Make sure Rhino 9 is installed and opens normally.
2. Create the runtime folder:
   %USERPROFILE%\Documents\Inventaur\Rhino Standards
3. Copy these two scripts into that folder:
   - Inventaur_RhinoAutoLayer.py from RhinoStandards/AutoLayer/
   - Inventaur_RhinoStandards_Install.py from RhinoStandards/Installer/
4. In Rhino, run the startup entrypoint once using the RunPythonScript command.
5. Check the command output and logs for standards/template results.
6. In **Rhino Options → General → Startup commands**, add this startup command:

~~~text
_-RunPythonScript "%USERPROFILE%\Documents\Inventaur\Rhino Standards\Inventaur_RhinoAutoLayer.py"
~~~

7. To export a local PAT file, separately run the HatchLibrary exporter from inside Rhino.

The source repository keeps each component in its own folder with its own README. The deployed runtime scripts are copied side-by-side because the startup entrypoint expects the installer at that fixed runtime path.

### Existing template fails validation

The installer deliberately refuses to silently replace an unreadable or invalid template. Back up the existing 3DM outside the runtime folder, then move or rename it so the expected Inventaur_Architecture_MM.3dm path is clear. Run the installer again to generate a fresh template, then verify the resulting log and template. Keep the backup until the replacement has been checked.

---

## Runtime files and logs

| File | Purpose |
|---|---|
| Inventaur_Architecture_MM.3dm | Locally generated metric architectural template |
| Inventaur_Architecture_MM.3dm.previous | Previous template retained as a rollback copy when the installer replaces an existing template during a rebuild |
| McNeel_Rhino_Hatch_Library.pat | Optional local PAT file generated by the hatch exporter |
| HatchLibrary_Export_Report.json | Export validation report with names, count, Rhino version and SHA-256 |
| Inventaur_RhinoStandards.log | Installer actions, counts and routing/validation errors |
| Inventaur_RhinoBootstrap.log | Startup installer and MCP-start results |

Logs are written under %LOCALAPPDATA%\Inventaur\RhinoStandards\logs. Generated template, PAT and report files are local runtime outputs and are not committed to this repository.

## Verification status

The locally maintained 1.3.2 package was previously headless-tested against Rhino 9 with 44 layers, 14 styles, 59 hatch definitions and zero geometry objects. The 1.3.3 public package changes the PAT input to optional native-default fallback, generates the template locally and includes the hatch exporter. Static syntax, package-file and manifest checks passed for the public release. A fresh cold-start/UI acceptance test of public 1.3.3 remains an operator check on the recipient's Rhino workstation. See [VERIFICATION.md](VERIFICATION.md).

## Repository structure

~~~text
RhinoStandards/
├── AutoLayer/
│   ├── Inventaur_RhinoAutoLayer.py
│   └── README.md
├── HatchLibrary/
│   ├── Inventaur_ExportRhinoDefaultHatches.py
│   └── README.md
├── Installer/
│   ├── Inventaur_RhinoStandards_Install.py
│   └── README.md
├── Legacy/
│   ├── Inventaur_RhinoAutoLayer_legacy_1_0.py
│   └── README.md
├── Template/
│   └── README.md
└── README.md
~~~

See [RhinoStandards/README.md](RhinoStandards/README.md) for the package-level summary. Each component folder has its own README with component-specific notes.

## Third-party materials

The repository does not bundle McNeel's native hatch PAT payload, Rhino application files, RhinoCommon binaries or a prebuilt 3DM template. The scripts call APIs from the user's local Rhino installation. McNeel's hatch information is available at [Rhino hatch documentation](https://wiki.mcneel.com/rhino/hatch). See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and McNeel's terms for third-party material.

## Licensing and commercial enquiries

Inventaur-authored scripts and documentation are proprietary. This repository is not an OSI-approved open-source release, and viewing the source does not grant permission to use or deploy it. Commercial deployment, business use, production use, integration, modification, redistribution or derivative development requires a separate written commercial licence signed by Inventaur Inc.

Read [LICENSE.md](LICENSE.md).
Commercial enquiries: [inventaur.in](https://inventaur.in).
