#!/usr/bin/env pwsh
# Installs the preconstruction-ru and preconstruction-en skills on Windows:
#   %USERPROFILE%\.claude\skills  - Claude Code (terminal, VS Code, JetBrains, Claude app)
#   %USERPROFILE%\.agents\skills  - Codex and other agents that read the Agent Skills layout
#
#   powershell -ExecutionPolicy Bypass -File .\install.ps1             # junctions
#   powershell -ExecutionPolicy Bypass -File .\install.ps1 -Copy       # copies
#   powershell -ExecutionPolicy Bypass -File .\install.ps1 -Uninstall  # remove junctions
#
# -ExecutionPolicy Bypass: by default Windows refuses to run downloaded scripts.
# Junctions, not symlinks: they need neither admin rights nor Developer Mode, and the
# agents follow them; `git pull` then updates the skills. Re-runnable: a name that is
# already taken is skipped, never overwritten.
# ASCII only on purpose: Windows PowerShell 5.1 reads a BOM-less script in the ANSI
# code page, and any Cyrillic text here would be garbled.
param([switch]$Copy, [switch]$Uninstall)

$ErrorActionPreference = 'Stop'
$repoSkills = Join-Path $PSScriptRoot 'skills'
if (-not (Test-Path $repoSkills)) { throw "No skills folder next to this script." }
$repoSkills = (Resolve-Path $repoSkills).Path

$targets = @(
  (Join-Path $env:USERPROFILE '.claude\skills'),
  (Join-Path $env:USERPROFILE '.agents\skills')
)

foreach ($t in $targets) {
  Write-Host "`nTarget: $t" -ForegroundColor Cyan
  if (-not $Uninstall) { New-Item -ItemType Directory -Force -Path $t | Out-Null }

  Get-ChildItem $repoSkills -Directory |
    Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') } |
    ForEach-Object {
      $dest = Join-Path $t $_.Name
      if ($Uninstall) {
        if (Test-Path $dest) {
          $item = Get-Item $dest -Force
          $linkTarget = $item.Target | Select-Object -First 1
          if ($item.LinkType -eq 'Junction' -and $linkTarget -eq $_.FullName) {
            # rmdir removes the junction itself and never touches the files it points to
            cmd /c rmdir "$dest" | Out-Null
            Write-Host "  removed junction: $($_.Name)" -ForegroundColor Green
          } else {
            Write-Host "  left as is (not a junction to this folder): $dest" -ForegroundColor Yellow
          }
        }
      } elseif (Test-Path $dest) {
        Write-Host "  skipped (already exists): $($_.Name)" -ForegroundColor Yellow
      } elseif ($Copy) {
        Copy-Item -Recurse -Path $_.FullName -Destination $dest
        Write-Host "  copied: $($_.Name)" -ForegroundColor Green
      } else {
        New-Item -ItemType Junction -Path $dest -Target $_.FullName | Out-Null
        Write-Host "  linked: $($_.Name)" -ForegroundColor Green
      }
    }
}

if ($Uninstall) {
  Write-Host "`nDone. Copies made with -Copy are not removed: delete those folders by hand." -ForegroundColor Cyan
} else {
  Write-Host "`nDone. Restart Claude Code (or run /reload-skills), then type /preconstruction-ru or /preconstruction-en." -ForegroundColor Cyan
  if ($Copy) {
    Write-Host "Copies do not update: re-run with -Copy after a new download." -ForegroundColor Cyan
  } else {
    Write-Host "Keep this folder where it is: the junctions point to it. Update later with: git pull" -ForegroundColor Cyan
  }
}
