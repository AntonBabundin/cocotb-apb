# cocotb-apb
APB interface on Python for cocotb framework

# Connection Example 

```{python}
class Connection:
    def __init__(self, dut):
        self.dut = dut
        # Init interface
        print (dut.apb.m.penable, dut.apb.s.pready)
        self.apb = ApbMaster(dut.apb, name=None, clock=dut.clk)

@cocotb.test()
async def simple_test(dut):
    ### Create connection ###
    connect_with_dut = Connection(dut)  # Connect with DUT phase
```

apb = ApbMaster(dut.apb, name=None, clock=dut.clk) #connect with  APB SystemVerilog interface. If you want to conncet by prefix, use field 'name'

#### `ApbMaster` constructor parameters

* _bus_: `ApbMaster` object containing Apb interface signals
* _clock_: clock signal
* _name_: If you want to conncet by prefix, like "i_"

#### ApbMaster Methods
* `write(addr, data, strb=0xF, verbose=False)`: write data, on addr
* `read(addr, verbose=False)`: read data on addr




