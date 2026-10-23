"""Verify an exact original disc and create a separate translated copy."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def require(condition, message):
    if not condition:
        raise ValueError(message)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path, nargs='?')
    parser.add_argument('--check', action='store_true', help='Verify original disc and patches only')
    args = parser.parse_args()
    src = args.source.resolve()
    meta = json.loads((HERE / 'source-hashes.json').read_text())
    require(src.is_dir(), 'Source folder does not exist')
    for f in meta['files']:
        p = src / f['name']
        require(p.is_file() and p.stat().st_size == f['size'] and sha(p) == f['input_sha256'], 'Original file mismatch: ' + f['name'])
        if 'patch' in f:
            require(sha(HERE / f['patch']) == f['patch_sha256'], 'Patch hash mismatch: ' + f['patch'])
    print('PASS: all 99 original tracks, original CUE and both patches match.')
    if args.check:
        return
    require(args.output is not None, 'Specify a new output folder, or use --check')
    out = args.output.resolve()
    require(not out.exists(), 'Output folder already exists; choose a new folder')
    require(out != src and src not in out.parents, 'Output must be outside the source folder')
    require(shutil.which('xdelta3') is not None, 'Install xdelta3 and put it on PATH')
    out.mkdir(parents=True)
    for f in meta['files']:
        p, q = src / f['name'], out / f['name']
        if 'patch' in f:
            subprocess.run(['xdelta3', '-d', '-s', str(p), str(HERE / f['patch']), str(q)], check=True)
        else:
            shutil.copy2(p, q)
        require(q.stat().st_size == f['size'] and sha(q) == f['output_sha256'], 'Output verification failed: ' + f['name'])
    for f in meta['files']:
        require(sha(src / f['name']) == f['input_sha256'], 'Source verification failed: ' + f['name'])
    print('PASS: translated copy verified; originals unchanged. Launch the CUE in:', out)

if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        sys.exit('ERROR: ' + str(error))
