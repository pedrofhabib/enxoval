# -*- coding: utf-8 -*-
"""Gera seeds.json a partir de:
   - 'Enxoval_Joao_Pedro_Comparativo vf.xlsx' (ROUPAS POR FASE) -> seed de roupas (autoritativo)
   - seed.json anterior -> seed 'geral' (tudo que NAO e roupa por fase)
"""
import json

# ---------------- roupas (planilha vf) ----------------
# it(cat, nome, qtd, tamanho, nota)
def it(cat, name, qty, size, note=""):
    return {"cat": cat, "name": name, "qty": qty, "size": size, "note": note, "source": None}

ROUPAS_ITEMS = [
    # FASE 1 - RN (nascimento ate ~1 mes). Dura pouco, comprar o minimo.
    it("roupas_rn", "Body manga curta", 4, "RN", "Clima de Salvador: priorize manga curta (Carter's)"),
    it("roupas_rn", "Body manga longa", 4, "RN", "Para ar-condicionado e noites; levar 2 para a maternidade"),
    it("roupas_rn", "Roupa de sair", 2, "RN", "As que vao para a mala da maternidade"),
    it("roupas_rn", "Saida de maternidade", 2, "RN", "Roupa de maternidade azul marinho completa com manta + saida bege"),
    it("roupas_rn", "Enxoval de berco", 4, "RN", "Levar 2 jogos para a maternidade; comprar lencol de elastico"),
    it("roupas_rn", "Meias", 1, "RN", "1 pacote"),
    it("roupas_rn", "Sapatinho", 1, "RN", "Sapato quase nao e usado nessa fase"),
    it("roupas_rn", "Saco de dormir", 1, "RN", "Swaddle"),
    it("roupas_rn", "Luvas", 1, "RN", "Evita arranhoes no rostinho"),

    # FASE 2 - 0-3 meses / P. Fase de muitas trocas (2-4 bodies por dia).
    it("roupas_p", "Body manga curta", 6, "P", "Carter's"),
    it("roupas_p", "Body manga longa", 4, "P", ""),
    it("roupas_p", "Roupa de sair", 2, "P", ""),
    it("roupas_p", "Meias", 1, "P", "1 pacote"),
    it("roupas_p", "Sapatos", 1, "P", ""),

    # FASE 3 - 3-6 meses / M. Fase mais longa: vale investir mais.
    it("roupas_m", "Body manga curta", 7, "M", ""),
    it("roupas_m", "Body manga longa", 3, "M", ""),
    it("roupas_m", "Roupa de sair", 3, "M", ""),
    it("roupas_m", "Meias", 1, "M", "1 pacote"),
    it("roupas_m", "Sapatos", 2, "M", ""),

    # FASE 4 - 6-9 meses / G. Comprar com moderacao.
    it("roupas_g", "Body manga curta", 5, "G", "Carter's. Ideal na planilha: 5 a 6 unidades"),
    it("roupas_g", "Body manga longa", 2, "G", ""),
    it("roupas_g", "Roupa de sair", 2, "G", "Ideal na planilha: 2 a 4 unidades"),
    it("roupas_g", "Meias", 1, "G", "1 pacote"),
    it("roupas_g", "Sapatos", 2, "G", ""),
    it("roupas_g", "Roupa UV piscina/praia", 1, "G", ""),

    # FASE 5 - 9-12 meses / GG. Comprar com moderacao (crescimento imprevisivel).
    it("roupas_gg", "Body manga curta", 5, "GG", ""),
    it("roupas_gg", "Body manga longa", 2, "GG", ""),
    it("roupas_gg", "Roupa de sair", 3, "GG", "Ideal na planilha: 3 a 4 unidades"),
    it("roupas_gg", "Meias", 1, "GG", "1 pacote"),
    it("roupas_gg", "Roupa UV piscina/praia", 1, "GG", ""),
    it("roupas_gg", "Sapatos", 1, "GG", ""),
]

def pc(desc, size, cat, item, note=""):
    return {"desc": desc, "size": size, "note": note, "link": [cat, item]}

# "Ja tenho" da planilha, com os nomes que as dicas descrevem
ROUPAS_PIECES = [
    # RN: body manga longa (2) - "o da Girafa e o conjunto da Tous"
    pc("Body manga longa da girafa", "RN", "roupas_rn", "Body manga longa"),
    pc("Conjunto body manga longa Tous", "RN", "roupas_rn", "Body manga longa"),
    # RN: saida de maternidade (2)
    pc("Saida de maternidade", "RN", "roupas_rn", "Saida de maternidade"),
    pc("Saida de maternidade", "RN", "roupas_rn", "Saida de maternidade"),
    # RN: enxoval de berco (2)
    pc("Jogo de enxoval de berco", "RN", "roupas_rn", "Enxoval de berco"),
    pc("Jogo de enxoval de berco", "RN", "roupas_rn", "Enxoval de berco"),
    pc("Meias", "RN", "roupas_rn", "Meias", "Pacote com 7 pares"),
    pc("Sapatinho All Star tamanho 1", "RN", "roupas_rn", "Sapatinho"),
    pc("Luvas", "RN", "roupas_rn", "Luvas", "Vem no conjunto da saida da maternidade"),
    # P: body manga longa (4) - macacoes descritos na dica
    pc("Macacao de ima", "P", "roupas_p", "Body manga longa"),
    pc("Macacao Hello World", "P", "roupas_p", "Body manga longa"),
    pc("Macacao polo", "P", "roupas_p", "Body manga longa"),
    pc("Macacao girafa", "P", "roupas_p", "Body manga longa"),
    # P: roupa de sair (1)
    pc("Conjunto short e blusa bege de ursinho", "P", "roupas_p", "Roupa de sair"),
    # M: body manga curta (3)
    pc("Body de cachorrinho", "M", "roupas_m", "Body manga curta"),
    pc("Body de cachorrinho", "M", "roupas_m", "Body manga curta"),
    pc("Body do Flamengo", "M", "roupas_m", "Body manga curta"),
    # M: body manga longa (1)
    pc("Body de ursinho Trousseau", "M", "roupas_m", "Body manga longa"),
    # M: roupa de sair (1)
    pc("Body de linha com sapatinho", "M", "roupas_m", "Roupa de sair"),
    # GG: body manga curta (1)
    pc("Body de barquinho", "GG", "roupas_gg", "Body manga curta"),
]

# ---------------- geral (resto do enxoval, do arquivo anterior) ----------------
old = json.load(open("seed.json", encoding="utf-8"))
PHASE_CATS = {"roupas_rn", "roupas_p", "roupas_m", "roupas_g", "roupas_gg"}
# itens de roupa por fase saem (a planilha vf manda neles);
# "Enxoval de berco" e "Saco de dormir" migraram para a fase RN
DROP_GERAL = {("quarto", "Enxoval de berco"), ("quarto", "Saco de dormir")}
GERAL_ITEMS = [i for i in old["items"]
               if i["cat"] not in PHASE_CATS and (i["cat"], i["name"]) not in DROP_GERAL]

# pecas antigas: mantem so as que NAO sao vestuario por fase
KEEP_PIECE_DESC = {
    "Toalha de banho com capuz", "Cueiro com pelinhos", "Cueiro em algodao",
    "Mamadeira Avent", "Escova limpadora de mamadeira Avent", "Pano de boca",
    "Projetor de estrelas", "Naninha",
}
GERAL_PIECES = [p for p in old["pieces"] if p["desc"] in KEEP_PIECE_DESC]

CATS = old["cats"]
out = {
    "cats": CATS,
    "roupas": {"items": ROUPAS_ITEMS, "pieces": ROUPAS_PIECES},
    "geral": {"items": GERAL_ITEMS, "pieces": GERAL_PIECES},
    "tips": old["tips"],
}
with open("seeds.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))

ru = sum(i["qty"] for i in ROUPAS_ITEMS)
print("roupas: %d itens (%d unidades), %d pecas ja tenho" % (len(ROUPAS_ITEMS), ru, len(ROUPAS_PIECES)))
print("geral : %d itens, %d pecas" % (len(GERAL_ITEMS), len(GERAL_PIECES)))
