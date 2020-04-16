# coding: utf-8

import random
import math
import time

""" simulation d'une chaine de montage de piston """
t_piston = "tete du piston"
j_piston = "jupe du piston"
a_piston = "axe du piston"

c_tete = []
c_jupe = []
c_axe = []

c_piston = [t_piston, j_piston, a_piston]


# simulation d'un dock
def create_dock(n_carton):
    """ simulation d'un dock """
    try:
        assert n_carton > 0, "Ce dock est vide, assurez qu'il n'est pas vide afin d'exécuter ce programme."
        dock_cree = []
        carton = []
        total_pc = 30

        i = 0
        while i < n_carton:

            while len(carton) < total_pc:
                pc_index = math.floor(random.random() * 3)
                carton.append(c_piston[pc_index])

            dock_cree.append(carton)

            i += 1
        return dock_cree

    except Exception:
        print("Erreur")


dock = create_dock(10)


# print(dock)
# print(len(dock))


# triage du dock,
# cette opération consiste à trier les cartons sur le dock afin de regrouper chaque pièces selon sa nature.
def trie_pc(dock=0):
    try:
        assert len(dock) > 0, 'un dock vide ne peut etre tier.'

        tete, jupe, axe = ['tete', 'jupe', 'axe']
        dock_vide = 0
        for cartons in dock:
            for pc in cartons:
                c_tete.append({tete: pc}) if tete in pc else c_jupe.append({jupe: pc}) if jupe in pc else c_axe.append({axe: pc})

        return [c_tete, c_jupe, c_axe]

    except Exception:
        print("Erreur")


trier = trie_pc(dock)


# print(trier)
# print(len(trier))


def usinage_mt(block_t):
    block_t_fini = []
    tps_usinage_tete = 120 * len(block_t) - random.randint(5, 15) * 60
    print(tps_usinage_tete)
    success = False
    start = time.time()
    for piece in block_t:

        for pc in piece:
            block_t_fini.append(piece[pc].strip())

    print(f"start time: ", start)
    print(f"new time: ", time.time())
    end = time.time() - start
    if end <= tps_usinage_tete:
        success = True
        if success:
            print(f"Temps d'usinage, environs: {math.ceil(tps_usinage_tete)}s")
            return block_t_fini


usinage = usinage_mt(trier[0])
print(usinage)