# SuperGrafx compatibility update

Released in **2026.10.30.1**. This update mainly addresses **SuperGrafx Mode I** while retaining standard PC Engine support and the CRT subtitle improvements from 2026.10.27.1.

## What was corrected

A graphics-upload operation in the cinematic subtitle renderer could also affect the SuperGrafx's additional video controls. That could cause corruption, a black screen or a freeze with the extra hardware enabled. Different starting states and timing could leave one setup apparently unaffected while another showed the problem.

The correction keeps that operation confined to its intended video destination. Subtitle placement, line breaks, font, black backing and the existing CRT safeguards are retained. The English text, Japanese voices, music and artwork are unchanged from the preceding release.

## Emulator verification

Verification used **Beetle PCE / Mednafen PCE (libretro)** with two explicitly selected configurations:

- Standard PC Engine with System Card 3 / Super CD-ROM² memory.
- SuperGrafx hardware enabled, also with System Card 3 / Super CD-ROM² memory.

All **38 cinematic/event checks passed in each configuration**. Checks covered caption rendering and cleanup, including one-line and two-line captions, with the existing protection against visible-picture palette interference retained.

## Physical hardware verification

The corrected build was tested using a **Turbo EverDrive Pro** on:

- **SuperGrafx in both Mode I and Mode II**.
- **PC Engine GT**.

External-display checks included a **CRT** and a **flat-panel display through a RetroTINK-4K Pro**. Cinematics displayed correctly in these checks. A one-off report of crunchy opening audio did not recur on retest; this compatibility update does not replace or reprocess the original audio.

These are the verified configurations, rather than a guarantee for every console, firmware, drive replacement or display chain.

## Updating and saves

Apply the two included patches to the exact **unmodified Japanese disc** listed in [source-hashes.json](source-hashes.json). This is a complete direct-from-original package; neither of the previous English releases is required.

Keep the CUE filename associated with your existing saves and cheats when moving the new build to an emulator or flash cartridge. The native save format is unchanged. The patcher creates a separate output folder and does not modify save or cheat files.

See [patching instructions](README.md#requirements-and-patching) and the earlier [renderer and CRT notes](SUBTITLE-RENDERER.md).
