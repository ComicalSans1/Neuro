from brian2 import *

def lif_neuron(curr, run_time, v_rest=-70*mV, v_reset=-65*mV, threshold=-50*mV, membrane_r=10.*Mohm, time_constant=8.*ms, refractory_period=2.0*ms):
    eqs = '''
    dv/dt = ( -(v - v_rest) + membrane_r * curr(t, i) ) / time_constant : volt (unless refractory)
    '''
    G = NeuronGroup(
    1, eqs, threshold='v > threshold', 
    reset="v = v_reset", method="linear", refractory=refractory_period)
    M = StateMonitor(G, True, True)
    S = SpikeMonitor(G)
    run(run_time)
    return M, S