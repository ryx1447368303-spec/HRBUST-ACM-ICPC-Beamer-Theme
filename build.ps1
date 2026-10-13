#Requires -Version 7.0
param(
    [ValidateSet('slide', 'template')]
    [string[]]$Document = @('slide', 'template'),
    [string]$TexBin
)
$ErrorActionPreference = 'Stop'
if ($TexBin) {
    if (-not (Test-Path -LiteralPath $TexBin -PathType Container)) {
        throw "TeX binary directory does not exist: $TexBin"
    }
    $env:PATH = "$TexBin$([IO.Path]::PathSeparator)$env:PATH"
} elseif (-not (Get-Command latexmk -ErrorAction SilentlyContinue)) {
    # An optional portable toolchain can remain local to this workspace.
    $localBin = Join-Path $PSScriptRoot 'tmp/toolchain/TinyTeX/bin/windows'
    if (Test-Path -LiteralPath (Join-Path $localBin 'latexmk.exe')) {
        $env:PATH = "$localBin$([IO.Path]::PathSeparator)$env:PATH"
    }
}
if (-not (Get-Command latexmk -ErrorAction SilentlyContinue)) {
    throw 'Install TeX Live / MiKTeX with XeLaTeX, latexmk and biber, or pass -TexBin.'
}
Push-Location $PSScriptRoot
try {
    foreach ($name in $Document) {
        & latexmk "$name.tex"
        if ($LASTEXITCODE -ne 0) { throw "Build failed: $name.tex" }
    }
} finally {
    Pop-Location
}
