# -*- coding: utf-8 -*-
"""Gera seeds.json.

roupas: planilha 'Enxoval_Joao_Pedro_Comparativo vf.xlsx' (30/08) - coluna
        'Falta comprar' e a operativa. Cada item traz 'falta' (quantas unidades
        ainda faltam); o app calcula qty = ja_tenho + falta.
geral : demais itens do enxoval (higiene, quarto, alimentacao, farmacia, passeio).
"""
import json

def it(cat, name, falta, size, note=""):
    return {"cat": cat, "name": name, "falta": falta, "size": size, "note": note, "source": None}

# ---- FASE 1 - RN (nascimento ate ~1 mes): dura pouco, comprar o minimo ----
ROUPAS_ITEMS = [
    it("roupas_rn", "Body manga curta", 5, "RN", "Clima de Salvador: priorize manga curta (Carter's). Qtd ideal na planilha: 4"),
    it("roupas_rn", "Body manga longa", 5, "RN", "Para ar-condicionado e noites; levar 2 para a maternidade. Qtd ideal na planilha: 4"),
    it("roupas_rn", "Calca", 6, "RN"),
    it("roupas_rn", "Macacao", 5, "RN"),
    it("roupas_rn", "Enxoval de berco", 1, "RN", "Levar 2 jogos para a maternidade; comprar lencol de elastico"),
    it("roupas_rn", "Meias", 1, "RN", "1 pacote"),
    it("roupas_rn", "Saco de dormir", 1, "RN", "Swaddle"),
    it("roupas_rn", "Saida de maternidade", 0, "RN", "Ja completo"),
    it("roupas_rn", "Sapatinho", 0, "RN", "Sapato quase nao e usado nessa fase"),
    it("roupas_rn", "Luvas", 0, "RN", "Evita arranhoes no rostinho"),

    # ---- FASE 2 - 0-3 meses / P: fase de muitas trocas (2-4 bodies por dia) ----
    it("roupas_p", "Body manga curta", 10, "P", "Carter's. Qtd ideal na planilha: 6"),
    it("roupas_p", "Body manga longa", 5, "P", "Qtd ideal na planilha: 4"),
    it("roupas_p", "Short", 5, "P"),
    it("roupas_p", "Calca", 10, "P"),
    it("roupas_p", "Macacao", 3, "P"),
    it("roupas_p", "Meias", 1, "P", "1 pacote"),
    it("roupas_p", "Sapatos", 1, "P"),
    it("roupas_p", "Roupa de sair", 0, "P", "Ja completo"),

    # ---- FASE 3 - 3-6 meses / M: fase mais longa, vale investir mais ----
    it("roupas_m", "Body manga curta", 10, "M", "Qtd ideal na planilha: 7"),
    it("roupas_m", "Body manga longa", 2, "M", "Qtd ideal na planilha: 3"),
    it("roupas_m", "Calca", 4, "M"),
    it("roupas_m", "Short", 10, "M"),
    it("roupas_m", "Blusa", 8, "M"),
    it("roupas_m", "Macacao", 4, "M"),
    it("roupas_m", "Meias", 1, "M", "1 pacote"),
    it("roupas_m", "Sapatos", 2, "M"),
    it("roupas_m", "Roupa piscina/praia", 1, "M"),
    it("roupas_m", "Roupa de sair", 0, "M", "Ja completo"),

    # ---- FASE 4 - 6-9 meses / G: comprar com moderacao ----
    it("roupas_g", "Body manga curta", 6, "G", "Qtd ideal na planilha: 5 a 6"),
    it("roupas_g", "Blusa", 8, "G"),
    it("roupas_g", "Short", 8, "G"),
    it("roupas_g", "Macacao", 2, "G", "Qtd ideal na planilha: 2"),
    it("roupas_g", "Roupa de sair", 4, "G", "Qtd ideal na planilha: 2 a 4"),
    it("roupas_g", "Meias", 1, "G", "1 pacote"),
    it("roupas_g", "Sapatos", 2, "G"),
    it("roupas_g", "Roupa piscina/praia", 2, "G", "Qtd ideal na planilha: 1"),

    # ---- FASE 5 - 9-12 meses / GG: comprar com moderacao (crescimento imprevisivel) ----
    it("roupas_gg", "Short", 12, "GG", "Qtd ideal na planilha: 5"),
    it("roupas_gg", "Blusa", 12, "GG"),
    it("roupas_gg", "Calca", 4, "GG"),
    it("roupas_gg", "Pijama", 4, "GG", "Qtd ideal na planilha: 2"),
    it("roupas_gg", "Meias", 1, "GG", "1 pacote"),
    it("roupas_gg", "Sapatos", 2, "GG", "Qtd ideal na planilha: 1"),
    it("roupas_gg", "Roupa piscina/praia", 4, "GG"),
    it("roupas_gg", "Body manga curta", 0, "GG", "Ja completo"),
]

def pc(desc, size, cat, item, note=""):
    return {"desc": desc, "size": size, "note": note, "link": [cat, item]}

# "Ja tenho" levantado na versao anterior da planilha - continuam validos
ROUPAS_PIECES = [
    pc("Body manga longa da girafa", "RN", "roupas_rn", "Body manga longa"),
    pc("Conjunto body manga longa Tous", "RN", "roupas_rn", "Body manga longa"),
    pc("Saida de maternidade", "RN", "roupas_rn", "Saida de maternidade"),
    pc("Saida de maternidade", "RN", "roupas_rn", "Saida de maternidade"),
    pc("Jogo de enxoval de berco", "RN", "roupas_rn", "Enxoval de berco"),
    pc("Jogo de enxoval de berco", "RN", "roupas_rn", "Enxoval de berco"),
    pc("Meias", "RN", "roupas_rn", "Meias", "Pacote com 7 pares"),
    pc("Sapatinho All Star tamanho 1", "RN", "roupas_rn", "Sapatinho"),
    pc("Luvas", "RN", "roupas_rn", "Luvas", "Vem no conjunto da saida da maternidade"),
    pc("Macacao de ima", "P", "roupas_p", "Body manga longa"),
    pc("Macacao Hello World", "P", "roupas_p", "Body manga longa"),
    pc("Macacao polo", "P", "roupas_p", "Body manga longa"),
    pc("Macacao girafa", "P", "roupas_p", "Body manga longa"),
    pc("Conjunto short e blusa bege de ursinho", "P", "roupas_p", "Roupa de sair"),
    pc("Body de cachorrinho", "M", "roupas_m", "Body manga curta"),
    pc("Body de cachorrinho", "M", "roupas_m", "Body manga curta"),
    pc("Body do Flamengo", "M", "roupas_m", "Body manga curta"),
    pc("Body de ursinho Trousseau", "M", "roupas_m", "Body manga longa"),
    pc("Body de linha com sapatinho", "M", "roupas_m", "Roupa de sair"),
    pc("Body de barquinho", "GG", "roupas_gg", "Body manga curta"),
]

# itens que mudaram de nome entre versoes da planilha
RENAME = [
    {"cat": "roupas_g", "from": "Roupa UV piscina/praia", "to": "Roupa piscina/praia"},
    {"cat": "roupas_gg", "from": "Roupa UV piscina/praia", "to": "Roupa piscina/praia"},
]
# itens da versao anterior que sairam da planilha (nenhuma compra registrada neles)
OBSOLETE = [
    {"cat": "roupas_rn", "name": "Roupa de sair"},
    {"cat": "roupas_g", "name": "Body manga longa"},
    {"cat": "roupas_gg", "name": "Body manga longa"},
    {"cat": "roupas_gg", "name": "Roupa de sair"},
]

# ---------------- geral (inalterado) ----------------
prev = json.load(open("seeds.json", encoding="utf-8"))
out = {
    "cats": prev["cats"],
    "roupas": {"items": ROUPAS_ITEMS, "pieces": ROUPAS_PIECES, "rename": RENAME, "obsolete": OBSOLETE},
    "geral": prev["geral"],
    "tips": prev["tips"],
}
json.dump(out, open("seeds.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

falta = sum(i["falta"] for i in ROUPAS_ITEMS)
print("roupas: %d itens, %d unidades a comprar, %d pecas 'ja tenho'"
      % (len(ROUPAS_ITEMS), falta, len(ROUPAS_PIECES)))
print("geral : %d itens" % len(prev["geral"]["items"]))
for c in ["roupas_rn", "roupas_p", "roupas_m", "roupas_g", "roupas_gg"]:
    sel = [i for i in ROUPAS_ITEMS if i["cat"] == c]
    print("  %-12s %2d itens, %3d unidades" % (c, len(sel), sum(i["falta"] for i in sel)))
