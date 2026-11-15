# Rhino startup entrypoint.
# Rhino 9: load Inventaur drafting standards, then start RhinoAI MCP on port 10500.
# Rhino 8: MCP autostart only, on port 10508. The standards installer is Rhino 9-targeted.
import Rhino, traceback, os, codecs, socket

_INV_INSTALLER_PATH = os.path.join(
    os.path.expanduser("~"), "Documents", "Inventaur", "Rhino Standards",
    "Inventaur_RhinoStandards_Install.py"
)
_INV_RHINO_MAJOR = 9
try:
    _INV_RHINO_MAJOR = int(Rhino.RhinoApp.Version.Major)
except Exception:
    try:
        _INV_RHINO_MAJOR = int(str(Rhino.RhinoApp.Version).split(".", 1)[0])
    except Exception:
        pass

_INV_MCP_PORT = 10508 if _INV_RHINO_MAJOR == 8 else 10500
_INV_BOOTSTRAP_LOG_PATH = os.path.join(
    os.environ.get("LOCALAPPDATA", os.path.expanduser("~")),
    "Inventaur", "RhinoStandards", "logs", "Inventaur_RhinoBootstrap.log"
)

def _inv_ensure_directory(path):
    """Create a directory on both IronPython 2.7 and CPython 3."""
    if os.path.isdir(path):
        return
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise

_inv_ensure_directory(os.path.dirname(_INV_BOOTSTRAP_LOG_PATH))

def _inv_bootstrap_log(message):
    try:
        with codecs.open(_INV_BOOTSTRAP_LOG_PATH, "a", "utf-8") as stream:
            stream.write(str(message) + "\n")
    except Exception:
        pass

def _inv_tcp_port_open(port):
    """Check whether the local MCP port already has a listener."""
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        return sock.connect_ex(("127.0.0.1", int(port))) == 0
    except Exception:
        return False
    finally:
        if sock is not None:
            try:
                sock.close()
            except Exception:
                pass

# Rhino Standards is currently qualified for Rhino 9. Keep Rhino 8's
# MCP bootstrap independent so an installer compatibility issue cannot block MCP.
if _INV_RHINO_MAJOR == 9:
    try:
        with codecs.open(_INV_INSTALLER_PATH, "r", "utf-8") as stream:
            _inv_installer_source = stream.read()
        eval(compile(_inv_installer_source, _INV_INSTALLER_PATH, "exec"), globals(), globals())
        _inv_bootstrap_log("STANDARDS_BOOTSTRAP_OK version={0}".format(str(globals().get("VERSION", "unknown"))))
    except Exception:
        _inv_bootstrap_log("STANDARDS_BOOTSTRAP_ERROR\n" + traceback.format_exc())
else:
    _inv_bootstrap_log(
        "STANDARDS_BOOTSTRAP_SKIPPED rhino_major={0}; MCP autostart continues".format(
            _INV_RHINO_MAJOR
        )
    )

# Use an explicit port argument. A bare _MCPStart leaves Rhino waiting at
# "MCPStart Port <10500>:" and stalls the startup command.
try:
    if _inv_tcp_port_open(_INV_MCP_PORT):
        _inv_bootstrap_log("MCP_ALREADY_REACHABLE port={0}".format(_INV_MCP_PORT))
    else:
        _inv_mcp_command = "_MCPStart {0} ".format(_INV_MCP_PORT)
        _inv_mcp_start_result = Rhino.RhinoApp.RunScript(_inv_mcp_command, False)
        _inv_bootstrap_log(
            "MCPSTART_RUNSCRIPT_RETURN={0} command={1}".format(
                repr(_inv_mcp_start_result), repr(_inv_mcp_command)
            )
        )
        if _inv_tcp_port_open(_INV_MCP_PORT):
            _inv_bootstrap_log("MCP_ENDPOINT_TCP_REACHABLE port={0}".format(_INV_MCP_PORT))
        else:
            _inv_bootstrap_log("MCP_ENDPOINT_TCP_NOT_REACHABLE port={0}".format(_INV_MCP_PORT))
except Exception:
    _inv_bootstrap_log("MCPSTART_ERROR\n" + traceback.format_exc())
