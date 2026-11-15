# Rhino AutoLayer Startup Entrypoint

Script: Inventaur_RhinoAutoLayer.py
Package version: 1.3.4

This startup entrypoint has two version-specific paths:

- **Rhino 9:** loads the Inventaur Rhino Standards installer, then starts the McNeel RhinoAI MCP server on 127.0.0.1:10500.
- **Rhino 8:** skips the Rhino 9-targeted drafting-standards installer and starts the RhinoAI MCP server on 127.0.0.1:10508.

The explicit port argument is important. A bare _MCPStart opens the interactive MCPStart Port <10500>: prompt and leaves Rhino waiting for input. The startup script instead runs _MCPStart 10500 in Rhino 9 or _MCPStart 10508 in Rhino 8, with a final space that submits the port as Enter in Rhino command scripting. It checks whether the selected local port already has a listener, avoiding an unnecessary server restart.

## Rhino 9 standards path

The Rhino 9 path loads Inventaur_RhinoStandards_Install.py, applies layers/styles/hatches, validates the local metric template, and registers annotation/hatch routing.

## Rhino 8 MCP-only path

The current drafting-standards installer is qualified for Rhino 9. Rhino 8 therefore uses this entrypoint for MCP autostart only; the installer is deliberately skipped there so an unverified Rhino 8 standards run cannot interfere with MCP startup.

## Install

Copy this entrypoint to:

%USERPROFILE%\Documents\Inventaur\Rhino Standards\Inventaur_RhinoAutoLayer.py

Configure the version-specific Rhino profile to run:

~~~text
_-RunPythonScript "%USERPROFILE%\Documents\Inventaur\Rhino Standards\Inventaur_RhinoAutoLayer.py"
~~~

The Rhino 9 Default profile already has this command. The Rhino 8 Default profile is configured by the matching setup update.

## Ports

| Rhino version | MCP port |
|---|---:|
| Rhino 8 | 10508 |
| Rhino 9 | 10500 |

Separate ports allow both Rhino versions to run at the same time without competing for the same TCP listener.

**Rhino 8 verification (2026-11-15):** a fresh Default-profile Rhino 8 process ran this entrypoint automatically. The script logged MCPSTART_RUNSCRIPT_RETURN=True for _MCPStart 10508, confirmed the TCP listener, and returned HTTP 200 to an MCP initialize request (server rhino-mcp 0.4.0.0). The empty test process was closed afterwards. Connect an external MCP client to the port for the Rhino instance being used.

## Logs

%LOCALAPPDATA%\Inventaur\RhinoStandards\logs\Inventaur_RhinoBootstrap.log

Relevant entries:

- STANDARDS_BOOTSTRAP_OK — Rhino 9 standards installer completed.
- STANDARDS_BOOTSTRAP_SKIPPED — Rhino 8 MCP-only path.
- MCPSTART_RUNSCRIPT_RETURN — explicit MCPStart command result.
- MCP_ENDPOINT_TCP_REACHABLE — local TCP listener verified.
- MCP_ALREADY_REACHABLE — listener already existed; no restart was sent.
- MCP_ENDPOINT_TCP_NOT_REACHABLE — command returned but no listener was found.
