# ROADMAP — qzuipo-toolkit

> Este arquivo documenta o planejamento interno de melhorias, decisões técnicas futuras e ideias em aberto.
> Para entender o que o projeto faz hoje, veja o [README.md](./README.md).

---

## Status atual

| Componente | Status |
|---|---|
| Caesar Cipher | ✅ Funcional (refatoração pendente) |
| Estrutura modular (`ciphers/`, `utils/`, `detector/`) | 🔄 Em andamento |
| Vigenère Cipher | ⬜ Planejado |
| Loop pós-operação | ⬜ Planejado |
| Interface CLI melhorada | ⬜ Planejado |
| Detector automático de cifras | ⬜ Pesquisa em andamento |

---

## Próximos passos imediatos

### 1. Finalizar refatoração do Caesar
- Extrair `encrypt()` e `decrypt()` para `ciphers/caesar.py` sem nenhuma lógica de I/O
- Mover validações para `utils/text_utils.py`
- Garantir que `main.py` só orquestra — sem lógica de cifra dentro dele

### 2. Implementar Vigenère Cipher (`ciphers/vigenere.py`)
- Mesma interface do Caesar: `encrypt(text, key)` e `decrypt(text, key)`
- Chave deve ser uma string alfabética (validar em `utils/`)
- Preservar case e caracteres não-alfabéticos, igual ao Caesar atual

### 3. Loop pós-operação no `main.py`
- Após cifrar ou decifrar, perguntar se o usuário quer continuar
- Usar o dicionário `CIPHERS` já planejado — adicionar nova cifra = uma linha só

---

## Melhorias de interface (CLI)

- [ ] Adicionar cores com `colorama` ou `rich`
- [ ] Menu visual mais limpo com separadores e títulos
- [ ] Exibir créditos e versão na tela inicial
- [ ] Opção `--help` via `argparse` pra uso não-interativo (ex: `python main.py --cipher caesar --encrypt "hello" --key 3`)

> **Decisão pendente:** usar `rich` (mais recursos, tabelas, progress bars) ou `colorama` (mais leve, só cores). Para fins de currículo, `rich` demonstra mais.

---

## Detector automático de cifras (`detector/analyzer.py`)

Este é o objetivo de longo prazo do projeto: dado um texto, identificar automaticamente se ele está cifrado e qual cifra foi usada.

### Como vai funcionar

**Etapa 1 — Detectar se o texto está cifrado**
Comparar o Índice de Coincidência (IC) do texto com o IC esperado da língua:
- Português natural: IC ≈ 0.072
- Texto aleatório (cifrado forte): IC ≈ 0.038
- Texto com Caesar: IC ≈ 0.072 (IC preservado, só desloca)
- Texto com Vigenère: IC cai dependendo do tamanho da chave

**Etapa 2 — Identificar a cifra**

| Cifra | Sinal |
|---|---|
| Caesar | IC normal + distribuição deslocada uniformemente |
| Vigenère | IC reduzido + padrão periódico (Kasiski / Friedman) |
| XOR | IC muito baixo + padrão binário |

**Etapa 3 — Tentar decifrar automaticamente**
- Caesar: brute force nos 25 shifts, ranquear pelo IC mais próximo do português
- Vigenère: estimar tamanho da chave (Kasiski), depois análise de frequência por fatia
- Apresentar os N melhores resultados com score de confiança

**Etapa 4 — Sugerir cifra ao usuário**
Se o texto não parece cifrado, perguntar qual cifra seria mais adequada dependendo do conteúdo (tamanho, sensibilidade, uso).

### Referências para implementação
- Índice de Coincidência: Friedman (1922)
- Teste de Kasiski para Vigenère
- `collections.Counter` para análise de frequência em Python

---

## Cifras planejadas para o futuro

| Cifra | Complexidade | Prioridade | Observação |
|---|---|---|---|
| Vigenère | Média | Alta | Próxima a implementar |
| XOR | Baixa | Média | Boa pra demonstrar operações bitwise |
| ROT13 | Baixa | Baixa | Caso especial do Caesar (shift=13) |
| RSA | Alta | Baixa | Requer `cryptography` ou `rsa` lib — mais demonstrativo que prático |
| Hash SHA-256 | N/A | Média | Não é cifra reversível — separar em módulo `hashing/` |

> **Nota:** SHA-256 não é uma cifra — é uma função de hash unidirecional. Quando implementado, deve ficar em `hashing/` e não em `ciphers/` para não passar conceito errado.

---

## Decisões técnicas registradas

**Por que estrutura modular e não tudo em um arquivo?**
O objetivo futuro de detecção automática exige que o `detector/` importe qualquer cifra de forma independente. Com tudo em um arquivo, isso vira um acoplamento difícil de manter.

**Por que não usar `argparse` agora?**
O foco atual é a lógica das cifras. CLI avançada entra depois que a base estiver sólida e testada.

**Por que `utils/` existe separado?**
Funções como `validate_input()`, `clean_text()` e `print_result()` seriam repetidas em cada cifra. Centralizar evita inconsistências quando o projeto crescer.

---

## Ideias em aberto (sem prazo)

- Interface web simples com Flask ou Streamlit
- Modo "desafio": o programa cifra uma mensagem e o usuário tenta quebrar manualmente
- Suporte a arquivos `.txt` como input/output
- Testes automatizados com `pytest` para cada cifra
- Internacionalização: suporte a análise de frequência em inglês, espanhol e português

---

*Última atualização: refatoração inicial + planejamento modular*