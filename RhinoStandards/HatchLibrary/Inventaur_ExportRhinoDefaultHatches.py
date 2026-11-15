# -*- coding: utf-8 -*-
"""Export the current Rhino native hatch definitions to a local PAT file."""
import os
import json
import hashlib
import codecs
import Rhino

def ensure_directory(path):
    if os.path.isdir(path):
        return
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise

def read_names(path):
    names = []
    with codecs.open(path, "r", "utf-8-sig") as stream:
        for line in stream:
            if line.startswith("*"):
                names.append(line[1:].split(",", 1)[0].strip())
    return names

def main():
    base = os.path.join(os.path.expanduser("~"), "Documents", "Inventaur", "Rhino Standards")
    ensure_directory(base)
    pat_path = os.path.join(base, "McNeel_Rhino_Hatch_Library.pat")
    report_path = os.path.join(base, "HatchLibrary_Export_Report.json")
    patterns = Rhino.DocObjects.HatchPattern.GetDefaultHatchPatterns()
    if patterns is None:
        raise RuntimeError("Rhino returned no default hatch definitions")
    if not Rhino.DocObjects.HatchPattern.WriteToFile(pat_path, patterns):
        raise RuntimeError("RhinoCommon WriteToFile returned False")
    names = read_names(pat_path)
    folded = [name.lower() for name in names]
    if len(names) != len(patterns):
        raise RuntimeError("PAT header count does not match Rhino default pattern count")
    if len(set(folded)) != len(folded):
        raise RuntimeError("PAT contains duplicate pattern names")
    digest = hashlib.sha256()
    with open(pat_path, "rb") as stream:
        digest.update(stream.read())
    report = {
        "status": "PASS",
        "rhino_version": str(Rhino.RhinoApp.Version),
        "pattern_count": len(names),
        "pattern_names": names,
        "pat_sha256": digest.hexdigest(),
        "pat_path": pat_path
    }
    with codecs.open(report_path, "w", "utf-8") as stream:
        stream.write(json.dumps(report, indent=2))
    print("INVENTAUR_HATCH_EXPORT_OK count={0} sha256={1}".format(len(names), digest.hexdigest()))
    print("PAT: " + pat_path)
    print("REPORT: " + report_path)

if __name__ == "__main__":
    main()
