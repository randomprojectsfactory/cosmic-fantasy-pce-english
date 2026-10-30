# Changelog

## 2026.10.30.1 — 2026-10-30

- Corrected a cinematic subtitle graphics-upload issue affecting SuperGrafx, principally Mode I.
- Retained standard PC Engine support and the approved CRT subtitle presentation.
- Passed 38 cinematic/event checks in both PCE + Super CD-ROM² and SGX + Super CD-ROM² emulation using Beetle PCE / Mednafen.
- Tested with Turbo EverDrive Pro on SuperGrafx in Mode I and Mode II, and on PC Engine GT. External-display checks covered a CRT and RetroTINK-4K Pro with a flat panel.
- Updated direct-from-original patches and exact input/output hashes; native saves and cheat associations remain compatible when filenames are retained.
- Added [SuperGrafx compatibility notes](SGX-COMPATIBILITY.md).

## 2026.10.27.1 — 2026-10-27

- Revised cinematic subtitle renderer for stable presentation and clearer contrast on CRT displays.
- Consistent caption position and wrapping; full-width black backing sized for one or two lines.
- Complete letter tails, clearer line separation, and improved caption/scene cleanup.
- Dedicated correction for the brief opening-logo jump.
- Retained Japanese voices, music, artwork, credits and the bilingual Planet Norg card.
- 41 local scene recordings and all 280 non-empty subtitle pages reviewed; original playback timing compared.
- Positive cutscene review on SuperGrafx, Turbo EverDrive Pro, EDFX RGB/composite paths and Toshiba 20AF43 CRT.
- Updated direct-from-original patches and input/output hash manifest.
- Added [renderer and CRT notes](SUBTITLE-RENDERER.md).

## 2026.10.23.1 — 2026-10-23

- Initial packaged English PCE adaptation based on the Collection localisation for Switch.
- English story and interface text, shops, items/descriptions and combat messages.
- 364 cinematic caption entries across 59 audio tracks; Japanese voices and music retained.
- Planet Norg bilingual title card preserving Japanese lettering and artwork.
- Corrected combat actor/target copy and Yu/Saya battle-command headings.
- Native text wrapping/pagination and menu, shop, battle and in-game Load display corrections.
- Two direct-from-original xdelta patches with exact input/output hashes.
