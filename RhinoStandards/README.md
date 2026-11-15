# Rhino 9 Standards Package

The metric template, installer, AutoLayer entrypoint and hatch exporter are one shared standards package.

- AutoLayer: startup entrypoint and automatic TEXT / ANNOTATIONS / HATCH routing.
- Installer: installs drafting layers/styles, Rhino native hatch defaults, and generates/validates the local metric template.
- Template: notes for the template generated locally by the installer.
- HatchLibrary: exports native Rhino hatch definitions to a local PAT file.
- Legacy: reference-only legacy router.

Each component has its own README. The public source package does not include generated 3DM or PAT files. Those are generated or stored locally by the user's own Rhino installation.
