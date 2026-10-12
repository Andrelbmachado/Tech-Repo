---
name: powershell
description: "Automatizar com PowerShell 7 em Windows, Linux e macOS. Use quando: Administração de sistemas Windows/Azure, automação multiplataforma e scripts de TI."
---

# Skill: PowerShell

Automatizar com PowerShell 7 em Windows, Linux e macOS.

## Quando usar

Administração de sistemas Windows/Azure, automação multiplataforma e scripts de TI.

## Conceitos principais

- Cmdlets no formato Verbo-Substantivo
- Pipeline de objetos (não texto)
- Módulos e Gallery
- Tratamento de erros (`try/catch`, `-ErrorAction`)
- Parâmetros avançados (`[CmdletBinding()]`)

## Boas práticas

- Use verbos aprovados (`Get-Verb`)
- Use `Set-StrictMode -Version Latest`
- Prefira objetos e `Select-Object`/`Where-Object` a parsing de texto
- Suporte `-WhatIf`/`-Confirm` em comandos que alteram estado
- Analise com PSScriptAnalyzer

## Comandos e padrões comuns

```powershell
Get-Help Get-Process -Full
Get-Command -Module Microsoft.PowerShell.Management
Get-Process | Where-Object CPU -gt 100 | Select-Object Name, CPU
Invoke-ScriptAnalyzer -Path .\script.ps1
$PSVersionTable
```

## Armadilhas comuns

- Diferenças entre Windows PowerShell 5.1 e PowerShell 7
- Erros não terminais não acionam `catch`
- Política de execução bloqueando scripts

## Checklist

- [ ] Use verbos aprovados (`Get-Verb`)
- [ ] Use `Set-StrictMode -Version Latest`
- [ ] Prefira objetos e `Select-Object`/`Where-Object` a parsing de texto
- [ ] Suporte `-WhatIf`/`-Confirm` em comandos que alteram estado
- [ ] Analise com PSScriptAnalyzer
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/powershell/`](../../../docs/programacao/linguagens/powershell/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/powershell/documentacao-oficial/`](../../../docs/programacao/linguagens/powershell/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/powershell/fontes.yml)

## Fontes oficiais

- [PowerShell documentation](https://learn.microsoft.com/en-us/powershell/) — Microsoft
- [PowerShell language specification](https://learn.microsoft.com/en-us/powershell/scripting/lang-spec/chapter-01) — Microsoft
- [PowerShell scripting documentation](https://learn.microsoft.com/en-us/powershell/scripting/overview) — Microsoft
- [PowerShell module reference](https://learn.microsoft.com/en-us/powershell/module/) — Microsoft
- [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/windows-powershell) — Microsoft
