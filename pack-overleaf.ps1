#Requires -Version 7.0
param(
    [switch]$Full,
    [switch]$WithFonts,
    [switch]$IncludePdfs,
    [string]$Output = 'dist/HRBUST-ACM-ICPC-Theme-overleaf.zip'
)
$ErrorActionPreference = 'Stop'
$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCommand) { throw 'Python 3 is required to build the zip.' }
$packArgs = @((Join-Path $PSScriptRoot 'pack_overleaf.py'), '--output', $Output)
if ($Full) { $packArgs += '--full' }
if ($WithFonts) { $packArgs += '--with-fonts' }
if ($IncludePdfs) { $packArgs += '--include-pdfs' }
& $pythonCommand.Source @packArgs
if ($LASTEXITCODE -ne 0) { throw 'Packaging failed.' }
