# Fonts in this directory

[中文版说明](./README_cn.md)

All fonts in this directory come from third-party projects; this repository
holds no copyright over them.

| Font | Source | License |
| --- | --- | --- |
| LXGW WenKai | <https://github.com/lxgw/LxgwWenKai> | SIL OFL 1.1, see `OFL.txt` |
| Sarasa Mono SC | <https://github.com/be5invis/Sarasa-Gothic> | SIL OFL 1.1, see `OFL.txt` |

`OFL.txt` contains the full text of the SIL Open Font License 1.1, which
applies to both font projects above.

In addition, the English fonts used in `slide.tex` — Times New Roman and
Arial — are Microsoft commercial fonts and are **not** included in this
repository. `fonts-setup.tex` uses them when they are installed on your system,
and otherwise loads TeX Gyre Termes / Heros from TeX Live. GitHub Actions uses
this fallback; the workflow does not install Microsoft fonts.

WenKai and Sarasa are loaded directly from the files in this directory, so no
system installation is required. Compact Overleaf packages omit this directory
and use TeX Live's Fandol fonts instead.
