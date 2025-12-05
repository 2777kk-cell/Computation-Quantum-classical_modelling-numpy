from libs import *

#####--------------------------#####
def get_pair_combinations(list1, list2):
    """
    Generates all possible combinations from list1 and list2
    Example: get_pair_combinations(["A", "B"], [1,2])
             [("A",1),("A",2),("B",1),("B",2),(1, 'A'),(1, 'B'),(2, 'A'),(2, 'B')]
    """
    combinations = []
    for item1 in list1:
        for item2 in list2:
            combinations.append((item1, item2))

    for item2 in list2:
        for item1 in list1:
            combinations.append((item2, item1))

    return combinations


#####--------------------------#####
def single_qubits_pair(basis=None):
    basis_list = [KET_0, KET_1, KET_YP, KET_YM, KET_XP, KET_XM]
    def inner(inList:list):
        return [qb_tuple for qb_tuple in product(inList, inList)]
        
    if basis:
        print(not basis)
        if basis.upper()=="Z":
            return inner(basis_list[:2])
        if basis.upper() =="Y":
            return inner(basis_list[2:4])
        if basis.upper()=="X":
            return inner(basis_list[4:])

    return inner(basis_list) 

#####--------------------------#####
def bell_pair():
    bell_2_pair = [BELL_00, BELL_01, BELL_10, BELL_11]
    def inner(inList:list):
        return [qb_tuple for qb_tuple in product(inList, inList)]

    return inner(bell_2_pair)


#####--------------------------#####
def nearest_kron_prod(input_ket_vector):
    KRON_PROD_RES = None
    A = input_ket_vector
    tolerance = 0.0000098
    if not A.shape[1] ==1:
        raise Exception("This custom method handls only Ket Vector or Column Matrix/array only")
        
    """***This returns a pair of ket vector (|x>_[(2x1)], |y>_[2x1])***"""
    if A.shape[0]==4:
        def non_entangled():
            for qubit_tuple in single_qubits_pair():
                phi = A - reduce(kron, list(qubit_tuple))
                phi_norm = float(np.linalg.norm(phi))
                if 0<= phi_norm <= tolerance:
                    return {'size': 2, 'frobenius-norm': phi_norm, 'qubit-pair' : qubit_tuple, 'ent':False}
                else:
                    continue

            return None

        def entangled():
            bell_pairs = [BELL_00, BELL_01, BELL_10, BELL_11]
            for qubit_state in bell_pairs:
                phi = A - qubit_state
                phi_norm = float(np.linalg.norm(phi))
                if 0<= phi_norm <= tolerance:
                    return {'size': 1, 'frobenius-norm': phi_norm, 'qubit-pair' : qubit_state, 'ent':True}
                else:
                    continue
                    
            return None
            

    if non_entangled() ==None:
        return entangled()
    else:
        return non_entangled()


