from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

import numpy

import time

NUM_LINES = 7
NUM_COLUMNS = 8

HIDDEN_LAYER_SIZE = 8


def set_dataset(ds, i, j):
    with open('dataset.data', 'r') as f:
        lines = f.readlines()
        lines = lines[i:j]
        for line in lines:
            line = line.split(",")
            ds_target = [int(line[-1])]
            ds_input = [int(n) for n in line[0:-1]]
            ds.addSample(ds_input, ds_target)


def get_connections(net):
    for mod in net.modules:
        for conn in net.connections[mod]:
            print conn
            for cc in range(len(conn.params)):
                print conn.whichBuffers(cc), conn.params[cc]


def get_connections_to_file(net, file_name):
    in_to_hidden = numpy.zeros(shape=(57, 8))
    hidden_to_out = numpy.zeros(shape=(9, 1))
    count = 1
    with open(file_name, 'w') as f:
        for mod in net.modules:
            for conn in net.connections[mod]:
                for cc in range(len(conn.params)):
                    value = conn.params[cc]
                    if count <= 9:
                        hidden_to_out[count - 1] = value
                    elif count <= 17:
                        in_to_hidden[56][count - 10] = value
                    else:
                        i = count - 18
                        in_to_hidden[i / 8][i % 8] = value
                    count += 1
        f.write(repr(in_to_hidden))
        f.write('\n')
        f.write(repr(hidden_to_out))
        f.write('\n')


print 'Create network'
net = buildNetwork(NUM_LINES * NUM_COLUMNS, HIDDEN_LAYER_SIZE, 1, bias=True)

ds = None
trainer = None
step = 100
count = 0
while True:
    print 'Create dataset'
    ds = SupervisedDataSet(NUM_LINES * NUM_COLUMNS, 1)
    set_dataset(ds, count * step, (count + 1) * step)

    print 'Train'
    trainer = BackpropTrainer(net, ds)

    start = time.time()
    trainer.trainUntilConvergence()
    print time.time() - start

    # Export net
    # get_connections(net)
    print 'save network from ' + str(count * step) + ' to ' + str((count + 1) * step)
    get_connections_to_file(net, 'network_' + str(count) + '.data')

    count += 1
