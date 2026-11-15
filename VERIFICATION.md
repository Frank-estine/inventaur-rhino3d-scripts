# Verification Summary

The source scripts derive from the locally maintained Rhino Standards 1.3.2 package.

Verified locally against Rhino 9:
- Installer headless regression: 44 layers, 14 annotation/text styles, 59 native hatch definitions and zero geometry objects.
- Existing metric template readback: 44 layers, 14 styles, 59 hatch definitions.
- The PAT exporter implementation previously generated and read back 59 unique native hatch definitions.
- Source scripts compile under the Rhino Python environment.

Public package 1.3.4 changes:
- PAT input is optional; native Rhino defaults are used when no local PAT file is present.
- The installer creates the metric template locally instead of downloading a prebuilt 3DM.
- A local PAT exporter is included.
- No locally generated PAT, 3DM, personal workstation logs or machine-specific verification reports are committed.

Rhino 8 fresh Default-profile startup and MCP initialization passed. Rhino 9's currently running MCP endpoint passed initialize and tools/list; a fresh Rhino 9 process restart after the latest bootstrap patch remains pending.

## Rhino 8 / Rhino 9 MCP autostart

The AutoLayer startup script now passes the port argument and a final command-script separator so Rhino receives the port value and Enter without an interactive pause.

- **Rhino 8:** fresh Default-profile process started the shared entrypoint automatically. The log recorded MCPSTART_RUNSCRIPT_RETURN=True for _MCPStart 10508, then MCP_ENDPOINT_TCP_REACHABLE. An MCP initialize request returned HTTP 200; server identified itself as rhino-mcp version 0.4.0.0. The temporary empty test process was closed after the test.
- **Rhino 9:** the live endpoint at 127.0.0.1:10500 returned HTTP 200 to MCP initialize and tools/list (44 tools). This was an already-running Rhino 9 session, not a fresh cold start after the latest bootstrap patch.
- **Ports:** Rhino 8 uses 10508; Rhino 9 uses 10500. The entrypoint skips the Rhino 9 standards installer in Rhino 8 and uses an MCP-only path there.

**Remaining acceptance:** verify the updated bootstrap on the next normal Rhino 9 cold start. The active Rhino 9 project process was not restarted or closed for this test.
