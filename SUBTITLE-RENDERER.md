# Subtitle renderer and CRT update

Introduced in **2026.10.27.1** and retained in **2026.10.30.1**. The later [SuperGrafx compatibility correction](SGX-COMPATIBILITY.md) keeps this subtitle presentation and its CRT safeguards.

## Why the renderer needed another pass

Cosmic Fantasy builds its cinematics using the console's own scene system. Adding subtitles means sharing that presentation with moving artwork, changing scene sizes and native audio playback. A clean-looking recording alone was not enough: earlier hardware reports described flickering and stray pixels around the captions, especially on CRT displays.

The revision focuses on keeping captions readable and stable while letting the original scenes continue normally. This page describes the visible changes and validation; implementation details are intentionally outside its scope.

## What changed

- Subtitles keep a consistent position and retain their line breaks throughout each page.
- White text has a solid, full-width black backing for contrast over light or busy artwork. Single-line and two-line captions use appropriately sized heights.
- Letter tails and the spacing between two lines remain fully visible.
- Caption changes, scene transitions and skipping received additional cleanup to prevent stray fragments and flickering.
- The brief opening-logo jump was corrected separately.
- Original Japanese voices, music, artwork and staff credits are retained. The bilingual Planet Norg card is also retained.

## Timing and scene transitions

Timing was compared with the original game's playback. The measured voiced sections differed by no more than two frames at their native start/pause boundaries. Subtitle timing follows native playback; the audio was not stretched or replaced.

Some transitions have a slightly longer pause between scenes. The reported hardware review found these pauses unobtrusive, with no scene repetition or looping.

## Review and hardware results

Local review covered **41 recordings**, including the bonus advertisement, and **280 non-empty subtitle pages**, plus the independent location card.

The release's cutscenes were also reviewed through the in-game debug menu on this setup:

| Component | Reported setup |
| --- | --- |
| Console | SuperGrafx |
| Disc replacement | Turbo EverDrive Pro |
| Video output | EDFX; RGB and composite paths |
| CRT display | Toshiba 20AF43 |

No major rendering problems or unusual flickering were observed in that hardware review. This records the result for the setup above, rather than claiming identical behaviour on every display or console configuration.

## Updating

Apply this release to the exact unmodified Japanese disc listed in [source-hashes.json](source-hashes.json), following the [patching instructions](README.md#requirements-and-patching). Both data-track patches are included; an older English release is not required. Existing saves and cheats can be retained by keeping the associated CUE filename and save files.
