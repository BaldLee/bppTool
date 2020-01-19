import time
from z3 import *
from structure import *

start = time.clock()
t = Solver()
u = []
for i in range(process_num):
    u.append(initial_expr[i])

u179 = [Int('u179_%d' %i) for i in range(2)]
u179 = [Int('u179_%d' %i) for i in range(2)]
u199 = [Int('u199_%d' %i) for i in range(2)]
u957 = [Int('u957_%d' %i) for i in range(2)]
u112 = [Int('u112_%d' %i) for i in range(2)]
u865 = [Int('u865_%d' %i) for i in range(2)]
u655 = [Int('u655_%d' %i) for i in range(2)]
u796 = [Int('u796_%d' %i) for i in range(2)]
u134 = [Int('u134_%d' %i) for i in range(2)]
u428 = [Int('u428_%d' %i) for i in range(2)]
u292 = [Int('u292_%d' %i) for i in range(2)]
u246 = [Int('u246_%d' %i) for i in range(2)]
u1050 = [Int('u1050_%d' %i) for i in range(2)]
u1232 = [Int('u1232_%d' %i) for i in range(2)]
u1402 = [Int('u1402_%d' %i) for i in range(2)]
u1381 = [Int('u1381_%d' %i) for i in range(2)]
left_side_cstr_u179_0 = u[0] >= 1
trans_u179_0 = And(u179[0] == u179[0]-1+0, u179[1] == u179[1]+1)
possi_u179_0 = And(left_side_cstr_u179_0, trans_u179_0)
left_side_cstr_u179_1 = u[1] >= 1
trans_u179_1 = And(u179[0] == u179[0]+2, u179[1] == u179[1]-1+0)
possi_u179_1 = And(left_side_cstr_u179_1, trans_u179_1)
bigDisj_u179 = Or(possi_u179_0, possi_u179_1)
left_side_cstr_u179_0 = u[0] >= 1
trans_u179_0 = And(u199[0] == u179[0]-1+0, u199[1] == u179[1]+1)
possi_u179_0 = And(left_side_cstr_u179_0, trans_u179_0)
left_side_cstr_u179_1 = u[1] >= 1
trans_u179_1 = And(u199[0] == u179[0]+2, u199[1] == u179[1]-1+0)
possi_u179_1 = And(left_side_cstr_u179_1, trans_u179_1)
bigDisj_u179 = Or(possi_u179_0, possi_u179_1)
left_side_cstr_u199_0 = u[0] >= 1
trans_u199_0 = And(u957[0] == u199[0]-1+0, u957[1] == u199[1]+1)
possi_u199_0 = And(left_side_cstr_u199_0, trans_u199_0)
left_side_cstr_u199_1 = u[1] >= 1
trans_u199_1 = And(u957[0] == u199[0]+2, u957[1] == u199[1]-1+0)
possi_u199_1 = And(left_side_cstr_u199_1, trans_u199_1)
bigDisj_u199 = Or(possi_u199_0, possi_u199_1)
left_side_cstr_u957_0 = u[0] >= 1
trans_u957_0 = And(u112[0] == u957[0]-1+0, u112[1] == u957[1]+1)
possi_u957_0 = And(left_side_cstr_u957_0, trans_u957_0)
left_side_cstr_u957_1 = u[1] >= 1
trans_u957_1 = And(u112[0] == u957[0]+2, u112[1] == u957[1]-1+0)
possi_u957_1 = And(left_side_cstr_u957_1, trans_u957_1)
bigDisj_u957 = Or(possi_u957_0, possi_u957_1)
left_side_cstr_u112_0 = u[0] >= 1
trans_u112_0 = And(u865[0] == u112[0]-1+0, u865[1] == u112[1]+1)
possi_u112_0 = And(left_side_cstr_u112_0, trans_u112_0)
left_side_cstr_u112_1 = u[1] >= 1
trans_u112_1 = And(u865[0] == u112[0]+2, u865[1] == u112[1]-1+0)
possi_u112_1 = And(left_side_cstr_u112_1, trans_u112_1)
bigDisj_u112 = Or(possi_u112_0, possi_u112_1)
left_side_cstr_u865_0 = u[0] >= 1
trans_u865_0 = And(u655[0] == u865[0]-1+0, u655[1] == u865[1]+1)
possi_u865_0 = And(left_side_cstr_u865_0, trans_u865_0)
left_side_cstr_u865_1 = u[1] >= 1
trans_u865_1 = And(u655[0] == u865[0]+2, u655[1] == u865[1]-1+0)
possi_u865_1 = And(left_side_cstr_u865_1, trans_u865_1)
bigDisj_u865 = Or(possi_u865_0, possi_u865_1)
left_side_cstr_u655_0 = u[0] >= 1
trans_u655_0 = And(u796[0] == u655[0]-1+0, u796[1] == u655[1]+1)
possi_u655_0 = And(left_side_cstr_u655_0, trans_u655_0)
left_side_cstr_u655_1 = u[1] >= 1
trans_u655_1 = And(u796[0] == u655[0]+2, u796[1] == u655[1]-1+0)
possi_u655_1 = And(left_side_cstr_u655_1, trans_u655_1)
bigDisj_u655 = Or(possi_u655_0, possi_u655_1)
left_side_cstr_u796_0 = u[0] >= 1
trans_u796_0 = And(u134[0] == u796[0]-1+0, u134[1] == u796[1]+1)
possi_u796_0 = And(left_side_cstr_u796_0, trans_u796_0)
left_side_cstr_u796_1 = u[1] >= 1
trans_u796_1 = And(u134[0] == u796[0]+2, u134[1] == u796[1]-1+0)
possi_u796_1 = And(left_side_cstr_u796_1, trans_u796_1)
bigDisj_u796 = Or(possi_u796_0, possi_u796_1)
left_side_cstr_u134_0 = u[0] >= 1
trans_u134_0 = And(u428[0] == u134[0]-1+0, u428[1] == u134[1]+1)
possi_u134_0 = And(left_side_cstr_u134_0, trans_u134_0)
left_side_cstr_u134_1 = u[1] >= 1
trans_u134_1 = And(u428[0] == u134[0]+2, u428[1] == u134[1]-1+0)
possi_u134_1 = And(left_side_cstr_u134_1, trans_u134_1)
bigDisj_u134 = Or(possi_u134_0, possi_u134_1)
left_side_cstr_u428_0 = u[0] >= 1
trans_u428_0 = And(u292[0] == u428[0]-1+0, u292[1] == u428[1]+1)
possi_u428_0 = And(left_side_cstr_u428_0, trans_u428_0)
left_side_cstr_u428_1 = u[1] >= 1
trans_u428_1 = And(u292[0] == u428[0]+2, u292[1] == u428[1]-1+0)
possi_u428_1 = And(left_side_cstr_u428_1, trans_u428_1)
bigDisj_u428 = Or(possi_u428_0, possi_u428_1)
left_side_cstr_u292_0 = u[0] >= 1
trans_u292_0 = And(u246[0] == u292[0]-1+0, u246[1] == u292[1]+1)
possi_u292_0 = And(left_side_cstr_u292_0, trans_u292_0)
left_side_cstr_u292_1 = u[1] >= 1
trans_u292_1 = And(u246[0] == u292[0]+2, u246[1] == u292[1]-1+0)
possi_u292_1 = And(left_side_cstr_u292_1, trans_u292_1)
bigDisj_u292 = Or(possi_u292_0, possi_u292_1)
left_side_cstr_u246_0 = u[0] >= 1
trans_u246_0 = And(u1050[0] == u246[0]-1+0, u1050[1] == u246[1]+1)
possi_u246_0 = And(left_side_cstr_u246_0, trans_u246_0)
left_side_cstr_u246_1 = u[1] >= 1
trans_u246_1 = And(u1050[0] == u246[0]+2, u1050[1] == u246[1]-1+0)
possi_u246_1 = And(left_side_cstr_u246_1, trans_u246_1)
bigDisj_u246 = Or(possi_u246_0, possi_u246_1)
left_side_cstr_u1050_0 = u[0] >= 1
trans_u1050_0 = And(u1232[0] == u1050[0]-1+0, u1232[1] == u1050[1]+1)
possi_u1050_0 = And(left_side_cstr_u1050_0, trans_u1050_0)
left_side_cstr_u1050_1 = u[1] >= 1
trans_u1050_1 = And(u1232[0] == u1050[0]+2, u1232[1] == u1050[1]-1+0)
possi_u1050_1 = And(left_side_cstr_u1050_1, trans_u1050_1)
bigDisj_u1050 = Or(possi_u1050_0, possi_u1050_1)
left_side_cstr_u1232_0 = u[0] >= 1
trans_u1232_0 = And(u1402[0] == u1232[0]-1+0, u1402[1] == u1232[1]+1)
possi_u1232_0 = And(left_side_cstr_u1232_0, trans_u1232_0)
left_side_cstr_u1232_1 = u[1] >= 1
trans_u1232_1 = And(u1402[0] == u1232[0]+2, u1402[1] == u1232[1]-1+0)
possi_u1232_1 = And(left_side_cstr_u1232_1, trans_u1232_1)
bigDisj_u1232 = Or(possi_u1232_0, possi_u1232_1)
left_side_cstr_u1402_0 = u[0] >= 1
trans_u1402_0 = And(u1381[0] == u1402[0]-1+0, u1381[1] == u1402[1]+1)
possi_u1402_0 = And(left_side_cstr_u1402_0, trans_u1402_0)
left_side_cstr_u1402_1 = u[1] >= 1
trans_u1402_1 = And(u1381[0] == u1402[0]+2, u1381[1] == u1402[1]-1+0)
possi_u1402_1 = And(left_side_cstr_u1402_1, trans_u1402_1)
bigDisj_u1402 = Or(possi_u1402_0, possi_u1402_1)
path_u = And(bigDisj_u179, bigDisj_u179, bigDisj_u199, bigDisj_u957, bigDisj_u112, bigDisj_u865, bigDisj_u655, bigDisj_u796, bigDisj_u134, bigDisj_u428, bigDisj_u292, bigDisj_u246, bigDisj_u1050, bigDisj_u1232, bigDisj_u1402)
initial_u = And(u179[0] == u[0], u179[1] == u[1])
u502 = [Int('u502_%d' %i) for i in range(2)]
act_cstr_u179_0 = 5 == 5
left_side_cstr_u179_0 = u179[0] >= 1
trans_u179_0 = And(u502[0] == u179[0]-1+0, u502[1] == u179[1]+1)
possi_u179_0 = And(act_cstr_u179_0, left_side_cstr_u179_0, trans_u179_0)
act_cstr_u179_1 = 5 == 10
left_side_cstr_u179_1 = u179[1] >= 1
trans_u179_1 = And(u502[0] == u179[0]+2, u502[1] == u179[1]-1+0)
possi_u179_1 = And(act_cstr_u179_1, left_side_cstr_u179_1, trans_u179_1)
bigDisj4ea_u179 = Or(possi_u179_0, possi_u179_1)
atom_u502 = u502[0] * 1 + u502[1] * 1 >= 2
ea_u179 = And(15 >= 1, Exists([u502[0], u502[1]], And(bigDisj4ea_u179, atom_u502)))
u1251 = [Int('u1251_%d' %i) for i in range(2)]
act_cstr_u179_0 = 5 == 5
left_side_cstr_u179_0 = u179[0] >= 1
trans_u179_0 = And(u1251[0] == u179[0]-1+0, u1251[1] == u179[1]+1)
possi_u179_0 = And(act_cstr_u179_0, left_side_cstr_u179_0, trans_u179_0)
act_cstr_u179_1 = 5 == 10
left_side_cstr_u179_1 = u179[1] >= 1
trans_u179_1 = And(u1251[0] == u179[0]+2, u1251[1] == u179[1]-1+0)
possi_u179_1 = And(act_cstr_u179_1, left_side_cstr_u179_1, trans_u179_1)
bigDisj4ea_u179 = Or(possi_u179_0, possi_u179_1)
atom_u1251 = u1251[0] * 1 + u1251[1] * 1 >= 2
ea_u179 = And(15 >= 1, Exists([u1251[0], u1251[1]], And(bigDisj4ea_u179, atom_u1251)))
u782 = [Int('u782_%d' %i) for i in range(2)]
act_cstr_u199_0 = 5 == 5
left_side_cstr_u199_0 = u199[0] >= 1
trans_u199_0 = And(u782[0] == u199[0]-1+0, u782[1] == u199[1]+1)
possi_u199_0 = And(act_cstr_u199_0, left_side_cstr_u199_0, trans_u199_0)
act_cstr_u199_1 = 5 == 10
left_side_cstr_u199_1 = u199[1] >= 1
trans_u199_1 = And(u782[0] == u199[0]+2, u782[1] == u199[1]-1+0)
possi_u199_1 = And(act_cstr_u199_1, left_side_cstr_u199_1, trans_u199_1)
bigDisj4ea_u199 = Or(possi_u199_0, possi_u199_1)
atom_u782 = u782[0] * 1 + u782[1] * 1 >= 2
ea_u199 = And(15 >= 1, Exists([u782[0], u782[1]], And(bigDisj4ea_u199, atom_u782)))
u760 = [Int('u760_%d' %i) for i in range(2)]
act_cstr_u957_0 = 5 == 5
left_side_cstr_u957_0 = u957[0] >= 1
trans_u957_0 = And(u760[0] == u957[0]-1+0, u760[1] == u957[1]+1)
possi_u957_0 = And(act_cstr_u957_0, left_side_cstr_u957_0, trans_u957_0)
act_cstr_u957_1 = 5 == 10
left_side_cstr_u957_1 = u957[1] >= 1
trans_u957_1 = And(u760[0] == u957[0]+2, u760[1] == u957[1]-1+0)
possi_u957_1 = And(act_cstr_u957_1, left_side_cstr_u957_1, trans_u957_1)
bigDisj4ea_u957 = Or(possi_u957_0, possi_u957_1)
atom_u760 = u760[0] * 1 + u760[1] * 1 >= 2
ea_u957 = And(15 >= 1, Exists([u760[0], u760[1]], And(bigDisj4ea_u957, atom_u760)))
u472 = [Int('u472_%d' %i) for i in range(2)]
act_cstr_u112_0 = 5 == 5
left_side_cstr_u112_0 = u112[0] >= 1
trans_u112_0 = And(u472[0] == u112[0]-1+0, u472[1] == u112[1]+1)
possi_u112_0 = And(act_cstr_u112_0, left_side_cstr_u112_0, trans_u112_0)
act_cstr_u112_1 = 5 == 10
left_side_cstr_u112_1 = u112[1] >= 1
trans_u112_1 = And(u472[0] == u112[0]+2, u472[1] == u112[1]-1+0)
possi_u112_1 = And(act_cstr_u112_1, left_side_cstr_u112_1, trans_u112_1)
bigDisj4ea_u112 = Or(possi_u112_0, possi_u112_1)
atom_u472 = u472[0] * 1 + u472[1] * 1 >= 2
ea_u112 = And(15 >= 1, Exists([u472[0], u472[1]], And(bigDisj4ea_u112, atom_u472)))
u277 = [Int('u277_%d' %i) for i in range(2)]
act_cstr_u865_0 = 5 == 5
left_side_cstr_u865_0 = u865[0] >= 1
trans_u865_0 = And(u277[0] == u865[0]-1+0, u277[1] == u865[1]+1)
possi_u865_0 = And(act_cstr_u865_0, left_side_cstr_u865_0, trans_u865_0)
act_cstr_u865_1 = 5 == 10
left_side_cstr_u865_1 = u865[1] >= 1
trans_u865_1 = And(u277[0] == u865[0]+2, u277[1] == u865[1]-1+0)
possi_u865_1 = And(act_cstr_u865_1, left_side_cstr_u865_1, trans_u865_1)
bigDisj4ea_u865 = Or(possi_u865_0, possi_u865_1)
atom_u277 = u277[0] * 1 + u277[1] * 1 >= 2
ea_u865 = And(15 >= 1, Exists([u277[0], u277[1]], And(bigDisj4ea_u865, atom_u277)))
u587 = [Int('u587_%d' %i) for i in range(2)]
act_cstr_u655_0 = 5 == 5
left_side_cstr_u655_0 = u655[0] >= 1
trans_u655_0 = And(u587[0] == u655[0]-1+0, u587[1] == u655[1]+1)
possi_u655_0 = And(act_cstr_u655_0, left_side_cstr_u655_0, trans_u655_0)
act_cstr_u655_1 = 5 == 10
left_side_cstr_u655_1 = u655[1] >= 1
trans_u655_1 = And(u587[0] == u655[0]+2, u587[1] == u655[1]-1+0)
possi_u655_1 = And(act_cstr_u655_1, left_side_cstr_u655_1, trans_u655_1)
bigDisj4ea_u655 = Or(possi_u655_0, possi_u655_1)
atom_u587 = u587[0] * 1 + u587[1] * 1 >= 2
ea_u655 = And(15 >= 1, Exists([u587[0], u587[1]], And(bigDisj4ea_u655, atom_u587)))
u290 = [Int('u290_%d' %i) for i in range(2)]
act_cstr_u796_0 = 5 == 5
left_side_cstr_u796_0 = u796[0] >= 1
trans_u796_0 = And(u290[0] == u796[0]-1+0, u290[1] == u796[1]+1)
possi_u796_0 = And(act_cstr_u796_0, left_side_cstr_u796_0, trans_u796_0)
act_cstr_u796_1 = 5 == 10
left_side_cstr_u796_1 = u796[1] >= 1
trans_u796_1 = And(u290[0] == u796[0]+2, u290[1] == u796[1]-1+0)
possi_u796_1 = And(act_cstr_u796_1, left_side_cstr_u796_1, trans_u796_1)
bigDisj4ea_u796 = Or(possi_u796_0, possi_u796_1)
atom_u290 = u290[0] * 1 + u290[1] * 1 >= 2
ea_u796 = And(15 >= 1, Exists([u290[0], u290[1]], And(bigDisj4ea_u796, atom_u290)))
u898 = [Int('u898_%d' %i) for i in range(2)]
act_cstr_u134_0 = 5 == 5
left_side_cstr_u134_0 = u134[0] >= 1
trans_u134_0 = And(u898[0] == u134[0]-1+0, u898[1] == u134[1]+1)
possi_u134_0 = And(act_cstr_u134_0, left_side_cstr_u134_0, trans_u134_0)
act_cstr_u134_1 = 5 == 10
left_side_cstr_u134_1 = u134[1] >= 1
trans_u134_1 = And(u898[0] == u134[0]+2, u898[1] == u134[1]-1+0)
possi_u134_1 = And(act_cstr_u134_1, left_side_cstr_u134_1, trans_u134_1)
bigDisj4ea_u134 = Or(possi_u134_0, possi_u134_1)
atom_u898 = u898[0] * 1 + u898[1] * 1 >= 2
ea_u134 = And(15 >= 1, Exists([u898[0], u898[1]], And(bigDisj4ea_u134, atom_u898)))
u626 = [Int('u626_%d' %i) for i in range(2)]
act_cstr_u428_0 = 5 == 5
left_side_cstr_u428_0 = u428[0] >= 1
trans_u428_0 = And(u626[0] == u428[0]-1+0, u626[1] == u428[1]+1)
possi_u428_0 = And(act_cstr_u428_0, left_side_cstr_u428_0, trans_u428_0)
act_cstr_u428_1 = 5 == 10
left_side_cstr_u428_1 = u428[1] >= 1
trans_u428_1 = And(u626[0] == u428[0]+2, u626[1] == u428[1]-1+0)
possi_u428_1 = And(act_cstr_u428_1, left_side_cstr_u428_1, trans_u428_1)
bigDisj4ea_u428 = Or(possi_u428_0, possi_u428_1)
atom_u626 = u626[0] * 1 + u626[1] * 1 >= 2
ea_u428 = And(15 >= 1, Exists([u626[0], u626[1]], And(bigDisj4ea_u428, atom_u626)))
u126 = [Int('u126_%d' %i) for i in range(2)]
act_cstr_u292_0 = 5 == 5
left_side_cstr_u292_0 = u292[0] >= 1
trans_u292_0 = And(u126[0] == u292[0]-1+0, u126[1] == u292[1]+1)
possi_u292_0 = And(act_cstr_u292_0, left_side_cstr_u292_0, trans_u292_0)
act_cstr_u292_1 = 5 == 10
left_side_cstr_u292_1 = u292[1] >= 1
trans_u292_1 = And(u126[0] == u292[0]+2, u126[1] == u292[1]-1+0)
possi_u292_1 = And(act_cstr_u292_1, left_side_cstr_u292_1, trans_u292_1)
bigDisj4ea_u292 = Or(possi_u292_0, possi_u292_1)
atom_u126 = u126[0] * 1 + u126[1] * 1 >= 2
ea_u292 = And(15 >= 1, Exists([u126[0], u126[1]], And(bigDisj4ea_u292, atom_u126)))
u1160 = [Int('u1160_%d' %i) for i in range(2)]
act_cstr_u246_0 = 5 == 5
left_side_cstr_u246_0 = u246[0] >= 1
trans_u246_0 = And(u1160[0] == u246[0]-1+0, u1160[1] == u246[1]+1)
possi_u246_0 = And(act_cstr_u246_0, left_side_cstr_u246_0, trans_u246_0)
act_cstr_u246_1 = 5 == 10
left_side_cstr_u246_1 = u246[1] >= 1
trans_u246_1 = And(u1160[0] == u246[0]+2, u1160[1] == u246[1]-1+0)
possi_u246_1 = And(act_cstr_u246_1, left_side_cstr_u246_1, trans_u246_1)
bigDisj4ea_u246 = Or(possi_u246_0, possi_u246_1)
atom_u1160 = u1160[0] * 1 + u1160[1] * 1 >= 2
ea_u246 = And(15 >= 1, Exists([u1160[0], u1160[1]], And(bigDisj4ea_u246, atom_u1160)))
u1007 = [Int('u1007_%d' %i) for i in range(2)]
act_cstr_u1050_0 = 5 == 5
left_side_cstr_u1050_0 = u1050[0] >= 1
trans_u1050_0 = And(u1007[0] == u1050[0]-1+0, u1007[1] == u1050[1]+1)
possi_u1050_0 = And(act_cstr_u1050_0, left_side_cstr_u1050_0, trans_u1050_0)
act_cstr_u1050_1 = 5 == 10
left_side_cstr_u1050_1 = u1050[1] >= 1
trans_u1050_1 = And(u1007[0] == u1050[0]+2, u1007[1] == u1050[1]-1+0)
possi_u1050_1 = And(act_cstr_u1050_1, left_side_cstr_u1050_1, trans_u1050_1)
bigDisj4ea_u1050 = Or(possi_u1050_0, possi_u1050_1)
atom_u1007 = u1007[0] * 1 + u1007[1] * 1 >= 2
ea_u1050 = And(15 >= 1, Exists([u1007[0], u1007[1]], And(bigDisj4ea_u1050, atom_u1007)))
u704 = [Int('u704_%d' %i) for i in range(2)]
act_cstr_u1232_0 = 5 == 5
left_side_cstr_u1232_0 = u1232[0] >= 1
trans_u1232_0 = And(u704[0] == u1232[0]-1+0, u704[1] == u1232[1]+1)
possi_u1232_0 = And(act_cstr_u1232_0, left_side_cstr_u1232_0, trans_u1232_0)
act_cstr_u1232_1 = 5 == 10
left_side_cstr_u1232_1 = u1232[1] >= 1
trans_u1232_1 = And(u704[0] == u1232[0]+2, u704[1] == u1232[1]-1+0)
possi_u1232_1 = And(act_cstr_u1232_1, left_side_cstr_u1232_1, trans_u1232_1)
bigDisj4ea_u1232 = Or(possi_u1232_0, possi_u1232_1)
atom_u704 = u704[0] * 1 + u704[1] * 1 >= 2
ea_u1232 = And(15 >= 1, Exists([u704[0], u704[1]], And(bigDisj4ea_u1232, atom_u704)))
u74 = [Int('u74_%d' %i) for i in range(2)]
act_cstr_u1402_0 = 5 == 5
left_side_cstr_u1402_0 = u1402[0] >= 1
trans_u1402_0 = And(u74[0] == u1402[0]-1+0, u74[1] == u1402[1]+1)
possi_u1402_0 = And(act_cstr_u1402_0, left_side_cstr_u1402_0, trans_u1402_0)
act_cstr_u1402_1 = 5 == 10
left_side_cstr_u1402_1 = u1402[1] >= 1
trans_u1402_1 = And(u74[0] == u1402[0]+2, u74[1] == u1402[1]-1+0)
possi_u1402_1 = And(act_cstr_u1402_1, left_side_cstr_u1402_1, trans_u1402_1)
bigDisj4ea_u1402 = Or(possi_u1402_0, possi_u1402_1)
atom_u74 = u74[0] * 1 + u74[1] * 1 >= 2
ea_u1402 = And(15 >= 1, Exists([u74[0], u74[1]], And(bigDisj4ea_u1402, atom_u74)))
u279 = [Int('u279_%d' %i) for i in range(2)]
act_cstr_u1381_0 = 5 == 5
left_side_cstr_u1381_0 = u1381[0] >= 1
trans_u1381_0 = And(u279[0] == u1381[0]-1+0, u279[1] == u1381[1]+1)
possi_u1381_0 = And(act_cstr_u1381_0, left_side_cstr_u1381_0, trans_u1381_0)
act_cstr_u1381_1 = 5 == 10
left_side_cstr_u1381_1 = u1381[1] >= 1
trans_u1381_1 = And(u279[0] == u1381[0]+2, u279[1] == u1381[1]-1+0)
possi_u1381_1 = And(act_cstr_u1381_1, left_side_cstr_u1381_1, trans_u1381_1)
bigDisj4ea_u1381 = Or(possi_u1381_0, possi_u1381_1)
atom_u279 = u279[0] * 1 + u279[1] * 1 >= 2
ea_u1381 = And(15 >= 1, Exists([u279[0], u279[1]], And(bigDisj4ea_u1381, atom_u279)))
sub_bigConj_u = And([ea_u179, ea_u179, ea_u199, ea_u957, ea_u112, ea_u865, ea_u655, ea_u796, ea_u134, ea_u428, ea_u292, ea_u246, ea_u1050, ea_u1232, ea_u1402, ea_u1381])
eg_u = Exists([u179[0], u179[1], u179[0], u179[1], u199[0], u199[1], u957[0], u957[1], u112[0], u112[1], u865[0], u865[1], u655[0], u655[1], u796[0], u796[1], u134[0], u134[1], u428[0], u428[1], u292[0], u292[1], u246[0], u246[1], u1050[0], u1050[1], u1232[0], u1232[1], u1402[0], u1402[1], u1381[0], u1381[1]], And(path_u, initial_u, sub_bigConj_u))

t.add(eg_u)
print(t.check())

elapsed = time.clock() - start
print("Time used: %.3fs" %elapsed)

print("-- finished --")