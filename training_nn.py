from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer


def get_connections(net):
    for mod in net.modules:
        for conn in net.connections[mod]:
            print conn
            for cc in range(len(conn.params)):
                print conn.whichBuffers(cc), conn.params[cc]

# Create network
net = buildNetwork(2, 3, 1, bias=True, hiddenclass=TanhLayer)

# Create dataset
ds = SupervisedDataSet(2, 1)

ds.addSample((0, 0), (0,))
ds.addSample((1, 0), (1,))
ds.addSample((0, 1), (1,))
ds.addSample((1, 1), (0,))

# Train
trainer = BackpropTrainer(net, ds)

trainer.trainUntilConvergence()


# Export net
get_connections(net)
print net.activate([0, 1])
