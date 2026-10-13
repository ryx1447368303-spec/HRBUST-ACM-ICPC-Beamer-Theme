"""Package the adapted XeLaTeX theme using only Python's standard library."""
from argparse import ArgumentParser
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--full", action="store_true", help="Include the full guide and bibliography")
    parser.add_argument("--with-fonts", action="store_true", help="Include the original WenKai/Sarasa fonts")
    parser.add_argument("--include-pdfs", action="store_true", help="Include compiled PDFs in a full package")
    parser.add_argument("--no-bib", action="store_true", help="Use the starter without bibliography (default)")
    parser.add_argument("-o", "--output", default="dist/HRBUST-ACM-ICPC-Theme-overleaf.zip")
    args = parser.parse_args()
    if args.full and args.no_bib:
        parser.error("--full includes the bibliography. Omit --full for the starter without biber.")
    if args.include_pdfs and not args.full:
        parser.error("--include-pdfs requires --full so the PDF and source document names match.")

    root = Path(__file__).resolve().parent
    output = Path(args.output)
    if not output.is_absolute():
        output = root / output
    output.parent.mkdir(parents=True, exist_ok=True)

    files = {p.name: p for p in root.glob("*.sty")}
    for name in ("fonts-setup.tex", "LICENSE", "README.md", "README_EN.md", "template.tex",
                 "build.ps1", "pack-overleaf.ps1", "pack_overleaf.py", "pack_overleaf.sh"):
        files[name] = root / name
    for path in (root / "img" / "README").glob("*.png"):
        files[path.relative_to(root).as_posix()] = path
    for name in ("CHANGELOG.md", "CONTRIBUTING.md"):
        if (root / name).is_file():
            files[name] = root / name
    if args.include_pdfs:
        for name in ("slide.pdf", "template.pdf"):
            files[name] = root / name
    for path in (root / "img" / "branding").glob("*"):
        files[path.relative_to(root).as_posix()] = path
    if args.full:
        files["slide.tex"] = root / "slide.tex"
        files["ref.bib"] = root / "ref.bib"
        illustration = root / "img" / "Example" / "SimpleDistributedStorageArchitecture.png"
        files[illustration.relative_to(root).as_posix()] = illustration
    else:
        files["slide.tex"] = root / "template.tex"
    if args.with_fonts:
        for name in ("LXGWWenKai-Regular.ttf", "LXGWWenKai-Medium.ttf", "SarasaMonoSC-Regular.ttf", "OFL.txt"):
            files[f"fonts/{name}"] = root / "fonts" / name
    for path in files.values():
        if not path.is_file():
            raise FileNotFoundError(path)

    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for target, source in sorted(files.items()):
            archive.write(source, target)
        archive.writestr(".latexmkrc", "$pdf_mode = 5;\n@default_files = ('slide.tex');\n")
        archive.writestr("PACKAGE-README.txt", (
            "HRBUST ACM-ICPC Beamer Theme\n"
            "Compiler: XeLaTeX. Main document: slide.tex.\n"
            + ("This package contains the full guide and template.tex starter.\n" if args.full else
               "This is the starter package: slide.tex is a copy of template.tex, without biber.\n")
            + ("Original WenKai/Sarasa fonts are included.\n" if args.with_fonts else
               "This compact package uses Fandol fonts. Use --with-fonts to preserve original typography.\n")
        ))
    print(f"Created {output} ({output.stat().st_size:,} bytes)")
    print("Overleaf: Main document = slide.tex; Compiler = XeLaTeX.")


if __name__ == "__main__":
    main()
