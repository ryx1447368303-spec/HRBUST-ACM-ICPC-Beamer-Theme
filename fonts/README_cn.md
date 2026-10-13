# 字体文件说明

[English version](./README.md)

本目录下的字体均来自第三方项目，本项目不持有其版权。

| 字体 | 来源 | 许可证 |
| --- | --- | --- |
| LXGW WenKai (落霞孤鹜文楷) | <https://github.com/lxgw/LxgwWenKai> | SIL OFL 1.1，见 `OFL.txt` |
| Sarasa Mono SC (更纱黑体) | <https://github.com/be5invis/Sarasa-Gothic> | SIL OFL 1.1，见 `OFL.txt` |

`OFL.txt` 为 SIL Open Font License 1.1 的完整文本，对上述两个字体项目均适用。

另外，`slide.tex` 中的英文字体 Times New Roman 与 Arial 为 Microsoft 商业字体，
**不包含**在本仓库中。`fonts-setup.tex` 在系统已安装时使用它们，缺失时
自动读取 TeX Live 的 TeX Gyre Termes / Heros。GitHub Actions 使用该回退方案，
工作流不安装 Microsoft 字体。

文楷与更纱字体由本目录文件直接加载，无须安装到系统。
Overleaf 精简包省略本目录，改用 TeX Live 自带的 Fandol 字体。
